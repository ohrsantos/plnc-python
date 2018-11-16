class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def repush_last(self):
         self.items.append(self.items[len(self.items)-1])

     def pop(self):
         return self.items.pop()

     def last(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)


reg_stack = Stack()
reg_stack.push(4.23)
reg_stack.push(3.14)
reg_stack.push(8.14)
reg_stack.push(4.44)
reg_stack.push(5.55)

print(reg_stack.items)

input_op = float(input(': '))

reg_stack.push(reg_stack.pop() + input_op)

print(reg_stack.items)

input_op = float(input(': '))

reg_stack.push(reg_stack.pop() - input_op)

print(reg_stack.items)






#######################################
#for item in reg_stack.items:
    #print(item)
#reg_stack.repush_last()
