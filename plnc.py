#ohrsantos
from termcolor import colored, cprint
from colorama import Fore, Back, Style
from colorama import init
init(autoreset=True)

from stack import Stack
from pln_calc import PlnCalc



def assert_equal(first, second):
    if first == second:
        cprint('[OK]', 'green')
    else:
        print(Fore.RED + '[FAILE]' + Fore.RESET + '===> expected: ' + str(first) + ', but got: ' + str(second))



calc = PlnCalc()


calc.enter(7)
assert_equal([7], calc.stack.items)

calc.sum(3)
assert_equal([10], calc.stack.items)

calc.repush_last()
assert_equal([10, 10], calc.stack.items)

calc.sum('EMPTY')
assert_equal([20], calc.stack.items)

calc.repush_last()
assert_equal([20, 20], calc.stack.items)

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
