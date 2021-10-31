# import os
# script_dir = os.path.dirname(__file__)
# path = "Test_Mail\log.log"
# abs_file_path = os.path.join(script_dir, path)
# print(abs_file_path)
# f = open(abs_file_path, "r")
# print(f.read())
from pathlib import Path
import os
import re
script_dir = os.path.dirname(__file__)
path = input()
abs_file_path = os.path.join(script_dir, path)
print(abs_file_path)
if (abs_file_path.find('.log')!=-1):
    f = open(abs_file_path, "r")
    print(f.read())
else:
    for file in os.listdir(abs_file_path):
        print(file)
        with open(os.path.join(abs_file_path, file),'r') as f:
            print(f.read())