#-*- coding: UTF-8 -*-
# coding=<encoding name>
import re
import itertools

newmodels = []
lines = open("/Users/tikacrota/desktop/qa__ac_displaying_errorcode.txt").readlines()

print ("lines is :",lines)

for keys in lines:
    p2 = r"\S+?\|"
    patterns= re.compile(p2)
    #newkeys = re.search(patterns,keys)
    newmodels.append(patterns.findall(keys))

structed_keys = list(itertools.chain(*newmodels))
newTest = set(structed_keys)

print (newTest)

final_error_set = set()

for error in structed_keys:
    code = error.replace('|', '')
    final_error_set.add(code)

print ("newmodels:", newmodels)
print ("structed keys:", structed_keys)
print ("final error code set:", final_error_set)
print ("numbers of error codes in total:", len(final_error_set))
