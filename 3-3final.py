from createTrie import trie_root, search_token_in_trie
import json
from main import intersection
import cProfile

def and_query_trie(query_terms):
    # load postings in memory

    # postings for only the query terms
    final = []
    for q in query_terms:
        result = search_token_in_trie(trie_root, q)
        
        if result:
            if final == []:
                final = result[1]
            final = intersection(final, result[1])
        else:
            return "Query not found in corpus. Please try again."
    print(final)
    # sort tokens in increasing order of their
    # frequencies


# token_to_search = "among"
# result = search_token_in_trie(trie_root, token_to_search)

# if result:
#     doc_freq, postings = result
#     print(f"Token: {token_to_search}")
#     print(f"Document Frequency: {doc_freq}")
#     print(f"Postings: {postings}")
# else:
#     print(f"Token '{token_to_search}' not found in trie.")
    

def read_and_print_queries(file_path):
    # print(and_query(["folk", "folk"],'/Users/vivanjain/Downloads/IR_Assignment-main/IR_Assignment-main/s2/'))

    with open(file_path, 'r') as file:
        # Load queries from JSON file into a Python object
        json_file = json.load(file)

        for json_object in json_file['queries']:
            arr = []
            qid = json_object['qid']
            query = json_object['query']
            tokens = query.split(" ")
            for t in tokens:
                # print(t, end = " ")
                arr.append(t)
            # print()
            print(arr)
            
            print(and_query_trie(arr))
            
# def dummy():
#     # print("Dummy")
#     and_query_trie(["machine", "learning"])
    
# dummy()

cProfile.run(read_and_print_queries('/Users/vivanjain/Downloads/IR_Assignment-main/IR_Assignment-main/s2/s2_query.json'))