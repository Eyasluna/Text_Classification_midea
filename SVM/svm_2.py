# -*- coding: utf-8 -*-
#author: Yibo Fu @midea
#9/12/2018

import re
import itertools
from sklearn import svm
import random
import jieba
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import metrics
import numpy
import argparse
import sys

# parser = argparse.ArgumentParser()
# parser.add_argument('-i', '--input', type = str, help = "input file")
# parser.add_argument('-r', '--ratio', type = float, help = 'split ratio')
# args = parser.parse_args()

def inputdata(filename):
    f = open(filename,'r')
    linelist = f.readlines()
    return linelist

# Extract words and labels from train set and test set
# def splitset(trainset,testset):
#     train_words = []
#     train_tags = []
#     test_words = []
#     test_tags = []
#
#     for keys in trainset:
#         keys = keys.strip()
#         p1 = r"\_.*\t"
#         p2 = r"\t.*"
#         patterns1 = re.compile(p1)
#         train_tags.append(patterns1.findall(keys))
#         patterns2 = re.compile(p2)
#         train_words.append(patterns2.findall(keys))
#     train_tags = list(itertools.chain(*train_tags))
#     train_words = list(itertools.chain(*train_words))
#
#     for keys in testset:
#         keys = keys.strip()
#         p1 = r'\_.*\t'
#         p2 = r'\t.*'
#         patterns1 = re.compile(p1)
#         test_tags.append(patterns1.findall(keys))
#         patterns2 = re.compile(p2)
#         test_words.append(patterns2.findall(keys))
#     test_tags = list(itertools.chain(*test_tags))
#     test_words = list(itertools.chain(*test_words))
#
#     return train_words,train_tags,test_words,test_tags

def splitset(train_file, test_file):
    train_tags = []
    test_tags = []

    f1 = open(train_file).readlines()
    for keys in f1:
        keys = keys.strip()
        p = r'\__.*?\s'
        pattern = re.compile(p)
        train_tags.append(pattern.findall(keys))
    remove_list = set(list(itertools.chain(*train_tags)))

    train_tags = list(itertools.chain(*train_tags))
    output_file_1 = 'tem1.txt'
    content_1 = open(output_file_1, 'w+')
    for line in f1:
        for keys in remove_list:
            line = line.replace(keys, '')
        content_1.write(line)
    content_1.close()
    train_words = open('tem1.txt').readlines()

    print('train tags:', len(train_tags), 'train words:', len(train_words))
    f2 = open(test_file).readlines()
    for keys in f2:
        keys = keys.strip()
        p = r'\__.*?\s'
        pattern = re.compile(p)
        test_tags.append(pattern.findall(keys))
    remove_list2 = set(list(itertools.chain(*test_tags)))
    test_tags = list(itertools.chain(*test_tags))
    output_file_2 = 'tem2.txt'
    content_2 = open(output_file_2, 'w+')
    for line in f2:
        for keys in remove_list2:
            line = line.replace(keys, '')
        content_2.write(line)
    content_2.close()
    test_words = open('tem2.txt').readlines()

    print('test tags', len(test_tags), 'test words:', len(test_words))

    return train_words, train_tags, test_words, test_tags
comma_tokenizer = lambda x: jieba.cut(x, cut_all=True)

def tfvectorize(train_words,test_words):
    v = TfidfVectorizer(tokenizer=comma_tokenizer,binary = False,
                        decode_error = 'ignore',stop_words = 'english')
    train_data = v.fit_transform(train_words)
    test_data = v.transform(test_words)

    return train_data,test_data

#split dataset to two by split ratio
def splitDataset(dataset,splitRatio):
    trainSize = int(len(dataset)*splitRatio)
    trainSet = []
    copy = dataset
    while len(trainSet)<trainSize:
        index = random.randrange(len(copy))
        trainSet.append(copy.pop(index))

    return trainSet,copy

#get precision and recall
def evaluate(actual, pred):
    m_precision = metrics.precision_score(actual, pred,average='macro')
    m_recall = metrics.recall_score(actual,pred,average='macro')
    m_f1 = metrics.f1_score(actual,pred,average='macro')
    print ('precision:{0:.3f}'.format(m_precision))
    print ('recall:{0:0.3f}'.format(m_recall))
    print('f1 score:{0:0.3f}'.format(m_f1))

#build svm classifer
def train_clf(train_data, train_tags):
    clf = svm.SVC(C=10.0, cache_size=200, class_weight=None, coef0=0.0,
                  decision_function_shape=None, degree=3,
                  gamma='auto', kernel='rbf', max_iter=-1, probability=False,
                  random_state=None, shrinking=True,
                  tol=0.001, verbose=False)
    clf.fit(train_data, numpy.asarray(train_tags))
    return clf

def covectorize(train_words,test_words):
    v = CountVectorizer(tokenizer=comma_tokenizer,binary = False,
                        decode_error = 'ignore',stop_words = 'english')
    train_data = v.fit_transform(train_words)
    test_data = v.transform(test_words)
    return train_data,test_data

if __name__ == '__main__':
    # linelist = inputdata(args.input)
    #
    # trainset, testset = splitDataset(linelist, args.ratio)
    #
    # print ('train number:', len(trainset))
    # print ('test number:', len(testset))

    if len(sys.argv) < 3:
        print ('Input format should be: python SVM.py train_file test_file')
        sys.exit(0)
    train_file = sys.argv[1]
    test_file = sys.argv[2]

    train_words, train_tags, test_words, test_tags = splitset(train_file, test_file)
    #train_data, test_data = tfvectorize(train_words, test_words)
    train_data, test_data = covectorize(train_words, test_words)

    clf = train_clf(train_data,train_tags)

    re =  clf.predict(test_data)
    # print re
    evaluate(numpy.asarray(test_tags),re)
    # print re







