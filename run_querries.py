import json
from main import and_query 

# Path to your JSON file
file_path = '/Users/srivantv/Downloads/IR_Assignment-main 2/IR_Assignment-main/s2/s2_query.json'

# Function to read and print queries from JSON file
def read_and_print_queries(file_path):
    print(and_query(["folk", "folk"],'/Users/srivantv/Downloads/IR_Assignment-main 2/IR_Assignment-main/s2/'))

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
            # print(and_query(arr,'/Users/srivantv/Downloads/IR_Assignment-main 2/IR_Assignment-main/s2/'))
            


            # tokens = paper_abstract.split(" ")
            # for t in tokens:
            #     o.write(t.lower() + "\t" + str(doc_no) + "\n")
        
        # Assuming queries is a list of dictionaries as per your example
        for query in queries:
            print(f"QID: {query[0]}, Query: {query[1]}")

# Call the function with the path to your JSON file
read_and_print_queries(file_path)
