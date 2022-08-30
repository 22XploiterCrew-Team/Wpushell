<p align="center"><img src="https://images2.imgbox.com/2d/10/ZxF6PUYs_o.jpg" /></p>

<p align="center">
   <img src="https://img.shields.io/badge/Python-3.10.6-blue?style=flat-square"/>
   <img src="https://img.shields.io/badge/aiohttp-3.8.1-red?style=flat-square"/>
</p>

> Automatically upload WordPress backdoor shell

## About Wpushell

Wpushell is a tool used to upload a backdoor shell to a site that uses a WordPress Content Management System with a simple and fast process.
Built using the Python programming language and can only be run on the command line terminal.
<br/>
This tool has advantages which include:

- Fast process.
- Execution of more than one target.
- Easy to use.

Using the asyncronus method, makes this tool run quite well.

## Installation

The first thing to be prepared is, of course, your computer must have ***python and pip*** installed.
<br>
There are several ways of installation:
#### Manual Installation
1. Clone or [download] (https://github.com/22XploiterCrew-Team/Wpushell) repository.
```sh
git clone https://github.com/22XploiterCrew-Team/Wpushell.git
```

2. Perform the installation of the required dependencies which have been written in the `requirements.txt` file.
```sh
pip3 install -r requirements.txt
```

#### As the package
Or you can clone/download repo and install it from the directory to use as a Python package.

1. Use the `setup.py` file for installation.
```sh
python3 setup.py install
```
2. Or in a simpler way.
```sh
pip3 install .
```

## Usage

```sh
python3 -m wpushell <target_file> [options]
```

or in a simpler way, If you have installed this tool as a module, you can simply run it easily like this:

```sh
wpushell <target_file> [options]
```

you can also run this tool not as a module by calling the ***run.py*** file, it's very simple man.

```sh
./run <target_file> [options]
```

<details>
<summary>Target</summary>
<br/>

Simple to use by adding one argument to fetch/read files from the target site:
```sh
wpushell sites.txt
```

Or combine tool with other through input/output pipelining:
```sh
cat randsx/22xploitercrew/wordpress-sites.txt | wpushell -fstdin
```

#### Target text format (IMPORTANT)

To be able to upload your backdoor shell, you must first have managed to find the ***username and password (credentials)*** used to login to the target site.
<br/>
In order for the program to read the target you have specified, the expected format should be like this:
```txt
https://target1.com/ -> [username::password]
https://target2.com/ -> [username2::password2]
```

So the `->` character is the separator between the site and the credentials, the credentials are wrapped in square brackets and separated using the `::` character.
Maybe this is a bit complicated, but this is the only way that comes to my mind :D.
</details>

<details>
<summary>Proxy</summary>
<br/>

This tool is supported by a proxy that can be used to make HTTP requests, simply do it like this:
```sh
wpushell sites.txt -x socks5://127.0.0.1:1337
```

This tool expects a proxy of type ***socks5***, so I hope you do what it says.
<br/>
You can search for proxies through the websites of free proxy providers such as https://spys.one/en/socks-proxy-list/.
</details>

## Program encountered an error

If you find any errors in this tool, we hope you can help us by contributing to make this tool even better than before, or you can create a [new issue](https://github.com/22XploiterCrew-Team/Wpushell/issues/new/choose) to describe the program errors you find.

## License

The Wpushell is opened-source tool licensed under the [MIT license](https://opensource.org/licenses/MIT).
