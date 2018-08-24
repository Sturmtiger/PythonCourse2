import itertools
#Функция-генератор primes. Выводит в генератор только простые числа(которые делятся на 1 и на себя).
#   #1 Первый блин комом
# def primes():
#     i = 2
#     while True:
#         cnt = -2
#         for divisor in range(1, i+1):
#             if i % divisor == 0:
#                 cnt += 1
#             if cnt > 0:
#                 break
#         if not cnt:
#             yield i
#         i += 1
#
# print(list(itertools.takewhile(lambda x: x <= 31, primes())))


#   #2 С помощью теоремы Вильсона без импорта факториала

def primes():
    i, f = 2, 1
    while True:
        if (f+1) % i == 0:
            yield i
        i, f = i + 1, f * i

print(list(itertools.takewhile(lambda x: x <= 31, primes())))
