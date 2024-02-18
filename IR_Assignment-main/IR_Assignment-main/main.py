# This is a sample Python script.

import shutil
import os
import json
import numpy as np


# reads s2 corpus in json and
# creates an intermediary file
# containing token and doc_id pairs.

def read_json_corpus(json_path):
    f = open(json_path + "/s2_doc.json", encoding="utf-8")
    json_file = json.load(f)
    if not os.path.exists(json_path + "/intermediate/"):
        os.mkdir(json_path + "/intermediate/")
    o = open(json_path + "/intermediate/output.tsv", "w", encoding="utf-8")
    for json_object in json_file['all_papers']:
        doc_no = json_object['docno']
        title = json_object['title'][0]
        paper_abstract = json_object['paperAbstract'][0]
        tokens = title.split(" ")
        for t in tokens:
            o.write(t.lower() + "\t" + str(doc_no) + "\n")
        tokens = paper_abstract.split(" ")
        for t in tokens:
            o.write(t.lower() + "\t" + str(doc_no) + "\n")
    o.close()


# sorts (token, doc_id) pairs
# by token first and then doc_id
def sort(dir):
    f = open(dir + "/intermediate/output.tsv", encoding="utf-8")
    o = open(dir + "/intermediate/output_sorted.tsv", "w", encoding="utf-8")

    # initialize an empty list of pairs of
    # tokens and their doc_ids
    pairs = []

    for line in f:
        line = line[:-1]
        split_line = line.split("\t")
        if len(split_line) == 2:
            pair = (split_line[0], split_line[1])
            pairs.append(pair)

    # sort (token, doc_id) pairs by token first and then doc_id
    sorted_pairs = sorted(pairs, key=lambda x: (x[0], x[1]))

    # write sorted pairs to file
    for sp in sorted_pairs:
        o.write(sp[0] + "\t" + sp[1] + "\n")
    o.close()


# converts (token, doc_id) pairs
# into a dictionary of tokens
# and an adjacency list of doc_id
def construct_postings(dir):
    # open file to write postings
    o1 = open(dir + "/intermediate/postings.tsv", "w", encoding="utf-8")

    postings = {}  # initialize our dictionary of terms
    doc_freq = {}  # document frequency for each term

    # read the file containing the sorted pairs
    f = open(dir + "/intermediate/output_sorted.tsv", encoding="utf-8")

    # initialize sorted pairs
    sorted_pairs = []

    # read sorted pairs
    for line in f:
        line = line[:-1]
        split_line = line.split("\t")
        pairs = (split_line[0], split_line[1])
        sorted_pairs.append(pairs)

    # construct postings from sorted pairs
    for pairs in sorted_pairs:
        if pairs[0] not in postings:
            postings[pairs[0]] = []
            postings[pairs[0]].append(pairs[1])
        else:
            len_postings = len(postings[pairs[0]])
            if len_postings >= 1:
                # check for duplicates
                # assuming the doc_ids are sorted
                # the same doc_ids will appear
                # one after another and detected by
                # checking the last element of the postings
                if pairs[1] != postings[pairs[0]][len_postings - 1]:
                    postings[pairs[0]].append(pairs[1])

    # update doc_freq which is the size of postings list
    for token in postings:
        doc_freq[token] = len(postings[token])

    # print("postings: " + str(postings))
    # print("doc freq: " + str(doc_freq))
    print("Dictionary size: " + str(len(postings)))

    # write postings and document frequency to file

    for token in postings:
        o1.write(token + "\t" + str(doc_freq[token]))
        for l in postings[token]:
            o1.write("\t" + l)
        o1.write("\n")
    o1.close()


# starting the indexing process
def index(dir):
    # reads the corpus and
    # creates an intermediary file
    # containing token and doc_id pairs.
    # read_corpus(dir)
    read_json_corpus(dir)

    # sorts (token, doc_id) pairs
    # by token first and then doc_id
    sort(dir)

    # converts (token, doc_id) pairs
    # into a dictionary of tokens
    # and an adjacency list of doc_id
    construct_postings(dir)


def load_index_in_memory(dir):
    f = open(dir + "intermediate/postings.tsv", encoding="utf-8")
    postings = {}
    doc_freq = {}

    for line in f:
        splitline = line.split("\t")

        token = splitline[0]
        freq = int(splitline[1])

        doc_freq[token] = freq

        item_list = []

        for item in range(2, len(splitline)):
            item_list.append(splitline[item].strip())
        postings[token] = item_list

    return postings, doc_freq


def intersection(l1, l2):
    count1 = 0
    count2 = 0
    intersection_list = []

    while count1 < len(l1) and count2 < len(l2):
        if l1[count1] == l2[count2]:
            intersection_list.append(l1[count1])
            count1 = count1 + 1
            count2 = count2 + 1
        elif l1[count1] < l2[count2]:
            count1 = count1 + 1
        elif l1[count1] > l2[count2]:
            count2 = count2 + 1

    return intersection_list


def and_query(query_terms, corpus):
    # load postings in memory
    postings, doc_freq = load_index_in_memory(corpus)

    # postings for only the query terms
    postings_for_keywords = {}
    doc_freq_for_keywords = {}

    for q in query_terms:
        try:
            postings_for_keywords[q] = postings[q]
        except:
            print("Query not found in corpus. Please try again.")


    # store doc frequency for query token in
    # dictionary

    for q in query_terms:
        try:
            doc_freq_for_keywords[q] = doc_freq[q]
        except:
            print("Query not found in corpus. Please try again.")

    # sort tokens in increasing order of their
    # frequencies

    sorted_tokens = sorted(doc_freq_for_keywords.items(), key=lambda x: x[1])

    # initialize result to postings list of the
    # token with minimum doc frequency

    result = postings_for_keywords[sorted_tokens[0][0]]

    # iterate over the remaining postings list and
    # intersect them with result, and updating it
    # in every step

    for i in range(1, len(postings_for_keywords)):
        result = intersection(result, postings_for_keywords[sorted_tokens[i][0]])
        if len(result) == 0:
            return result

    return result


# Code starts here
if __name__ == '__main__':
    index('/Users/vivanjain/Downloads/IR_Assignment-main/IR_Assignment-main/s2')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/








