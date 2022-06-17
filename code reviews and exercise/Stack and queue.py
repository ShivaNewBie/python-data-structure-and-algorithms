from collections import deque


class Stack():
    def __init__(self):
        self.stack = list()
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return None
    def peek(self): #peeks behind last stack
        if len(self.stack) > 0:
            return self.stack[len(self.stack)-2] #looking at index of list. #I changed this to 2 so it will look the previous last stack 
        else:
            return None
    def __str__(self):
        return str(self.stack)

my_stack = Stack()
my_stack.push(1)
my_stack.push(3)
my_stack.push(5)
my_stack.push(7)

# print(my_stack)
# print(my_stack.pop())
# print(my_stack.peek())
# print(my_stack.pop())
# print(my_stack.pop())

#Write a wrapper class for the Queue class, similar to what we did for Stack, but using Python deque.  
#Try adding enqueue, dequeue, and get_size methods.
class Queue():
    def __init__(self):
        self.queue = deque()
        self.size = 0
    def enqueue(self,item):
        self.queue.append(item)
        self.size += 1
    def dequeue(self):
        if len(self.queue) > 0: #means we have an item
            return self.queue.popleft()
        else:
            return None
    def peek(self):
        if self.size > 0:
            return self.queue[len(self.queue)-2]
    def get_size(self):
        return self.size
    def __str__(self):
        return str(self.queue)

test = Queue()
test.enqueue(5)
test.enqueue(7)
test.enqueue(6)

# test.dequeue()

print(test.get_size())
