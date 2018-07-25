import sys
sys.stdin = open('dataset\\ex8.txt', 'r') # набор данных(авто ввод)



#   #1(громоздкий код, но работает на все случаи наследования)
#
# def isParent(parent, descendant):
#     if inheritance[descendant] is None:
#         return 'No'
#     if parent in inheritance[descendant]:
#         return 'Yes'
#     for i in range(len(inheritance[descendant])):
#
#         if inheritance[descendant][i] in tempPar:
#             break
#         tempPar.append(inheritance[descendant][i])
#
#         if isParent(parent, inheritance[descendant][i]) == 'Yes':
#             return 'Yes'
#     return 'No'
#
# inheritance = dict()
# for _ in range(int(input())):
#     classInh = input().split()
#     if classInh[0] not in classInh[2:]:
#         if len(classInh) == 1:
#             inheritance[classInh[0]] = None
#         else:
#             inheritance[classInh[0]] = classInh[2:]
#             for j in range(2, len(classInh)):
#                 if classInh[j] not in inheritance:
#                     inheritance[classInh[j]] = None
#
# query = list()
# [query.append(input().split()) for _ in range(int(input()))]
#
# for parent, descendant in query:
#     if parent == descendant:
#         print('Yes')
#     elif (parent not in inheritance) or (descendant not in inheritance):
#         print('No')
#     else:
#         tempPar = list()
#         print(isParent(parent, descendant))



#   #2(красивое лаконичное решение, работает только по условиям задачи)
#
# def isParent(parent, descendant):
#     return parent == descendant or any(map(lambda x: isParent(parent, x), inheritahce[descendant]))
# inheritahce = dict()
# for i in [input().split() for _ in range(int(input()))]:
#     inheritahce[i[0]] = i[2:]
# print(inheritahce)
# for j in [input().split() for _ in range(int(input()))]:
#     print(j)
#     print(['No', 'Yes'][isParent(j[0], j[1])])


#	#3 Без рекурсии. Работает во всех случаях

inheritance = dict()
for i in [input().split() for _ in range(int(input()))]:
    inheritance[i[0]] = i[2:]
for k, v in inheritance.items():
    for i in v:
        if i in inheritance:
            inheritance[k].extend(inheritance[i])
for parent, inheritor in [input().split() for _ in range(int(input()))]:
    # print('Yes' if parent == inheritor or parent in inheritance[inheritor] else 'No') #1 variant of output
    print(['No', 'Yes'][parent == inheritor or parent in inheritance[inheritor]]) #2 variant of output