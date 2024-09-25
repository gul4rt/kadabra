import argparse

version = "1.1"
banner = """
  _             _       _
 | | ____ _  __| | __ _| |__  _ __ __ _
 | |/ / _` |/ _` |/ _` | '_ \| '__/ _` |
 |   < (_| | (_| | (_| | |_) | | | (_| |
 |_|\_\__,_|\__,_|\__,_|_.__/|_|  \__,_|

"""

menu = f"""
Dependency confusion checker
[i] version: {version}

options:
    -h, --help: show this help message
    -f, --file string: read content from a package.json file
    -o, --output string: output file to write found issues

example:
    $ kadabra.py -f package.json 
"""

def custom_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", required=True)
    parser.add_argument("-o", "--output")
    return parser
