#   #1 try
# from datetime import date, timedelta
# output = date(*(int(i) for i in input().split())) + timedelta(int(input()))
# print(output.year, output.month, output.day)


#   #2 try
# from datetime import date, timedelta
# output = date(*map(int, input().split())) + timedelta(int(input())) #можно обходиться без lambda в map
# print(output.year, output.month, output.day)


#   #3 try
from datetime import datetime, timedelta
output = datetime.strptime(input(), '%Y %m %d') + timedelta(int(input()))
print(output.strftime('%Y %m %d').replace(' 0', ' '))

