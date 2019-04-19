#coding=utf-8
#author: Yibo Fu @midea
#4/12/2019

import re
import itertools
import os

def file_process(file_name):
    input_file = file_name
    f1 = open(input_file,encoding='utf8').readlines()

    f2 = open(file_name, 'w+', encoding='utf-8')

    for line in f1:
        newline = line[4:]
        f2.write(newline )
    f2.close()


def add_name(file_path):
    names = os.listdir(file_path)
    new_list = []
    for name in names:
        new_list.append(file_path+name)
    return new_list

def combine_files(file_path):
    file_names = os.listdir(file_path)
    print(file_names)
    f = open('result.txt','w+', encoding='utf-8')
    for files in add_name(file_path):
        for lines in open(files):
            f.writelines(lines)
    f.close()



print('name:', add_name('/Users/tikacrota/Desktop/Midea/Text_Classification_midea/english/'))
# for files in add_name('/Users/tikacrota/Desktop/Midea/Text_Classification_midea/english/'):
#     file_process(files)
#     print("Done")
#
combine_files('/Users/tikacrota/Desktop/Midea/Text_Classification_midea/english/')

