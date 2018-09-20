#coding=utf-8
#author: Yibo Fu @midea
#8/12/2018

import random
from sklearn.model_selection import KFold
import numpy as np
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
import fasttext
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', type = str, help = "training file")
args = parser.parse_args()

new_data = []
data= []
counter = 1
Total_precision = 0
Total_recall = 0
# input_file = '/Users/tikacrota/desktop/Midea/fastText/all_qa_qustions_original.txt'

#Input raw training data
with open(args.file) as raw_data:
    for line in raw_data:
        line = line.strip()
        new_data.append(line)
#new_data = open('/Users/tikacrota/desktop/Midea/fastText/1000test.txt','r').readlines()
new_data = np.array(new_data)

KFOLD = KFold(10, True, 1)  #Import KFold by 10 flods

random.shuffle(new_data)

for train_set, test_set in KFOLD.split(new_data):
    print('train data set:',counter)
    with open("train_data_" + str(counter), 'w') as training_files:
        for i in train_set:
            training_files.write(new_data[i] + '\n')
    print('test data set:',counter)
    with open("test_data_"+ str(counter), 'w') as test_files:
        for i in test_set:
            test_files.write(new_data[i]+'\n')
    print()

    #Training model using fastText
    classifier = fasttext.supervised("train_data_"+ str(counter), "train_data_"+
                                     str(counter)+".model", label_prefix="__label__")
    result = classifier.test('test_data_'+ str(counter))

    #Get training results
    print(result.precision)
    print(result.recall)
    print("---------------------------------------")

    #Get total precison and recall for all training results.
    Total_precision = result.precision + Total_precision
    Total_recall = result.recall + Total_recall
    
    counter += 1

print("Average precision:",Total_precision/10)
print("Average recall:", Total_recall/10)


















