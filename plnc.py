#ohrsantos
from termcolor import colored, cprint
from colorama import Fore, Back, Style
from colorama import init
init(autoreset=True)

from stack import Stack
from pln_calc import PlnCalc

print(__name__)




calc = PlnCalc()
print("===>> ", calc.stack.get(),  "   ", calc.stack.size())
calc.enter(7)
print("===>> ", calc.stack.get(),  "   ", calc.stack.size())
calc.sum(3)
calc.repush_last()
print("===>> ", calc.stack.get(),  "   ", calc.stack.size())
calc.sum('EMPTY')
print("===>> ", calc.stack.get(),  "   ", calc.stack.size())

exit()

















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
