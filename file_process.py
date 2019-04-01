# -*- coding: utf-8 -*-

import os
import re


# def file_name(file_dir):
#     for root, dirs, files in os.walk(file_dir):
#         #print(root)  # 当前目录路径
#         #print(dirs)  # 当前路径下所有子目录
#         print(files)  # 当前路径下所有非目录子文件

list = [
          '_nihao_xiaomei',
          '_kaiji',
          '_kongtiao_guanji',
          '_guanji',
          '_kongtiao_kaiji',
          '_chaxun_zhuangtai',
          '_kaiqi_baifeng',
          '_guanbi_baifeng',
          '_zidong_moshi',
          '_choushi_moshi',
          '_songfeng_moshi',
          '_zhileng_moshi',
          '_17_du',
          '_18_du',
          '_19_du',
          '_20_du',
          '_21_du',
          '_22_du',
          '_23_du',
          '_24_du',
          '_25_du',
          '_26_du',
          '_27_du',
          '_28_du',
          '_29_du',
          '_30_du',
          '_zidongfeng',
          '_zuidafeng',
          '_zuixiaofeng',
          '_zhongdengfeng',
          '_zengda_fengsu',
          '_jianxiao_fengsu',
          '_kaiqi_shangxia_baifeng',
          '_guanbi_shangxia_baifeng',
          '_kaiqi_zuoyou_baifeng',
          '_guanbi_zuoyou_baifeng',
          '_kaiqi_shuimian_moshi',
          '_guanbi_shuimian_moshi',
          '_kaiqi_ziqingjie'
          '_guanbi_ziqingjie'
          "_zhire_moshi",
          '_kaiqi_dianfure',
          '_guanbi_dianfure'
          ]

list2 = ['rns_out_autoTest_Selected3_0035_26_du.wav',
'rns_out_autoTest_Selected3_0036_27_du.wav',
'rns_out_autoTest_Selected3_0037_28_du.wav',
'rns_out_autoTest_Selected3_0038_29_du.wav']

path = \
    '/Users/tikacrota/Desktop/Midea/file_process/new_test/'
file_name = os.listdir(path)


file = open('file2.txt',encoding='utf-8').readlines()
files = [s.rstrip() for s in file]
# for name, ele in zip(file_name, list_2):
#     new_name = name.replace(name , name[:-4] + ele+'.wav')
#     print(new_name)
#     os.renames(os.path.join(path,name),os.path.join(path,new_name))
#



for names,lists in zip(file_name,files):
    new_name = names.replace(names, lists)
    os.renames(os.path.join(path,names),os.path.join(path,new_name))
print('Done')

def change_name(file_name_path,ori_text, re_text):
    f = open(file_name_path, 'r',encoding='utf-8')
    alllines = f.readlines()
    f.close()
    f = open(file_name_path, 'w+',encoding='utf-8')
    for eachline in alllines:
        a = re.sub(ori_text, re_text, eachline)
        f.writelines(a)
    f.close()


# path = '/Users/tikacrota/Desktop/Midea/file_process/new_test/'
# file_name = os.listdir(path)
# n=1
# for file in file_name:
#     os.renames(os.path.join(path,file),os.path.join(path,str(n)+'cccp'))
#     n = n+1

# change_name('file2.txt')
