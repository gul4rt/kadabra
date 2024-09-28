import json
import requests

def dependencies_parser(content):
    parsed_file = json.loads(content)
    dependencies = parsed_file["dependencies"]
    return dependencies 

def check_package(package):
    url = f"https://registry.npmjs.org/{package}"
    response = requests.get(url)
    if response.status_code == 200:
        return True
    elif response.status_code == 404:
        return False
    else:
        return None
