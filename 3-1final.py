import json
from main import and_query 
import cProfile
from memory_profiler import profile

# Path to your JSON file
file_path = '/Users/vivanjain/Downloads/IR_Assignment-main/IR_Assignment-main/s2/s2_query.json'

# Function to read and print queries from JSON file
@profile
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
            print(and_query(arr,'/Users/vivanjain/Downloads/IR_Assignment-main/IR_Assignment-main/s2/'))

cProfile.run('read_and_print_queries(file_path)')
# print(and_query(["machine", "learning"], '/Users/vivanjain/Downloads/IR_Assignment-main/IR_Assignment-main/s2/'))
