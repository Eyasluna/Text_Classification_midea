import requests
import re
import itertools

import numpy as np

def file_process(file_name):
    input_file = file_name
    f1 = open(input_file,encoding='utf8').readlines()

    remove_lines= []
    for keys in f1:
        keys = keys.strip()
        p = r'\__.*__0.*\$'
        pattern = re.compile(p)
        remove_lines.append(pattern.findall(keys))
    remove_lines = set(list(itertools.chain(*remove_lines)))

    processed_file = 'new_output.txt'
    content = open(processed_file, 'w+',encoding='utf-8')
    for line in f1:
        for keys in remove_lines:
            line = line.replace(keys,'')
        content.write(line)
    content.close()

    file1 = open('new_output.txt', 'r', encoding='utf-8') # 要去掉空行的文件
    file2 = open('new_output2.txt', 'w', encoding='utf-8') # 生成没有空行的文件
    try:
        for line in file1.readlines():
            if line == '\n':
                line = line.strip("\n")
            file2.write(line)
    finally:
        file1.close()
        file2.close()

    s = '__label__1 ^ 我 有 糯米 $'
    new_s = s[13:-2]
    print(new_s)

    output= open('processed_file.txt','w+',encoding='utf-8')
    f2 = open("new_output2.txt",encoding='utf-8').readlines()
    for line in f2:
        newline = line[13:-2]
        output.write(newline+'\n')
    output.close()
    return output



def get_tag_type(utterance_name,tag_type):
    out = {"currentUtterance": utterance_name,
           "clearDialogHistory": True,
           "userGroup": "nlp",
           "userGroupCredential": "11c19213-25ef-46d8-b863-e7603c7aa00e"}

    HEADERS = {"User-Agent": "python-requests/2.18.4", "Accept-Encoding": "gzip, deflate",
               "Accept": "*/*", "Connection": "keep-alive", "Content-Length": "86",
               "Content-Type": "application/json"}

    r = requests.post('http://10.3.225.144:8888/three_scenarios/nlp/listen/session', json=out,
                      headers=HEADERS)
    c = r.json()
    intent_type = c['intent'][tag_type]
    c.dump()
    return intent_type

#processed_file = open('processed_file.txt',encoding='utf-8').readlines()


def generate_tag_file(output_file,process_file,tag_type):
    intent = open(output_file,'w+', encoding='utf-8')
    processed_file = open(process_file, encoding='utf-8').readlines()
    for line in processed_file:
        results = get_tag_type(line,tag_type)
        intent.write(results+'\n')
        print(results)
    intent.close()
    return intent


def generate_final_file(intent_file,processed_file,output_file):
    new_intent = open(intent_file,encoding='utf-8').readlines()
    final_output = open(output_file,'w+',encoding='utf-8')
    process_file = open(processed_file, encoding='utf-8').readlines()
    for i in range(len(process_file)):
        line = process_file[i].strip() + '  ' + new_intent[i]
        final_output.write(line)
    final_output.close()
    return final_output


def remove_dup(input_file,output_file):
    lines_seen = set()  # holds lines already seen
    outfile = open(output_file, 'w+', encoding='utf-8')
    for line in open(input_file, 'r', encoding='utf-8'):
        if line not in lines_seen:  # not a duplicate
            outfile.write(line)
            lines_seen.add(line)

    outfile.close()


def combine_files(file1, file2, output_file):
    with open(file1,encoding='utf-8') as input1:
        first_input = input1.readlines()
    with open(file2,encoding= 'utf-8') as input2:
        second_input = input2.readlines()

    output = open(output_file,'w+',encoding='utf-8')
    print(type(input2))
    for i in range(len(first_input)):
        line = first_input[i]
        output.write(line)
    for k in range(len(second_input)):
        line = second_input[k]
        output.write(line)
    output.close()
    return output

def count_file_lines(file_name):
    count = -1
    for count,line in enumerate(open(file_name,'rU',encoding='utf-8')):
        pass
    count +=1
    print('file lines is:', count)
    return count

#if __name__ == '__main__':

#split file from processed file to 6400 lines, then send to get intent func.
def generate_second_pro_file(range1,range2):
    output = open('second_processed_file.txt','w+',encoding='utf-8')
    with open('processed_file.txt',encoding='utf-8') as test1:
        array = []
        for line in test1:
            array.append(line)
    for u in range(range1,range2):
        new_input = array[u]
        output.write(new_input)
    output.close()
    return output


def remove_space(file_name):
    #get all lines from file
    with open(file_name, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    # remove spaces
    lines = [line.replace(' ', '') for line in lines]
    # write lines in the file
    with open(file_name, 'w', encoding='utf-8') as f:
        f.writelines(lines)


# count_file_lines('second_processed_file.txt')
# generate_tag_file('domain.txt','processed_file.txt','domain')
# generate_final_file('domain.txt','processed_file.txt','domain_output.txt')
m = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(m[1][2])
print(m.shape)



print(get_tag_type('不知道土豆焖豆角怎么做','domain'))


#combine_files('Corpus.txt','tuneSet.txt','combined.txt')
