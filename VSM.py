import re
import os
import zipfile
import sys
from parsing import get_term_key
from parsing import get_term_val
from parsing import get_main_key
from parsing import get_main_val
from parsing import get_doc_key
from parsing import get_doc_val
from parsing import get_map
from parsing import get_termInfo

term_key_list = get_term_key()
term_val_list = get_term_val()

main_key_list = get_main_key()
main_val_list = get_main_val()

doc_key_list = get_doc_key()
doc_val_list = get_doc_val()

map = get_map()
termInfo = get_termInfo()
queryDict = {}

stop_file = open("stopwords.txt", "r")
temp_stopwords = stop_file.readlines()
stopwords = []
for word in temp_stopwords:
    stopwords.append(word.replace("\n", ""))
stop_file.close()


query_list = open('query_list.txt', 'r') # FIXME update this to accept command line filename
lines = query_list.readlines()
# Populates queryDict where key = query number and val = each word of query 
for line in lines:
    line = re.sub("[^0-9a-zA-Z ]+", "", line)
    word_list = line.split()
    word_list = [i for i in word_list if i not in stopwords] # Source of this line: https://www.techiedelight.com/remove-all-occurrences-item-list-python/
    queryDict[word_list[0]] = word_list[1:]

for query in queryDict:

# print(main_val_list[0])
print(map)