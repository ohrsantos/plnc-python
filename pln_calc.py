from stack import Stack

class PlnCalc():
    def __init__(self):
        self.stack = Stack()
    def repush_last(self):
        self.stack.push(self.stack.last())
