#ohrsantos
from termcolor import colored, cprint
from colorama import Fore, Back, Style
from colorama import init
init(autoreset=True)

from stack import Stack
from pln_calc import PlnCalc

import unittest


class TestPlncCalc(unittest.TestCase):

    calc = PlnCalc()
    def test_enter(self):
        self.calc.enter(7)
        self.assertEqual([7], self.calc.stack.items)
        self.assertEqual(7, self.calc.stack.last())
    def test_repush_last(self):
        self.calc.repush_last()
        self.assertEqual([7, 7], self.calc.stack.items)
        self.assertEqual(7, self.calc.stack.last())
    def test_sum(self):
        self.calc.sum(3)
        self.assertEqual(10, self.calc.stack.last())
    def test_empty_sum(self):
        self.calc.sum('EMPTY')
        self.assertEqual(17, self.calc.stack.last())

    #def tearDown(self):
        #del self.calc


if __name__ == '__main__':
    unittest.main()
