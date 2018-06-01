    #1 try
# class Buffer:
#     def __init__(self):
#         self.lst = []
#
#     def add(self, *a):
#         for i in a:
#             self.lst.append(i)
#         while len(self.lst) >= 5:
#             print(sum(self.lst[0:5]))
#             del self.lst[0:5]
#
#     def get_current_part(self):
#         return self.lst



    #2 try
#class Buffer:
#    def __init__(self):
#        self.lst = []
#
#    def add(self, *a):
#        self.lst += a # 1 итерация куда быстрее, чем цикл, который добавляет поэлементно(1 элемент - 1 итерация)
#        while len(self.lst) >= 5:
#            print(sum(self.lst[0:5]))
#            del self.lst[0:5]
#
#    def get_current_part(self):
#        return self.lst



	#Solution
class Buffer:
    def __init__(self):
        self.lst = []

    def add(self, *a):
        self.lst.extend(a) # 1 итерация куда быстрее, чем цикл, который добавляет поэлементно(1 элемент - 1 итерация)
        while len(self.lst) >= 5:
            print(sum(self.lst[0:5]))
            del self.lst[0:5]

    def get_current_part(self):
        return self.lst

a = Buffer()
a.add(1, 43, 56, 34, 65, 34, 2)
print(a.get_current_part())