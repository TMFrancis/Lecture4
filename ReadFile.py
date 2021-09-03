# read file

import os
path = "/Users/tomfrancis/Documents/"
os.chdir(path)

with open('test.txt') as b:
    lines = b.readlines()
    print(lines)

print(lines[0])