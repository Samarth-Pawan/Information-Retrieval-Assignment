def load_inverted_index(file_path):
    inverted_index = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            term, freq, *doc_ids = line.strip().split('\t')
            inverted_index[term] = {'freq': int(freq), 'doc_ids': set(doc_ids)}
    return inverted_index

def boolean_retrieval(query, inverted_index):
    query_terms = query.split()
    result = None
    
    for term in query_terms:
        if term in inverted_index:
            if result is None:
                result = inverted_index[term]['doc_ids']
            else:
                if term.startswith('NOT'):
                    term = term[3:]
                    result.difference_update(inverted_index[term]['doc_ids'])
                elif term == 'OR':
                    _, next_term = query_terms[query_terms.index(term) + 1], query_terms[query_terms.index(term) + 2]
                    result.update(inverted_index[next_term]['doc_ids'])
                elif term == 'AND':
                    _, next_term = query_terms[query_terms.index(term) + 1], query_terms[query_terms.index(term) + 2]
                    result.intersection_update(inverted_index[next_term]['doc_ids'])
    return result if result else set()

def main():
    inverted_index = load_inverted_index("inverted_index.tsv")
    
    # Sample queries
    queries = [
        "deep AND learning",
        "machine OR learning",
        "NOT deep",
        "machine AND NOT learning"
    ]
    
    for query in queries:
        result = boolean_retrieval(query, inverted_index)
        print(f"Query: {query}\nResult: {result}\n")

if __name__ == "__main__":
    main()
