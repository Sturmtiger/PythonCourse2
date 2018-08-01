import sys
sys.stdin = open('dataset\\ex12.txt')

#   #1 без рекурсивных функций. Минусы решения: память может заниматься повторяющимися элементами в списке
# errorInheritance, passedErrs = dict(), list()
# for inh in [input().split() for _ in range(int(input()))]:
#     errorInheritance[inh[0]] = inh[2:]
#     for i in inh[2:]: #в данном задании родители определены, этот пункт необязателен
#         if i not in errorInheritance: #в данном задании родители определены, этот пункт необязателен
#             errorInheritance[i] = [] #в данном задании родители определены, этот пункт необязателен
# for k, v in errorInheritance.items():
#     for i in v:
#         if i in errorInheritance: #в данном задании данный усл. оператор не нужнен, т.к. родители потомков определены
#             errorInheritance[k].extend(errorInheritance[i])
#
# for errorQuery in [input() for _ in range(int(input()))]:
#     if errorQuery not in passedErrs:
#         passedErrs.append(errorQuery)
#         if any(i in passedErrs for i in errorInheritance[errorQuery]):
#             print(errorQuery)


#   #1(2) лаконичный вариант, ровно под задание
errorInheritance, passedErrs = dict(), list()
for inh in [input().split() for _ in range(int(input()))]:
    errorInheritance[inh[0]] = inh[2:]
for k, v in errorInheritance.items():
    for i in v:
        errorInheritance[k].extend(errorInheritance[i])
for errorQuery in [input() for _ in range(int(input()))]:
    if errorQuery not in passedErrs:
        passedErrs.append(errorQuery)
        if any(i in passedErrs for i in errorInheritance[errorQuery]):
            print(errorQuery)


#   #2
# errorInheritance, passedErrs = dict(), list()
# def findUnnecessary(error):
#     for i in errorInheritance[error]:
#         data.add(i)
#         findUnnecessary(i)
#
# for inh in [input().split() for _ in range(int(input()))]:
#     errorInheritance[inh[0]] = inh[2:]
# for inh in errorInheritance:
#     data = set()
#     findUnnecessary(inh)
#     errorInheritance[inh] = data
#
# for errorQuery in [input() for _ in range(int(input()))]:
#     if errorQuery not in passedErrs:
#         passedErrs.append(errorQuery)
#         if any(parent in passedErrs for parent in errorInheritance[errorQuery]):
#             print(errorQuery)





#   #2(2) Вариант 2-го с errorInheritanceModified, сокращает кол-во итераций(пример в dataset/ex12.txt)
# errorInheritance, errorInheritanceModified, passedErrs = dict(), dict(), list()
# def findUnnecessary(error):
#     for i in errorInheritance[error]:
#         data.add(i)
#         findUnnecessary(i)
#
# for inh in [input().split() for _ in range(int(input()))]:
#     errorInheritance[inh[0]] = inh[2:]
# for inh in errorInheritance:
#     data = set()
#     findUnnecessary(inh)
#     errorInheritanceModified[inh] = data
#
# for errorQuery in [input() for _ in range(int(input()))]:
#     if errorQuery not in passedErrs:
#         passedErrs.append(errorQuery)
#         if any(parent in passedErrs for parent in errorInheritanceModified[errorQuery]):
#             print(errorQuery)


