#   #(1)с функцией
# def mod_checker(x, mod=0):
#     return lambda y: y % x == mod  
#   #(2)на лямбде
mod_checker = lambda x, mod=0: lambda y: y % x == mod

# test
mod_3 = mod_checker(3)
print(mod_3(3))  # True
print(mod_3(4))  # False

mod_3_1 = mod_checker(3, 1)
print(mod_3_1(4))  # True

c = 1
b = 2