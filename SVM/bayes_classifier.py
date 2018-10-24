# coding: utf-8
#author: Yibo Fu @midea
#9/12/2018

import sys
import jieba
import re
import itertools
import numpy
from sklearn import metrics
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.naive_bayes import MultinomialNB

# def input_data(train_file, test_file):
#     train_words = []
#     train_tags = []
#     test_words = []
#     test_tags = []
#
#     with open(train_file, 'r') as f1:
#         for keys in f1:
#
#             keys = keys.strip()
#             #p1 = r"\_.*\t"
#             p1=r'\_.*?\s'
#             #p2 = r"\t.*"
#             p2 = r'[^a-z_1234567890?!]'
#             patterns1 = re.compile(p1)
#             train_tags.append(patterns1.findall(keys))
#             patterns2 = re.compile(p2)
#             train_words.append(patterns2.findall(keys))
#         train_tags = list(itertools.chain(*train_tags))
#         train_words = list(itertools.chain(*train_words))
#
#     with open(test_file, 'r') as f2:
#         for keys in f2:
#             keys = keys.strip()
#             #p1 = r'\_.*\t'
#             p1= r'\_.*?\s'
#             #p2 = r'\t.*'
#             p2 = r'[^a-z_1234567890?!]'
#             patterns1 = re.compile(p1)
#             test_tags.append(patterns1.findall(keys))
#             patterns2 = re.compile(p2)
#             test_words.append(patterns2.findall(keys))
#         test_tags = list(itertools.chain(*test_tags))
#         test_words = list(itertools.chain(*test_words))
#
#     return train_words, train_tags, test_words, test_tags
#

def input_data(train_file, test_file):
    train_tags= []
    test_tags= []

    f1 = open(train_file).readlines()
    for keys in f1:
        keys = keys.strip()
        p = r'\__.*?\s'
        pattern = re.compile(p)
        train_tags.append(pattern.findall(keys))
    remove_list = set(list(itertools.chain(*train_tags)))
    train_tags = list(itertools.chain(*train_tags))
    output_file_1 = 'tem1.txt'
    content_1 = open(output_file_1,'w+')
    for line in f1:
        for keys in remove_list:
            line = line.replace(keys,'')
        content_1.write(line)
    content_1.close()
    train_words = open('tem1.txt').readlines()

    print('train tags:',len(train_tags),'train words:',len(train_words))

    f2 = open(test_file).readlines()
    for keys in f2:
        keys = keys.strip()
        p = r'\__.*?\s'
        pattern = re.compile(p)
        test_tags.append(pattern.findall(keys))
    remove_list2 = set(list(itertools.chain(*test_tags)))
    test_tags = list(itertools.chain(*test_tags))
    output_file_2 = 'tem2.txt'
    content_2 = open(output_file_2,'w+')
    for line in f2:
        for keys in remove_list2:
            line = line.replace(keys, '')
        content_2.write(line)
    content_2.close()
    test_words = open('tem2.txt').readlines()

    print('test tags',len(test_tags),'test words:',len(test_words))

    return train_words, train_tags, test_words, test_tags

with open('hlt_stop_words.txt', 'r') as f:
    stopwords = set([w.strip() for w in f])

comma_tokenizer = lambda x: jieba.cut(x, cut_all=True)

def vectorize(train_words, test_words):
    v = HashingVectorizer(tokenizer=comma_tokenizer, n_features=30000, non_negative=True)
    train_data = v.fit_transform(train_words)
    test_data = v.fit_transform(test_words)
    return train_data, test_data

def evaluate(actual, pred):
    m_precision = metrics.precision_score(actual, pred, average= 'macro')
    m_recall = metrics.recall_score(actual, pred, average= 'macro')
    m_f1 = metrics.f1_score(actual,pred,average='macro')
    print ('Precision:{0:.3f}'.format(m_precision))
    print ('Recall:{0:0.3f}'.format(m_recall))
    print('f1 score:{0:.3f}'.format(m_f1))

def train_clf(train_data, train_tags):
    clf = MultinomialNB(alpha=0.01)
    clf.fit(train_data, numpy.asarray(train_tags))
    return clf

def main():
    if len(sys.argv) < 3:
        print ('Input format should be: python SVM.py train_file test_file')
        sys.exit(0)
    train_file = sys.argv[1]
    test_file = sys.argv[2]
    
    train_words, train_tags, test_words, test_tags = input_data(train_file, test_file)
    #print(test_words)
    train_data, test_data = vectorize(train_words, test_words)
    clf = train_clf(train_data, train_tags)
    predict = clf.predict(test_data)
    evaluate(numpy.asarray(test_tags), predict)

if __name__ == '__main__':
    main()
