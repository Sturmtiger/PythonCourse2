from random import random

    #ИТЕРАТОРЫ
#Итератор - класс, генератор - функция
# lst = [54, 23, 20, 54]
# #---
# for i in lst:
#     print(i)
# #---
# x = iter(lst) # цикл while примерно представляет более глубоко, как работает цикл for
# while True: #
#     try:
#         i = next(x)
#         print(i)
#     except StopIteration:
#         break
###
#(1)
# class RandomIteration:
#     def __init__(self, k):
#         self.k = k
#         self.i = 0
#     def __next__(self):
#         if self.i < self.k:
#             self.i += 1
#             return random()
#         else:
#             raise StopIteration
#
# x = RandomIteration(2)
# print(next(x))
# print(next(x))
# print(next(x)) # raise, превышено кол-во итераций

###
#(2)
# class RandomIteration:
#     def __iter__(self):
#         return self
#     def __init__(self, k):
#         self.k = k
#         self.i = 0
#     def __next__(self):
#         if self.i < self.k:
#             self.i += 1
#             return random()
#         else:
#             raise StopIteration
#
# x = RandomIteration(5)
# print(list(iter(x))) # можем видеть список элементов итератора
# print(list(iter(x))) # также можно заметить, что задействовав все элементы даже просто вызвав функцию iter - они удаляется из списка итератора
#                      # так же и при работе с циклом, при каждой итерации из списка удаляется по элементу
# #запустим цикл для проверки
# for i in RandomIteration(4): # пример работы с циклом
#     print(i)

###
#(3)
#   #Создание итератора, который будет выводить элементы через цикл попарно
# class DoubleListElementIterator:
#     def __init__(self, lst):
#         self.lst = lst
#         self.i = 0
#     def __next__(self):
#         if self.i < len(self.lst):
#             self.i += 2
#             return self.lst[self.i - 2], self.lst[self.i - 1]
#         else:
#             raise StopIteration
#
# class MyList(list):
#     def __iter__(self):
#         return DoubleListElementIterator(self)
#
# for i in MyList([23, 54, 642, 245]):
#     print(i)

# #способ перебора с помощью метода __getitem__
# class indexIterable:
#     def __init__(self, k):
#         self.kek = k
#     def __getitem__(self, index):
#         return self.kek[index]
#
# for i in indexIterable('string'):
#     print(i)

###
        #ГЕНЕРАТОРЫ
#Генератор используется для написания итератора. Генератор создается с помощью 'def', итератор же с помощью 'class'
#В итераторе нужно обязательно объявлять функции __iter__, __next__
# (4) - функция генератора random_iterator по функционалу тождественна классу RandomIteration (2), она намного компактнее
# def random_iterator(k):
#     for i in range(k):
#         yield random() # используется в генераторе
#
# gen = random_iterator(3) # итератор
#
# for i in gen:
#     print(i)

###
# def simple_gen():
#     print('Checkpoint 1')
#     yield 1
#     print('Checkpoint 2')
#     # return 'Comment' # станет причиной StopIteration, и при наличии данных в return - они будут выведены в StopIteration
#     yield 2
#     print('Checkpoint 3')
#
# gen = simple_gen()
# x = next(gen) #next работает при условии начилия yield, когда yield заканчивается - работа прекращается с ошибкой StopIteration
# print(x)
# y = next(gen)
# print(y)
# z = next(gen) #StopIteration, т.к. yield 3 не определен
