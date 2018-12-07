from stack import Stack

class PlnCalc():
    def __init__(self):
        self.reg_stack = Stack()
    def repush_last(self):
        self.reg_stack.push(self.reg_stack.last())
