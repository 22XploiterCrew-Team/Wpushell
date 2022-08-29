<h1 align="center">Wpushell</h1>

<p align="center">
<img src="https://img.shields.io/badge/Python-3.10.6-blue?style=flat-square"/>
<img src="https://img.shields.io/badge/aiohttp-3.8.1-red?style=flat-square"/>
</p>

<p align="center">
<img src="https://images2.imgbox.com/95/f8/qSh6N1up_o.jpg"/>

Wpushell is a tool used to upload a backdoor shell to a site that uses a WordPress Content Management System with a simple and fast process.
</p>

## Installation
Make sure you have Python3 and pip installed.

### Manually
1. Clone or [download] (https://github.com/22XploiterCrew-Team/Wpushell.git) repository
```sh
git clone https://github.com/22XploiterCrew-Team/Wpushell.git
```

2. Install dependencies
```sh
pip3 install -r requirements.txt
```

### As the package
You can clone/download repo and install it from the directory to use as a Python package.
```sh
pip3 install .
```
#### or
```sh
python3 setup.py install
```

## Features
- Fast process
- Execution of more than one target
- Easy to use

## Usage
In order to use it to upload your backdoor shell, you must first have managed to find the username and password (credentials) used to login to the target site. the input from your target list should be in this format:
https://target.com/ -> [username::password]

```sh
python3 -m wpushell <target_file> [options]
```

### or simply

```sh
wpushell <target_file> [options]
```

### or locally without installing

```sh
./run.py <target_file> [options]
```
