#     #1
#objects = [1, 2, 3, 3, 3, 'Hello', {'4'}, 0]
# ans = set()
# for obj in objects:
#     ans.add(id(obj))
# print(len(ans))


#   #2
# objects = [1, 2, 3, 3, 3, 'Hello', {'4'}, 0]
# print(len(set(map(id, objects))))


#   #solution
# objects = [1, 2, 3, 3, 3, 'Hello', {'4'}, 0]
# exec('print(len(set(map(id, objects))))')