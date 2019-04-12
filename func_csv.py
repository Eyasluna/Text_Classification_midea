import csv

with open('dialogueText.csv','r',encoding='utf-8') as f1:
    reader = csv.DictReader(f1)
    column = [row['text']for row in reader]

f = open('train.txt', 'w+',encoding= 'utf-8')
for lines in column:
    f.writelines(lines+'\n')
f.close()