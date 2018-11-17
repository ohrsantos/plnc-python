from stack import Stack
from pln_calc_stack import PlnCalcStack

print(__name__)


reg_stack = Stack()
reg_stack.push(4.23)
reg_stack.push(3.14)
reg_stack.push(8.14)
reg_stack.push(4.44)
reg_stack.push(5.55)

print(reg_stack.get())

input_op = float(input(': '))

reg_stack.push(reg_stack.pop() + input_op)

print(reg_stack.get())

input_op = float(input(': '))

reg_stack.push(reg_stack.pop() - input_op)

print(reg_stack.get())

reg_stack.load([4, 6, 9])

print(reg_stack.get())

a = Stack()

a.push(3.1415)
a.load([1, 2, 3])
print(reg_stack.size())
reg_stack.load(a.get())
print(reg_stack.get())
print(reg_stack.size())


plnc_stack = PlnCalcStack()
plnc_stack.load([1,2,3,4])
print(plnc_stack.get())
print(plnc_stack.size())


plnc_stack.repush_last()
print(plnc_stack.get())
print(plnc_stack.size())
print(plnc_stack._Stack__items)

#######################################
#for item in reg_stack.items:
    #print(item)
#reg_stack.repush_last()
