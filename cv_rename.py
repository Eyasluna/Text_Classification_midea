import os
import re


# path = '/Users/tikacrota/Desktop/Midea/file_process/new_test/'
# file_name = os.listdir(path)
# file_name.sort()
#
# k = open('file3.txt','w+',encoding= 'utf-8')
# for lines in file_name:
#     k.writelines(lines+'\n')
# k.close()
#
#
# file = open('file3.txt',encoding='utf-8').readlines()
# files = [s.rstrip() for s in file]
#
#
# for old_names,lists in zip(file_name,files):
#     new_name = old_names.replace(old_names, lists)
#     os.renames(os.path.join(path,old_names),os.path.join(path,new_name))
# print('Done')


def change_name(file_name_path,ori_text, re_text):
    f = open(file_name_path, 'r',encoding='utf-8')
    alllines = f.readlines()
    f.close()
    f = open(file_name_path, 'w+',encoding='utf-8')
    for eachline in alllines:
        a = re.sub(ori_text, re_text, eachline)
        f.writelines(a)
    f.close()

def new_change_name(ori_text, new_text):
    path = '/Users/tikacrota/Desktop/Midea/file_process/new_test/'
    file_name = os.listdir(path)
    file_name.sort()
    new_line = []
    for each_line in file_name:
        new_line = re.sub(ori_text, new_text, each_line)
    for names, lines in zip(file_name,new_line):
        new_name = names.replace(names, lines)
        os.renames(os.path.join(path, names), os.path.join(path, new_name))
    print('done')

def changing_name(org_text, new_text):
    path = '/Users/tikacrota/Desktop/Midea/file_process/20190226/rns_out_MoShini_F_20190226_seg'
    file_name = os.listdir(path)
    file_name.sort()

    k = open('file3.txt', 'w+', encoding='utf-8')
    for lines in file_name:
        k.writelines(lines + '\n')
    k.close()

    change_name('file3.txt',org_text,new_text)

    file = open('file3.txt', encoding='utf-8').readlines()
    files = [s.rstrip() for s in file]

    for old_names, lists in zip(file_name, files):
        new_name = old_names.replace(old_names, lists)
        os.renames(os.path.join(path, old_names), os.path.join(path, new_name))
    print('Done')

changing_name('_你好_小美','_nihao_xiaomei')
changing_name('_开机','_kaiji')
changing_name('_关机','_guanji')
changing_name('_空调','_kongtiao')
changing_name('_空调_开机','_kongtiao_kaiji')
changing_name('_空调_关机','_kongtiao_guanji')
changing_name('_查询_状态','_chaxun_zhuangtai')
changing_name('_开启_摆风','_kaiqi_baifeng')
changing_name('_关闭_摆风','_guanbi_baifeng')
changing_name('_自动_模式','_zidong_moshi')
changing_name('_抽湿_模式','_choushi_moshi')
changing_name('_送风_模式','_songfeng_moshi')
changing_name('_制冷_模式','_zhileng_moshi')
changing_name('_17_度','_17_du')
changing_name('_18_度','_18_du')
changing_name('_19_度','_19_du')
changing_name('_20_度','_20_du')
changing_name('_21_度','_21_du')
changing_name('_22_度','_22_du')
changing_name('_23_度','_23_du')
changing_name('_24_度','_24_du')
changing_name('_25_度','_25_du')
changing_name('_26_度','_26_du')
changing_name('_27_度','_27_du')
changing_name('_28_度','_28_du')
changing_name('_29_度','_29_du')
changing_name('_30_度','_30_du')
changing_name('_自动风','_zidongfeng')
changing_name('_最大风','_zuidafeng')
changing_name('_最小风','_zuixiaofeng')
changing_name('_中等风','_zhongdengfeng')
changing_name('_增大_风速','_zengda_fengsu')
changing_name('_减小_风速','_jianxiao_fengsu')
changing_name('_开启_上下_摆风','_kaiqi_shangxia_baifeng')
changing_name('_关闭_上下_摆风','_guanbi_shangxia_baifeng')
changing_name('_开启_左右_摆风','_kaiqi_zuoyou_baifeng')
changing_name('_关闭_左右_摆风','_guanbi_zuoyou_baifeng')
changing_name('_开启_睡眠_模式','_kaiqi_shuimian_moshi')
changing_name('_关闭_睡眠_模式','_guanbi_shuimian_moshi')
changing_name('_开启_自清洁','_kaiqi_ziqingjie')
changing_name('_关闭_自清洁','_guanbi_ziqingjie')
changing_name('_制热_模式','_zhire_moshi')
changing_name('_开启_电辅热','_kaiqi_dianfure')
changing_name('_关闭_电辅热','_guanbi_dianfure')

# change_name('file2.txt','17_du','17读速度')




