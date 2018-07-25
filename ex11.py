#Exception hierarchy
#https://docs.python.org/3/library/exceptions.html#exception-hierarchy

def foo(a, b):
    print(a/b)


#   #functional variant
try:
    foo(5, 0) #test
except Exception as e:
    if e.__class__.__name__ in ('FloatingPointError', 'OverflowError'):
        print(e.__class__.__base__.__name__)
    else:
        print(e.__class__.__name__)

#   #easy variant
# try:
#     foo()
# except ZeroDivisionError:
#     print('ZeroDivisionError')
# except ArithmeticError:
#     print('ArithmeticError')
# except AssertionError:
#     print('AssertionError')

