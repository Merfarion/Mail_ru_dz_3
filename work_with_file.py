import os
import re

script_dir = os.path.dirname(__file__)
path = input()
pattern = re.compile(' [a-zA-Z]{7}: [a-zA-Z]{7}:')
abs_file_path = os.path.join(script_dir, path)
result = open('result.log', 'w')
# print(abs_file_path)
if abs_file_path.find('.log') != -1:
    f = open(abs_file_path, "r")
    for line in f:
        print(line)
        if pattern.findall(line):
            result.write(line + '\n')
else:
    for file in os.listdir(abs_file_path):
        with open(os.path.join(abs_file_path, file), 'r') as f:
            for line in f:
                print(line)
                if pattern.findall(line):
                    result.write(line+'\n')