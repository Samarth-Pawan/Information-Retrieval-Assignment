import cProfile
import json
all_times = []

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

def find_common_elements(bwd_result, fwd_result):
    common_elements = []  # Use a different name for the list to avoid confusion
    for el in bwd_result:
        el=''.join(reversed(el))
        #print(el)
        if el in fwd_result:
            common_elements.append(el)
    return common_elements

#input="there*"
with open('/Users/srivantv/Downloads/IR_Assignment-main 2/IR_Assignment-main/s2/s2_wildcard.json', 'r') as file:
    queries_data = json.load(file)

# Profiling and executing each query
for query in queries_data['queries']:
    input_query = query['query']
    fwd = ""
    bwd = ""
    flag = 0
    for i in input_query:
        if i == '*' and flag == 0:
            flag = 1
        elif flag == 0:
            fwd += i
        else:
            bwd += i
    bwd = ''.join(reversed(bwd))

    # Start profiling
    profiler = cProfile.Profile()
    profiler.enable()

    # Execute search
    bwd_result = b.bwd_search(bwd)
    fwd_result = f.search(fwd)
    common_words = find_common_elements(bwd_result, fwd_result)
    
    # Stop profiling
    profiler.disable()
    stats = profiler.getstats()
    time_taken = sum(stat.totaltime for stat in stats)
    all_times.append(time_taken)
    # Print results and profiling information
    print(f"Query: {input_query}, Common Words: {common_words}")
    #profiler.print_stats()
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
print("min: ", min)


