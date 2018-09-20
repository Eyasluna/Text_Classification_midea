import re
import itertools

content = open("input_text.txt").readlines()
delete_list = []
for keys in content:
    #keys = keys.strip()
    #p= r"\s.*"  #tab
    #p= r"([a-zA-Z_]+)?\s(.*?)"   #find the pattern here
    p = r'[\s.*\s]'
    patterns =re.compile(p)
    #delete_list1= re.search(patterns,keys)
    delete_list.append(patterns.findall(keys))

new_delete = set(list(itertools.chain(*delete_list)))

print(new_delete)

output = 'new_test.txt'
fout = open(output,"w+")
for line in content:
    for keys in new_delete:
        line = line.replace(keys,'')
    fout.write(line)
fout.close()
