class Stack:
    def __init__(self):
        self.__items = []

    def isEmpty(self):
        return self.__items == []

    def push(self, item):
        self.__items.append(item)

    def repush_last(self):
        self.__items.append(self.__items[len(self.__items)-1])

    def pop(self):
        return self.__items.pop()

    def last(self):
        return self.__items[len(self.__items)-1]

    def size(self):
        return len(self.__items)

    def load(self, iterable):
        for item in iterable:
            self.__items.append(item)

    def get(self):
        return [self.__items]
