# class Sturm:
#     a = 10
#     def func(self):
#         print('Hello')
# x = Sturm
# print(x)
# x.count = 43
# print(x.count)



# class Counter:
#     def __init__(self):
#         self.count = 0
# x = Counter()
# print(x.count)

#test(ex6)
# res, tempV = None, 0
# class MoneyBox:
#     def __init__(self, capacity=10):
#         self.capacity = capacity
#     def can_add(self, v):
#         global tempV, res
#         tempV = v
#         if (self.capacity - v) < 0:
#             res = False
#             return False
#         res = True
#         return True
#     def add(self, v):
#         global res
#         if res == True and tempV == v:
#             self.capacity -= v
#             res = False
#             return self.capacity
#         return self.capacity

#Solution
class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity

    def can_add(self, v):
        if (self.capacity - v) >= 0:
            return True
        else:
            return False

    def add(self, v):
        if MoneyBox.can_add(self, v) == True:
            self.capacity -= v


w = MoneyBox(20)
print(w.can_add(5))
print(w.add(5))
print(w.capacity)
print(w.add(5))
print(w.capacity)
print(w.add(5))
print(w.capacity)