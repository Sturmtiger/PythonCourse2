#   #1-й блин - комом
# s, a, b = [input() for _ in range(3)]
# cnt = 0
#
# while True:
#     if a in s:
#         s = s.replace(a, b)
#         cnt += 1
#
#     else:
#         print(cnt)
#         break
#
#     if cnt > 1000 or a in b:
#         print('Impossible')
#         break



#   #2 С помощью генератора
# s, a, b = [input() for _ in range(3)]
# def gen(s, a, b):
#     while a in s: s = s.replace(a, b); yield True
# print('Impossible' if a in b and a in s else sum(gen(s, a, b)))



#   #3
s, a, b, cnt = [input() for _ in range(3)] + [0]
while a in s:
    if a in b: cnt = 'Impossible'; break
    s, cnt = s.replace(a, b), cnt+1
print(cnt)