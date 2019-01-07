#ohrsantos
from termcolor import colored, cprint
from colorama import Fore, Back, Style
from colorama import init
init(autoreset=True)

from stack import Stack
from pln_calc import PlnCalc

from unittest import TestCase


calc = PlnCalc()

class TestPlncCalc(TestCase):

    #def setUp(self):

    def test_enter(self):
        calc.enter(7)
        self.assertEqual([7], calc.stack.items)
        self.assertEqual(7, calc.stack.last())
    def test_sum(self):
        calc.sum(3)
        self.assertEqual([10], calc.stack.items)
        self.assertEqual(10, calc.stack.last())
    def test_repush_last(self):
        calc.repush_last()
        self.assertEqual([10, 10], calc.stack.items)
        #self.assertEqual(10, calc.stack.last())
    #def test_empty_sum(self):
        #calc.sum('EMPTY')
        #self.assertEqual([20], calc.stack.items)
        #self.assertEqual(20, calc.stack.last())

    #def tearDown(self):
        #del self.calc


if __name__ == '__main__':
    unittest.main()
