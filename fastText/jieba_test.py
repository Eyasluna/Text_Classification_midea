#encoding=utf-8

import jieba
seg_list = jieba.cut("迷失的人就迷失了，相遇的人还会再相遇",cut_all=True)
print ("Full Mode:", "/ ".join(seg_list)) #全模式

seg_list = jieba.cut("迷失的人就迷失了，相遇的人还会再相遇",cut_all=False)
print ("Default Mode:","/ ".join(seg_list)) #精确模式

seg_list = jieba.cut("迷失的人就迷失了，相遇的人还会再相遇") #精确模式
print ("精确模式：", ", ".join(seg_list))

seg_list = jieba.cut_for_search("迷失的人就迷失了，相遇的人还会再相遇") #搜索引擎模式
print ("搜索引擎模式：",", ".join(seg_list))

seg_list = jieba.cut("I'm sorry for everything oh everything I've done",cut_all=True)
print ("Full Mode:", "/ ".join(seg_list))
