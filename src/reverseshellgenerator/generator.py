#!/usr/bin/env python3
from cmd import Cmd
import os
from termcolor import colored
import netifaces as ni

import sys


module_path = os.path.dirname(__file__)
sys.path.append(module_path)

from shells_templates import bind_shell_commands, reverse_shell_commands, msf_venom_commands, listener_commands




shells = ['sh',
          '/bin/sh',
          'bash',
          '/bin/bash',
          'cmd',
          'powershell',
          'pwsh',
          'ash',
          'bsh',
          'csh',
          'ksh',
          'zsh',
          'pdksh',
          'tcsh']

from ipaddress import ip_address


class ReverseShellGenerator(Cmd):
    intro: str = colored("Welcome to the reverse shell generator. Type 'help' or '?' to list available commands.", 'yellow')
    prompt: str = colored(">> ", 'yellow')
    ip: str = None
    port: int = None
    shell: str = '/bin/sh'

    REVERSE = 'reverse'
    LISTENERS = 'listeners'
    SHELLS = 'shells'
    MSFVENOM = 'msfvenom'
    list_actions = [REVERSE, LISTENERS, SHELLS, MSFVENOM]
    get_actions = [REVERSE, LISTENERS, MSFVENOM]

    def cmdloop(self, intro=None):
        try:
            super().cmdloop(intro=intro)
        except KeyboardInterrupt:
            print("\nExiting...")
            return

    def do_ip(self, ip: str):
        if ip:
            try:
                if ip in ni.interfaces():  # check if interface exists
                    self.ip = ni.ifaddresses(ip)[ni.AF_INET][0]['addr']  # take it's ip
                else:
                    ip_address(ip)
                    self.ip = ip
            except Exception as e:
                print(colored(f"{e}", 'red'))
                return
            print(colored(f"The IP address has been set as '{self.ip}'", 'green'))
        else:
            print(colored('The IP address must not be empty', 'red'))

    def do_port(self, port: str):
        if port:
            try:
                port = int(port)
            except Exception:
                print(colored('The port value must be an integer', 'red'))
                return
            if port <= 0 or port > 65535:
                print(colored("The port value must in range between 0 and 65535", 'green'))
                return
            self.port = port
            print(colored(f"The port has been set as '{self.port}'", 'green'))
        else:
            print(colored('The port value must not be empty', 'red'))

    def do_shell(self, shell):
        if shell:
            if shell not in shells:
                print(colored("No such shell found. Use 'list shells' to see available ones."))
                return
            self.shell = shell
            print(colored(f"The shell has been set as '{self.shell}'", 'green'))
        else:
            print(colored('The shell name must not be empty', 'red'))

    def do_list(self, item: str):
        if not item:
            print(colored("You must give something to list first. "
                          "Use 'help list' to see available items.",
                          "red"))
            return
        if item not in self.list_actions:
            print(colored(f"'{item}' is not a valid item to list,"
                          f" use one of {self.list_actions} instead", 'red'))
        else:
            if item == self.REVERSE:
                for i, reverse in enumerate(reverse_shell_commands):
                    meta = colored(f"[{' | '.join(reverse['meta'])}]", 'red')
                    print(colored(f"{i} - {reverse['name']} {meta}", 'yellow'))
            elif item == self.LISTENERS:
                for i, listener in enumerate(listener_commands):
                    print(colored(f"{i} - {listener['name']}", 'yellow'))
            elif item == self.SHELLS:
                for i, shell in enumerate(shells):
                    print(colored(f"{i} - {shell}", 'yellow'))
            elif item == self.MSFVENOM:
                for i, venom in enumerate(msf_venom_commands):
                    print(colored(f"{i} - {venom['name']}", 'yellow'))

    def do_get(self, command: str):
        if not self.ip:
            print(colored("The IP address must be set before generating the command. "
                          "Use 'ip <ip_address>' or `ip <iface_name>` to set it.", "red"))
            return
        if not self.port:
            print(colored("The port must be set before generating the command. "
                          "Use 'port <port>' for setting it.", "red"))
            return
        invalid_item_message = os.linesep.join([colored('Invalid command. It needs to be as follows:', 'red'),
                                                colored(f'get [ {" | ".join(self.list_actions)} ] [index]', 'yellow'),
                                                '',
                                                colored(f"E.g.: get reverse 0", 'yellow')])
        if ' ' not in command:
            print(invalid_item_message)
            return
        chunks = command.split(' ')
        if len(chunks) != 2:
            print(invalid_item_message)
            return
        else:
            item = chunks[0]
            if item not in self.list_actions:
                print(invalid_item_message)
                return
            try:
                index = int(chunks[1])
            except Exception:
                print(invalid_item_message)
                return
            template = self.get_command_by_index(item, index)
            if template:
                generated_command = self.generate_command(template)
                print(generated_command)

    def generate_command(self, template: str):
        return template.replace("{ip}", self.ip) \
            .replace("{port}", f"{self.port}") \
            .replace("{shell}", self.shell)

    def get_command_by_index(self, item: str, index: int):
        no_such_index_error_message = colored(f"There is no such {item} with index {index}", 'red')

        def get_item_from_list(items_list: list, attribute: str, index: int):
            try:
                command = items_list[index]
                return command[attribute]
            except IndexError:
                print(no_such_index_error_message)
                return

        if item == self.REVERSE:
            return get_item_from_list(reverse_shell_commands, 'command', index)
        elif item == self.LISTENERS:
            return get_item_from_list(listener_commands, 'command', index)
        elif item == self.SHELLS:
            return get_item_from_list(shells, 'command', index)
        elif item == self.MSFVENOM:
            return get_item_from_list(msf_venom_commands, 'command', index)

    def help_ip(self):
        print(colored(os.linesep.join(['ip [ip_address]',
                                       'Use the given IP address as the reverse or bind shell IP address',
                                       ]), 'yellow'))

    def help_port(self):
        print(colored(os.linesep.join(['port [port]',
                                       'Use the given port as the reverse or bind port',
                                       ]), 'yellow'))

    def help_shell(self):
        print(colored(os.linesep.join([f'shell [ {" | ".join(shells)} ]',
                                       'Set the desired shell to be used in the generated reverse shell command. ',
                                       'E.g.: shell /bin/bash',
                                       "The '/bin/sh' shell is the default one.",
                                       ]), 'yellow'))

    def help_list(self):
        print(colored(os.linesep.join([f'list [ {" | ".join(self.list_actions)} ]',
                                       'List the available templates, shells or listener commands. ',
                                       'E.g.: list shells',
                                       ]), 'yellow'))

    def help_get(self):
        print(colored(os.linesep.join([f'get [ {" | ".join(self.get_actions)} ] [index]',
                                       'Generate the actual command with the given options. ',
                                       '',
                                       "The first parameter specifies which type of the command it's going to be.",
                                       "The [index] parameter specifies which template should be used for generating "
                                       "the command. ",
                                       "E.g.: get reverse 0",
                                       '',
                                       "Use 'list' command for getting the index."
                                       ]), 'yellow'))


def get_arguments():
    from argparse import ArgumentParser
    parser = ArgumentParser(description="Reverse Shell Generator Script")
    parser.add_argument('--ip',
                        dest='ip',
                        required=False,
                        type=str,
                        help="Specify the IP address or the interface name to put into the chosen command template. "
                             "If omitted, the script requires you to interactively prompt it.")

    parser.add_argument('--port',
                        dest='port',
                        required=False,
                        type=int,
                        help="Specify the port to put into the chosen command template. "
                             "If omitted, the script requires you to interactively prompt it.")
    parser.add_argument('--shell',
                        dest='shell',
                        required=False,
                        default='/bin/sh',
                        type=str,
                        help="Specify which shell interpreter should be put into the generated command. "
                             "If omitted, can be changed interactively. "
                             f"Default is '/bin/sh'.")
    options = parser.parse_args()
    return options


def main():
    options = get_arguments()
    generator = ReverseShellGenerator()
    if options.ip:
        generator.do_ip(ip=options.ip)
    generator.port = options.port
    generator.shell = options.shell

    generator.cmdloop()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(os.linesep)
        print('Bye')
