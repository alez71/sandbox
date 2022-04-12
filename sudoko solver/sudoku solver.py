from copy import deepcopy
from pprint import pprint

class Stored:
    def __init__(self) -> None:
        self.allowed = [1,2,3,4,5,6,7,8,9]
    def remove(self,value):
        self.allowed.remove(value)
    def get(self):
        print(self.allowed)
    def report(self,x):
        return int(self.allowed.count(x))
a = [[1,2,3],[3,4,5]]
b = deepcopy(a)
b.append([9,9,9])
print(a,b)