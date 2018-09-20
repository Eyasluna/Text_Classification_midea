import fileinput
import sys
import itertools
import re

for line in fileinput.input(['new_test.txt'],inplace=True):
     sys.stdout.write(' __label__\t{l}'.format(l=line))
