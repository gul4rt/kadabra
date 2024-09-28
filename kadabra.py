#!/usr/bin/python3

from core.package_parser import *
from core.internals import *
from sys import argv

print(banner)
print(menu)
parser = custom_parser()
args = parser.parse_args()

try:
    f = open(args.file)
    f_content = f.read()
    data = dependencies_parser(f_content)
    f.close()
except: 
    print("An error occurred while trying to open the file.")

print("[INF] checking dependencies\n")
finds = 0

if args.output:
    try:
        f = open(args.output, 'a')
    except:
        print("An error occurred while trying to open the output file.")

for i in data.keys():
    try:
        r = check_package(i)
        if(r == False):
            print(f"[404] {i} package not found, possibly vulnerable to dependency confusion")
            finds += 1
            if args.output:
                f.write(i+'\n')
        elif(r == None):
            print("[!] error in {i} package search")
        else:
            print(f"[200] {i} package is up")
    except:
        print("[!] error")

f.close()
print(f"[INF] total finds: {finds}")
