import re
import itertools
import os

def file_process(file_name):

    input_file = file_name
    f1 = open(input_file,encoding='utf8').readlines()

    remove_lines= []
    for keys in f1:
        keys = keys.strip()
        p = r'\-.'
        pattern = re.compile(p)
        remove_lines.append(pattern.findall(keys))
    remove_lines = set(list(itertools.chain(*remove_lines)))

    with open(file_name, 'w+',encoding='utf-8') as w1:
        for line in f1:
            for keys in remove_lines:
                line = line.replace(keys,'')
                line = line.strip()
                w1.write(line+'\n')

def add_name(file_path):
    file_names = os.listdir(file_path)
    newlist = []
    for name in file_names:
        newlist.append(file_path+name)
    return newlist


print(add_name('/Users/tikacrota/Desktop/Midea/Text_Classification_midea/english/'))
for files in add_name('/Users/tikacrota/Desktop/Midea/Text_Classification_midea/english/'):
    file_process(files)
    print("Done")




