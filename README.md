# Kadabra

<div align="center">
  <img src="docs/kadabra.png" alt="Kadabra" width="200">
</div>


Kadabra is a tool developed to check for dependency confusion vulnerabilities in JavaScript projects (NPM).

As a Bug Hunter, you can use Kadabra when you find exposed package.json files in applications.
## Download and install

```
# Download
$ git clone https://github.com/gul4rt/kadabra.git && cd kadabra/
# Install dependencies
$ pip3 install -r requirements.txt
```
## Usage
```
# showing options
$ python3 kadabra.py --help
  _             _       _
 | | ____ _  __| | __ _| |__  _ __ __ _
 | |/ / _` |/ _` |/ _` | '_ \| '__/ _` |
 |   < (_| | (_| | (_| | |_) | | | (_| |
 |_|\_\__,_|\__,_|\__,_|_.__/|_|  \__,_|



Dependency confusion checker
[i] version: 1.1

options:
    -h, --help: show this help message
    -f, --file string: read content from a package.json file
    -o, --output string: output file to write found issues

example:
    $ kadabra.py -f package.json 

usage: kadabra.py [-h] -f FILE [-o OUTPUT]

options:
  -h, --help            show this help message and exit
  -f FILE, --file FILE
  -o OUTPUT, --output OUTPUT
```

```
# parsing a package.json file
$ python3 kadabra.py -f package.json
  _             _       _
 | | ____ _  __| | __ _| |__  _ __ __ _
 | |/ / _` |/ _` |/ _` | '_ \| '__/ _` |
 |   < (_| | (_| | (_| | |_) | | | (_| |
 |_|\_\__,_|\__,_|\__,_|_.__/|_|  \__,_|



Dependency confusion checker
[i] version: 1.1

options:
    -h, --help: show this help message
    -f, --file string: read content from a package.json file
    -o, --output string: output file to write found issues

example:
    $ kadabra.py -f package.json 

[INF] checking dependencies

[200] bootstrap package is up
[200] jquery package is up
[200] popper.js package is up
[404] xpto-inn package not found, possibly vulnerable to dependency confusion
[INF] total finds: 1

```
