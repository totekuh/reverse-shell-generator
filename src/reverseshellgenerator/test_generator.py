#!/usr/bin/env python3
import unittest
from unittest.mock import patch
from termcolor import colored
from generator import ReverseShellGenerator, ip_address

class TestReverseShellGenerator(unittest.TestCase):
    def setUp(self):
        self.generator = ReverseShellGenerator()

    @patch('builtins.print')
    def test_do_ip(self, mock_print):
        valid_ip = '192.168.1.1'
        self.generator.do_ip(valid_ip)
        self.assertEqual(self.generator.ip, valid_ip)
        mock_print.assert_called_with(colored(f"The IP address has been set as '{valid_ip}'", 'green'))

        invalid_ip = '999.999.999.999'
        self.generator.do_ip(invalid_ip)
        mock_print.assert_called_with(colored(f"'{invalid_ip}' does not appear to be an IPv4 or IPv6 address", 'red'))

    @patch('builtins.print')
    def test_do_port(self, mock_print):
        valid_port = '12345'
        self.generator.do_port(valid_port)
        self.assertEqual(self.generator.port, int(valid_port))
        mock_print.assert_called_with(colored(f"The port has been set as '{valid_port}'", 'green'))

        invalid_port = '70000'
        self.generator.do_port(invalid_port)
        mock_print.assert_called_with(colored("The port value must in range between 0 and 65535", 'green'))

    @patch('builtins.print')
    def test_do_shell(self, mock_print):
        valid_shell = '/bin/bash'
        self.generator.do_shell(valid_shell)
        self.assertEqual(self.generator.shell, valid_shell)
        mock_print.assert_called_with(colored(f"The shell has been set as '{valid_shell}'", 'green'))

        invalid_shell = '/invalid/shell'
        self.generator.do_shell(invalid_shell)
        mock_print.assert_called_with(colored("No such shell found. Use 'list shells' to see available ones."))

if __name__ == "__main__":
    unittest.main()
