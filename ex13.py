#   #1
# class NonPositiveError(Exception): pass
# class PositiveList(list):
#   def append(self, x):
#     if x > 0:
#       getattr(super(PositiveList, self), 'append')(x)
#     else:
#       raise NonPositiveError


#   #2
# class NonPositiveError(Exception): pass
# class PositiveList(list):
#   def append(self, x):
#     if x > 0:
#       super(PositiveList, self).append(x)
#     else:
#       raise NonPositiveError


#   #3
# class NonPositiveError(Exception): pass
# class PositiveList(list):
#   def append(self, x):
#     if x > 0:
#       self.extend([x])
#     else:
#       raise NonPositiveError


#   #4 the Best solution
class NonPositiveError(Exception): pass
class PositiveList(list):
    def append(self, x):
        if x <= 0:
            raise NonPositiveError
        self.extend([x])