import json

def json_parser(content):
    parsed_file = json.loads(content)
    print(parsed_file)
