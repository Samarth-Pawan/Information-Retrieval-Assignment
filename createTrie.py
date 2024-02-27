

class TrieNode:
    def __init__(self):
        self.children = {}
        self.doc_freq = 0
        self.postings = []


def insert_into_trie(root, token, freq, postings):
    node = root
    for char in token:
        if char not in node.children:
            node.children[char] = TrieNode()
        node = node.children[char]
    node.doc_freq = freq
    node.postings = postings


def load_index_in_memory_with_trie():
    f = open("/Users/vivanjain/Downloads/IR_Assignment-main/IR_Assignment-main/s2/intermediate/postings.tsv", encoding="utf-8")
    root = TrieNode()

    for line in f:
        splitline = line.split("\t")

        token = splitline[0]
        freq = int(splitline[1])
        item_list = [splitline[i].strip() for i in range(2, len(splitline))]

        insert_into_trie(root, token, freq, item_list)

    f.close()
    return root



def print_trie(root, level=0):
    if root is None:
        return

    print("  " * level + f"{root.doc_freq} : {root.postings}")

    for char, child_node in root.children.items():
        print_trie(child_node, level + 1)


def search_token_in_trie(root, token):
    node = root
    for char in token:
        if char not in node.children:
            # Token not found in trie
            return None

        node = node.children[char]

    # Token found in trie, return doc_freq and postings
    return node.doc_freq, node.postings

# Example usage:
trie_root = load_index_in_memory_with_trie()
# print_trie(trie_root)




# trie_root = load_index_in_memory_with_trie()
# token_to_search = "analytical,"
# result = search_token_in_trie(trie_root, token_to_search)

# if result:
#     doc_freq, postings = result
#     print(f"Token: {token_to_search}")
#     print(f"Document Frequency: {doc_freq}")
#     print(f"Postings: {postings}")
# else:
#     print(f"Token '{token_to_search}' not found in trie.")