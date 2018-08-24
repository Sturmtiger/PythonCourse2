#   #1 способ. Решение через _next. В next_нужно подавать уже перебранный список. В самом_next__перебирать список нельзя
#Ибо возникнут проблемы. Если значение не прошло условие - все равно автоматически вернется пустой return, добавив None
#в элементы, которые в конечном итоге вернет __iter__
# class multifilter:
#     def judge_half(pos, neg):
#         return pos >= neg
#
#     def judge_any(pos, neg):
#         return pos >= 1
#
#     def judge_all(pos, neg):
#         return neg == 0
#
#     def __init__(self, iterable, *funcs, judge=judge_any):
#         self.iterable = iterable
#         self.wentOverIterable = list()
#         i = 0
#         self.funcs = funcs
#         self.judge = judge
#
#         for i in range(len(self.iterable)):
#             pos, neg = 0, 0
#             for f in self.funcs:
#                 if f(self.iterable[i]):
#                     pos += 1
#                 else:
#                     neg += 1
#             if self.judge(pos, neg):
#                 self.wentOverIterable.append(self.iterable[i])
#
#     def __next__(self):
#         if self.i < len(self.wentOverIterable):
#             self.i += 1
#             return self.wentOverIterable[self.i - 1]
#         raise StopIteration
#
#     def __iter__(self):
#         return self
#
#
# def mul2(x):
#     return x % 2 == 0
# def mul3(x):
#     return x % 3 == 0
# def mul5(x):
#     return x % 5 == 0
#
# a = [i for i in range(31)] # [0, 1, 2, ... , 30]
# print(list(multifilter(a, mul2, mul3, mul5)))
# # [0, 2, 3, 4, 5, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30]
# print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half)))
# # [0, 6, 10, 12, 15, 18, 20, 24, 30]
# print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_all)))
# # [0, 30]





#   #2 способ. Решил без __next__ , генерируя набор элементов в самом __iter__
class multifilter:
    judge_half = lambda f: sum(f) >= len(f) / 2

    judge_any = lambda f: any(f)

    judge_all = lambda f: all(f)

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.iterable = iterable
        self.funcs = funcs
        self.judge = judge

    def __iter__(self):
        return (i for i in self.iterable if self.judge([f(i) for f in self.funcs]))


def mul2(x):
    return x % 2 == 0
def mul3(x):
    return x % 3 == 0
def mul5(x):
    return x % 5 == 0

a = [i for i in range(31)] # [0, 1, 2, ... , 30]
print(list(multifilter(a, mul2, mul3, mul5)))
# [0, 2, 3, 4, 5, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30]
print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half)))
# [0, 6, 10, 12, 15, 18, 20, 24, 30]
print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_all)))
# [0, 30]





#   # 3 способ с применением yield
# class multifilter:
#     def judge_half(pos, neg):
#         return pos >= neg
#
#     def judge_any(pos, neg):
#         return pos >= 1
#
#     def judge_all(pos, neg):
#         return neg == 0
#
#     def __init__(self, iterable, *funcs, judge=judge_any):
#         self.iterable = iterable
#         self.funcs = funcs
#         self.judge = judge
#
#     def __iter__(self):
#         for i in self.iterable:
#             pos, neg = 0, 0
#             for f in self.funcs:
#                 if f(i):
#                     pos += 1
#                 else:
#                     neg += 1
#             if self.judge(pos, neg):
#                 yield i
#
#
# def mul2(x):
#     return x % 2 == 0
# def mul3(x):
#     return x % 3 == 0
# def mul5(x):
#     return x % 5 == 0
#
# a = [i for i in range(31)] # [0, 1, 2, ... , 30]
# print(list(multifilter(a, mul2, mul3, mul5)))
# # [0, 2, 3, 4, 5, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30]
# print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half)))
# # [0, 6, 10, 12, 15, 18, 20, 24, 30]
# print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_all)))
# # [0, 30]