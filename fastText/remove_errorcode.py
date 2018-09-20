import re
import itertools

content = open("/Users/tikacrota/desktop/all_data_expanded1.txt").readlines()
delete_list = []
for keys in content:
    p= r"\|<.*?>"
    patterns =re.compile(p)
    #delete_list1= re.search(patterns,keys)
    delete_list.append(patterns.findall(keys))

new_delete = list(itertools.chain(*delete_list))
    #content = content.replace(str(newkeys), '')

print(new_delete)
# with open('test1.txt', 'w') as fpw:
#     fpw.write(content)


output = '/Users/tikacrota/desktop/all_data_expanded.txt'
fout = open(output,"w+")
for line in content:
    for keys in new_delete:
        line = line.replace(keys,'')
    fout.write(line)
fout.close()




