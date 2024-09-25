#!/usr/bin/python3

from package_parser import *
from internals import *
from sys import argv

print(banner)
print(menu)
parser = custom_parser()
args = parser.parse_args()

try:
    f = open(args.file)
    f_content = f.read()
    json_parser(f_content)
    f.close()
except: 
    print("An error occurred while trying to open the file.")


