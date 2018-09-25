#   #1 starswith
# s, t = (input() for _ in range(2))
# print(sum(s.startswith(t, i) for i in range(len(s))))


#   #2 index
s, t = [input() for _ in range(2)]
index = [None]
while True:
    if s.find(t, index[-1]) == -1:
        break
    index.append(s.find(t, index[-1]) + 1)
print(len(index) - 1) # Вычитаем None(лишний элемент)