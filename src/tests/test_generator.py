#!/usr/bin/env python3
import unittest
from unittest.mock import patch
from termcolor import colored
from generator import ReverseShellGenerator, ip_address
from netifaces import AF_INET
class TestReverseShellGenerator(unittest.TestCase):

    def setUp(self):
        self.generator = ReverseShellGenerator()

    @patch('builtins.print')
    @patch('reverseshellgenerator.generator.ni.ifaddresses')
    @patch('reverseshellgenerator.generator.ni.interfaces')
    def test_do_ip_interface(self, mock_interfaces, mock_ifaddresses, mock_print):
        # mock network interface and corresponding IP address
        mock_interfaces.return_value = ['eth0']
        mock_ifaddresses.return_value = {AF_INET: [{'addr': '192.168.0.1'}]}

        self.generator.do_ip('eth0')
        mock_print.assert_called_with(colored("The IP address has been set as '192.168.0.1'", 'green'))
        self.assertEqual(self.generator.ip, '192.168.0.1')

    @patch('builtins.print')
    @patch('reverseshellgenerator.generator.ni.interfaces')
    def test_do_ip_address(self, mock_interfaces, mock_print):
        # mock no network interface
        mock_interfaces.return_value = []

        self.generator.do_ip('192.168.0.1')
        mock_print.assert_called_with(colored("The IP address has been set as '192.168.0.1'", 'green'))
        self.assertEqual(self.generator.ip, '192.168.0.1')

    @patch('builtins.print')
    @patch('reverseshellgenerator.generator.ni.interfaces')
    def test_do_ip_invalid(self, mock_interfaces, mock_print):
        # mock no network interface
        mock_interfaces.return_value = []

        self.generator.do_ip('999.999.999.999')
        mock_print.assert_called_with(colored("'999.999.999.999' does not appear to be an IPv4 or IPv6 address", 'red'))
        self.assertIsNone(self.generator.ip)

    @patch('builtins.print')
    def test_do_ip_empty(self, mock_print):
        self.generator.do_ip('')
        mock_print.assert_called_with(colored('The IP address must not be empty', 'red'))
        self.assertIsNone(self.generator.ip)


if __name__ == "__main__":
    unittest.main()
