from stack import Stack
from pln_calc import PlnCalc

print(__name__)




calc = PlnCalc()
calc.reg_stack.load([1,2,3,4])
calc.reg_stack.push(3)
print(calc.reg_stack.get())
print(calc.reg_stack.size())


calc.repush_last()
print(calc.reg_stack.get())
print(calc.reg_stack.size())
