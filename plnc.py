#ohrsantos
from termcolor import colored, cprint
from colorama import Fore, Back, Style
from colorama import init
init(autoreset=True)

from stack import Stack
from pln_calc import PlnCalc

print(__name__)




calc = PlnCalc()
calc.stack.load([1,2,3,4])
calc.stack.push(3)
print(calc.stack.get())
print(calc.stack.size())


calc.repush_last()
print(calc.stack.get())
print(calc.stack.size())
print("\033[38;5;1mThis is a text!\033[0m")

print(colored('hello', 'red'), colored('world', 'green'))
cprint('Hello, World!', 'green', 'on_red')

print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Fore.BLUE + Back.WHITE + 'Orlando')
print('back to normal now')
