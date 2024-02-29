class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False

class bwd_Trie:
    def __init__(self):
        self.root = TrieNode()

    def getNode(self):
        return TrieNode()

    def _charToIndex(self, ch):
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
        for a in range(26):
            if node.children[a] is not None:
                self._search(node.children[a], prefix + chr(a + ord('a')), result)

    def bwd_search(self, key):
        pCrawl = self.root
        for level in key:
            index = self._charToIndex(level)
            if not pCrawl.children[index]:
                return []  # Key not present
            pCrawl = pCrawl.children[index]

        result = []
        self._search(pCrawl, key, result)
        return result

# Driver function
def main():
    # Initialize the Trie
    t = bwd_Trie()

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
            t.insert(new_string)

    # Example search
    bwd_result = t.bwd_search("e")
    print(bwd_result)

if __name__ == '__main__':
    main()

