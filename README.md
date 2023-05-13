# General Information

https://pypi.org/project/revshell-generator/

The Reverse Shell Generator is a CLI tool that assists in quickly generating reverse shell commands and their corresponding listener commands.

# Installation

You can either clone the repository or install the package from PyPI.

Clone the repository:

```bash
apt install python3 python3-pip
git clone https://github.com/totekuh/reverse-shell-generator
cd reverse-shell-generator
pip3 install .
python3 revshellgenerator.py -h
```

PyPI:
```bash
sudo apt install python3 python3-pip
sudo pip3 install revshell-generator
revshell-generator -h
```

# Usage

### Running the Reverse Shell Generator

```bash
$ revshell-generator
Welcome to the reverse shell generator. Type 'help' or '?' to list available commands.
```

### Setting Reverse IP Address and Port

```bash
$ python3 revshellgenerator.py
>> ip 192.168.45.19
The IP address has been set as '192.168.45.19'
>> port 4200
The port has been set as '4200'
```

Alternatively, you can provide the IP/port as script arguments to avoid prompting them later: `revshell-generator --ip 192.168.45.19 --port 4200`

### Listing Available Reverse Shell Commands

```bash
>> list reverse
```

*Note: the indexes are used while choosing the command template.*

### Listing Available Listener Commands

```bash
>> list listeners
```

### Generating Reverse Shell Commands

```bash
$ python3 revshellgenerator.py
>> get reverse 0
```

Alternatively, you can provide the IP/port as script arguments and call the get reverse command straightaway:

```bash
$ revshell-generator --ip 192.168.45.19 --port 4200
Welcome to the reverse shell generator. Type 'help' or '?' to list available commands.
>> get reverse 0
```

№№№ Generating Listener Commands

```bash
>> get listeners 10
```

For more detailed instructions and specific commands, use the 'help' command followed by the command name, such as `help list` or `help get`.
