#!/usr/bin/env python
from __future__ import division 
import sys
#from sets import Set
import re
from math import log


def featurize(train_articles, test_articles):
    '''
    Returns a tuple (train_features, test_features) of matrices of
    features. Each matrix is list of feature vectors, where a feature vector is
    simply a list of numbers. Note that features must be converted here to the
    proper numerical type (e.g., booleans should be converted to integers).
        
    You may find that returning a list of feature vectors is too
    memory-intensive. You can reduce memory usage considerably by defining the
    matrix as a Python generator that yields feature vectors, instead of
    building the whole list of vectors. For example, if your matrix was defined
    as [make_features(article) for article in articles], you could instead write
    (make_features(article) for article in articles). See
    https://wiki.python.org/moin/Generators for more details on
    generators. (Note that this approach may increase running time.)

    If you would like to examine an actual instance of the return type, try
    running the following function call using the default implementation:
       featurize(['train 1', 'training article 2'], ['test 1', 'the second test article'])
    and inspecting the return value.
    '''

    def contains_digits(d):
        return bool(re.compile('\d').search(d))

    def get_stopword():
        stopword_set = set()
        with open("parameters.txt", 'r') as in_file:
            for line in in_file.readlines():
                line = line.rstrip()      # Remove trailing whitespace.
                if line:                  # Only process non-empty lines.
                    stopword_set.add(line)
        return stopword_set
        # get all different word
    def get_word_set(train_articles, test_articles, stopword_set):
        word_set = set()
        for line in train_articles:
            tmpList = line.split()
            #print  tmpList
            #sys.exit()
            for word in tmpList:
                if word not in stopword_set and not contains_digits(word):
                    if word not in word_set:
                        word_set.add(word)

            #print word_set
            #sys.exit()

        for line in test_articles:
            #re.sub('^[0-9 ]+', '', line)
            tmpList = line.split()
            for word in tmpList:
                if word not in stopword_set and not contains_digits(word):
                    if word not in word_set:
                        word_set.add(word)


        return word_set

    def get_word_dic(train_articles, test_articles, stopword_set):
    	word_dict = {}
        word_set = set()
    	for line in train_articles:
            tmpList = line.split()  
            tmpSet = set(tmpList)        
      
            for word in tmpSet:
                if word not in stopword_set and not contains_digits(word):
                    if word in word_dict:
                        word_dict[word] = word_dict[word] + 1;
		    else:
			word_dict[word] = 1

        cur_line = 0

    	for line in test_articles:
            tmpList = line.split()
            tmpSet = set(tmpList)        
            for word in tmpSet:
                if word not in stopword_set and not contains_digits(word):
                    if word in word_dict:
                        word_dict[word] = word_dict[word] + 1;
                    else:
                        word_dict[word] = 1
    	#print word_dict["game"]
        #sys.exit()
        i = 0
        word_list = []
        for word in word_dict:
            if word_dict[word] > 500:
                #print word + " " + (str)(word_dict[word])
                word_list.append(word)
                i = i + 1

        #print i
        #sys.exit()
    	return word_list
			 

	

    ### REPLACE THE REST OF THIS FUNCTION WITH YOUR FEATURE GENERATION CODE ###
    def make_features(articles):
        # store the stop words
        stopword_set = get_stopword()
        word_list = get_word_dic(train_articles, test_articles, stopword_set)
        Matrix = [[0 for x in xrange(len(word_list))] for x in xrange(len(articles))]
        idf_counter = []
        for word in word_list:
            i = 0
            for line in train_articles:
                if word in line:
                    i = i + 1
            for line in test_articles:
                if word in line:
                    i = i + 1
            idf_counter.append(i)
        #print idf_counter
        idf = [log((len(test_articles)+len(test_articles))/n) for n in idf_counter]

        i = 0
        for line in train_articles:
            tf_counter = []
            tf = []
            tmpList = []
            tmpList = line.split()
            for word in word_list:
                tf_counter.append(tmpList.count(word))
            t = max(tmpList.count(word) for word in tmpList)
            tf = [(0.5+(0.5*n/t)) for n in tf_counter]
            for j in range(len(word_list)):
                Matrix[i][j] = tf[j]*idf[j]
            #print Matrix[i]
            i = i + 1
            #if i == 10:
                #sys.exit()

        return Matrix
       
    return (make_features(train_articles), make_features(test_articles))

def articles_to_features(train_in_name, train_out_name, test_in_name, test_out_name):
    with open(train_in_name, 'r') as in_file:
        train_lines = in_file.readlines()
    with open(test_in_name, 'r') as in_file:
        test_lines = in_file.readlines()


    train_features, test_features = featurize(train_lines, test_lines)
    for features, out_name in ((train_features, train_out_name),
                               (test_features, test_out_name)):
        with open(out_name, 'wb') as csvfile:
            # Output features in MATLAB-readable CSV format
            for row in features:
                
                csvfile.write(', '.join([str(feature) for feature in row]))
                csvfile.write('\n')

if __name__ == '__main__':
    articles_to_features(*sys.argv[1:5])
