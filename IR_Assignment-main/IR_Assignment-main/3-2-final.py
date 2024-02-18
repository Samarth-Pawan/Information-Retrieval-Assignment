import nltk
from nltk.stem import PorterStemmer
import nltk 
from nltk import word_tokenize
nltk.download('wordnet')
from nltk.corpus import stopwords
nltk.download('stopwords')
from nltk.stem import WordNetLemmatizer
stop_words = set(stopwords.words('english'))

stemmer = PorterStemmer()
lemmatizer=WordNetLemmatizer()




with open("/Users/vivanjain/Downloads/IR_Assignment-main/IR_Assignment-main/s2/intermediate/postings.tsv", "r", encoding="utf-8") as f, open("/Users/vivanjain/Downloads/IR_Assignment-main/IR_Assignment-main/s2/intermediate/stemmed.tsv", "w", encoding="utf-8") as o:
  # Write header for the new file
    postings = {}
    doc_freq = {}

    for line in f:
        splitline = line.split("\t")

        token = splitline[0]
        if token.lower() not in stop_words:
                lem=lemmatizer.lemmatize(token.lower())
                stem = stemmer.stem(lem)
        else:
            continue
        
        freq = int(splitline[1])
        doc_freq[token] = doc_freq.get(token, 0) + freq

        item_list = []

        for item in range(2, len(splitline)):
            item_list.append(splitline[item].strip())
        postings[token] = postings.get(token, []) + item_list
    for a,b in doc_freq.items():
        o.write(a + "\t" + str(b) + "\t" + "\t".join(postings[a]) + "\n")