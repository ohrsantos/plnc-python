#ohrsantos
from termcolor import colored, cprint
from colorama import Fore, Back, Style
from colorama import init
init(autoreset=True)

from stack import Stack
from pln_calc import PlnCalc

import unittest


class LoadUnitTest(unittest.TestCase):
    def setUp(self):
        self.calc = PlnCalc()
        self.calc.stack.load([3,-2,-3,5])
    def runTest(self):
        self.assertEqual(self.calc.stack.items, [3, -2,-3,5])
    def tearDown(self):
        del self.calc


class SumUnitTest(unittest.TestCase):
    def setUp(self):
        self.calc = PlnCalc()
        self.calc.stack.load([3,-2,-3,5])
        self.calc.enter(7)
        self.calc.sum(3)
        self.calc.sum(-1)
        self.calc.sum(9)
        self.calc.sum('EMPTY')
        self.calc.sum('EMPTY')
        self.calc.sum('EMPTY')
    def runTest(self):
        self.assertEqual(self.calc.stack.last(), 18)
    def tearDown(self):
        del self.calc


if __name__ == '__main__':
    unittest.main()
