from stack import Stack

class PlnCalc():
   def __init__(self):
       self.stack = Stack()
       self.input_register = 0.0
   def repush_last(self):
       self.stack.push(self.stack.last())
   def enter(self, value):
       if value != 0.0:
          self.stack.push(value) 
       else:
          repush_last()
   def sum(self, value):
       if type(value) == str:
          self.stack.push(self.stack.pop() +  self.stack.pop())
       else:
          self.stack.push(value + self.stack.pop())
        
