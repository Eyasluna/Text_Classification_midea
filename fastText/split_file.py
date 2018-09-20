# _*_coding:utf-8 _*_
#author: Yibo Fu @midea
#8/7/2018

import random
import argparse

newdata = []
parser = argparse.ArgumentParser(description = "Get train data for fasttext")
parser.add_argument('-o', '--raw', type = str, help = 'Input the raw data set')
parser.add_argument('-t', '--train',type = str,  help = 'Output train data set')
parser.add_argument('-s', '--test', type = str, help = 'Output test data set')
parser.add_argument('-r', '--rate', type = float, default = 0.7, help = 'Input the raw/test rate')
args = parser.parse_args()
# if args.raw is None or args.train is None or args.test is None:
#     parser.print_help()
#     exit(0)

with open(args.raw, 'r') as unpro_file:
    for line in unpro_file:
        line = line.strip()
        newdata.append(line)

random.shuffle(newdata)
newtrain_size = int(len(newdata) * float(args.rate))

with open(args.train ,'w') as newtrain_file:
    for traindata in newdata[: newtrain_size]:
        newtrain_file.write(traindata)
        newtrain_file.write('\n')

with open(args.test, 'w') as  newtest_file:
    for testdata in newdata[newtrain_size:]:
        newtest_file.write(testdata)
        newtest_file.write('\n')








