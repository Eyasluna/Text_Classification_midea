# _*_coding:utf-8 _*_
#author: Yibo Fu @midea
#4/28/2019
import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', type = str, help = 'Input data set')
parser.add_argument('-o', '--output',type = str,  help = 'Output data set')
args = parser.parse_args()


def tokenize(Utterance):
    out = {'currentUtterance': Utterance,
           'clearDialogHistory': True,
           'userGroup': 'nlp',
           'userGroupCredential': '11c19213-25ef-46d8-b863-e7603c7aa00e'}

    HEADERS = {'User-Agent': 'python-requests/2.18.4', 'Accept-Encoding':
        'gzip, deflate',
               'Accept': '*/*', 'Connection': 'keep-alive',
               'Content-Length': '86', 'Content-Type': 'application/json'}

    r = requests.post('http://10.3.225.144:8888/three_scenarios/nlp/listen/test',
                      json=out, headers=HEADERS)
    raw = r.text
    temp = [w for w in raw.rstrip('').split('\n') if w != '']
    tokens = temp[1].split(',')
    return tokens


def tokenize_files(input_file, output_file):
    processed_file = open(input_file, encoding='utf-8').readlines()
    with open(output_file, 'w+', encoding='utf-8') as content:
        for line in processed_file:
            new_line = tokenize(line)
            new_line = ' '.join(new_line)
            content.write(new_line+'\n')
            print(new_line)

tokenize_files(args.input,args.output)

