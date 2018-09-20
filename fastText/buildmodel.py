# _*_coding:utf-8 _*_
#author: Yibo Fu @midea
#8/12/2018

import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
import fasttext
import itertools
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-tr', '--train', type = str, help = "training file")
parser.add_argument('-te', '--test', type = str, help = "test file")
parser.add_argument('-pr', '--predict', type = str, help = 'precidct file')
parser.add_argument('-ot', '--output', type = str, help = 'output file')
args = parser.parse_args()

#training model
classifier = fasttext.supervised(args.train, "new.model", label_prefix="__label__")

#load trained model
#classifier = fasttext.load_model('news_fasttext.model.bin', label_prefix='__label__')

#test model
result = classifier.test(args.test)
print ("precision:",result.precision)
print ("recall:",result.recall)

#predict model
predict_file = open(args.predict).readlines()
labels = classifier.predict(predict_file)
data = list(itertools.chain(*labels))

with open(args.output , 'w') as label_file:
    label_file.write('\n'.join(map(str,data)))







