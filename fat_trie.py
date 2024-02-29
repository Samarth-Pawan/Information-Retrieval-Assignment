from bwd_trie import bwd_Trie
from trie import fwd_Trie

b= bwd_Trie()

    # Initialize the Trie
    

    # Open the postings.tsv file and read lines
with open('/Users/srivantv/Downloads/IR_Assignment-main 2/IR_Assignment-main/s2/intermediate/postings.tsv', 'r') as file:
    for line in file:
        # Split each line into word, frequency, and docID
        parts = line.strip().split('\t')
        word = parts[0]  # Extract the word

        new_string = ""

        for char in word:
            if ord(char)>=97 and ord(char)<=122:
                new_string += char
            elif 65<=ord(char)<=90:
                new_string += char.lower()
            
            # if 65<=ord(char)<=90:
            #     char=char.replace(char,char.lower())
            # elif ord(char) < 97 or ord(char)>122:
            #     char=char.replace(char,'')


        # Insert the word into the Trie
        new_string=''.join(reversed(new_string))
        b.insert(new_string)


    
f = fwd_Trie()

    # Initialize the Trie
    

    # Open the postings.tsv file and read lines
with open('/Users/srivantv/Downloads/IR_Assignment-main 2/IR_Assignment-main/s2/intermediate/postings.tsv', 'r') as file:
    for line in file:
        # Split each line into word, frequency, and docID
        parts = line.strip().split('\t')
        word = parts[0]  # Extract the word

        new_string = ""

        for char in word:
            if ord(char)>=97 and ord(char)<=122:
                new_string += char
            elif 65<=ord(char)<=90:
                new_string += char.lower()
            
            # if 65<=ord(char)<=90:
            #     char=char.replace(char,char.lower())
            # elif ord(char) < 97 or ord(char)>122:
            #     char=char.replace(char,'')


        # Insert the word into the Trie
        f.insert(new_string)



input="there*"
fwd=""
bwd=""
flag=0
for i in input:
    if i=='*' and flag==0:
        flag=1
    elif flag==0:
        fwd+=i
    else:
        bwd+=i
# print(fwd)
# print(bwd)
bwd=''.join(reversed(bwd))
#print(bwd)

bwd_result = b.bwd_search(bwd)
fwd_result = f.search(fwd)
#print(bwd_result)
common1=[]
def find_common_elements(bwd_result, fwd_result):
    common_elements = []  # Use a different name for the list to avoid confusion
    for el in bwd_result:
        el=''.join(reversed(el))
        #print(el)
        if el in fwd_result:
            common_elements.append(el)
    return common_elements
common_words = find_common_elements(bwd_result, fwd_result)
print(common_words)

