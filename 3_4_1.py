import json
import cProfile 
all_times = []
my_dict = {}

file_path = '/Users/srivantv/Downloads/IR_Assignment-main 2/IR_Assignment-main/s2/s2_wildcard.json'

class TrieNode:
    def __init__(self):
        self.children = [None] * 27  # 26 letters + '{'
        self.isEndOfWord = False

class fwd_Trie:
    def __init__(self):
        self.root = TrieNode()

    def getNode(self):
        return TrieNode()

    def _charToIndex(self, ch):
        # Adjust to handle '{', mapping it to index 26
        if ch == '{':
            return 26
        return ord(ch) - ord('a')

    def insert(self, key):
        pCrawl = self.root
        for level in key:
            index = self._charToIndex(level)
            if not pCrawl.children[index]:
                pCrawl.children[index] = self.getNode()
            pCrawl = pCrawl.children[index]
        pCrawl.isEndOfWord = True

    def _search(self, node, prefix, result):
        if node.isEndOfWord:
            result.append(prefix)
        for a in range(27):
            if node.children[a] is not None:
                self._search(node.children[a], prefix + chr(a + ord('a')), result)

    def search(self, key):
        pCrawl = self.root
        for level in key:
            index = self._charToIndex(level)
            if not pCrawl.children[index]:
                return []  # Key not present
            pCrawl = pCrawl.children[index]

        result = []
        self._search(pCrawl, key, result)
        return result


def read_and_print_queries():
    with open(file_path, 'r') as file:
        json_file = json.load(file)

        for json_object in json_file['queries']:
            profiler = cProfile.Profile()
            profiler.enable()

            qid = json_object['qid']
            query = json_object['query']
            parts = query.split('*')
            # Correct placement of the query transformation
            transformed_query = parts[1] + '{' + parts[0]

            result_keys = t.search(transformed_query)
            result_list = [my_dict[key] for key in result_keys if key in my_dict]  # Ensure the key exists in my_dict

            print(result_list)

            profiler.disable()
            stats = profiler.getstats()
            time_taken = sum(stat.totaltime for stat in stats)
            all_times.append(time_taken)

t = fwd_Trie()
def rotate_string(s, k):
    # Ensure k is within the length of s
    k = k % len(s)
    return s[k:] + s[:k]

def generate_permuterm(word):
    term = word + '{'
    for i in range(len(term)):
        rotated_term = rotate_string(term, i)
        my_dict[rotated_term] = word
        t.insert(rotated_term)
# def search(prefix):
#     result_keys = [key for key in my_dict if key.startswith(prefix)]
#     result_list = [my_dict[key] for key in result_keys]
#     return result_list

def main():
    # Example input to replace file reading for demonstration
    
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

        # Insert the word into the Trie
            generate_permuterm(new_string)
    #print(t)
    
    read_and_print_queries()

    print(all_times)

    max = 0
    min = 100
    total = 0
    for i in all_times:
        total += i
        if i>max:
            max = i
        if i<min:
            min = i

    
    print("total: ", total)
    print("average: ", total/len(all_times))
    print("max: ", max)
    print("max: ", min)

    
    
    # query = "m*g"
    # parts = query.split('*')
    # transformed_query = parts[1] + '$' + parts[0]  # Rearrange the query to fit the permuterm index structure
    
    # results = search(transformed_query)
    
    # print(results)

# Assuming the file reading and actual data handling is correct, replace the example words with your file reading logic.
main()
