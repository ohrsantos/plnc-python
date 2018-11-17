from stack import Stack

class PlnCalcStack(Stack):
    def repush_last(self):
        self._Stack__items.append(self._Stack__items[len(self._Stack__items)-1])

