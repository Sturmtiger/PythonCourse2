import time

#	#1 solution
class Loggable: # в проверке определен данный класс!!!
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))

class LoggableList(list, Loggable):
    def append(self, e):
        super(LoggableList, self).append(e)
        self.log(e)


test = LoggableList()
test.append('msg 1')
test.append('msg 2')
print(test)

#	#2 solution by getattr method
# class Loggable: # в проверке определен данный класс!!!
#     def log(self, msg):
#         print(str(time.ctime()) + ": " + str(msg))
#
# class LoggableList(list, Loggable):
#     def append(self, e):
#         for f in 'append', 'log':
#             getattr(super(), f)(e)


#   #3 easy primitive solution
# class LoggableList(list, Loggable):
#     def append(self, p):
#         self += [p]
#         self.log(p)