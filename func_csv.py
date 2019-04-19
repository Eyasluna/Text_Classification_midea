#coding=utf-8
#author: Yibo Fu @midea
#4/15/2019

import csv
import re
import itertools


def csv_process(input_file,row_name,output_file):
    with open(input_file,'r',encoding='utf-8') as f1:
        reader = csv.DictReader(f1)
        column = [row[row_name]for row in reader]

    f = open(output_file, 'w+',encoding= 'utf-8')
    for lines in column:
        f.writelines(lines+'\n')
    f.close()


def get_remove_pattens(file_name):
    input_file = file_name
    f1 = open(input_file, encoding='utf8').readlines()

    remove_lines = []
    for keys in f1:
        keys = keys.strip()
        p = r'\s\s'
        pattern = re.compile(p)
        remove_lines.append(pattern.findall(keys))
    remove_lines = set(list(itertools.chain(*remove_lines)))

    with open(file_name, 'w+', encoding='utf-8') as w1:
        for line in f1:
            for keys in remove_lines:
                line = line.replace(keys, '')
                line = line.strip()
                w1.write(line + '\n')

def file_process(file_name):
    f1= open(file_name,'r',encoding='utf-8').readlines()
    f2= open(file_name,'w+',encoding='utf-8')
    for lines in f1:
        if len(lines) > 14:
            f2.write(lines.lstrip())

#csv_process('dialogueText_301.csv','text','result3.txt')
file_process('result.txt')

print(len('roger that :)'))
