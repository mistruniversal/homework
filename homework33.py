# class Singleton:
#     _instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if not cls._instance:
#             cls._instance = super(Singleton, cls).__new__(cls)
#         return cls._instance
#
# if __name__ == "__main__":
#     singleton1 = Singleton()
#     singleton2 = Singleton()
#
#     print(singleton1 is singleton2)







# class animal:
#     def what_you_say(self):
#         return 'не знаю что написать'
# class dog(animal):
#     def speak(self):
#         return 'gaw'
# class cat(animal):
#     def speak(self):
#         return 'mau'
# class factory:
#     def score(self,w):
#         if w=='cat':
#             return cat()
#         elif w=='dog':
#             return dog()
#         else:
#             print(animal.what_you_say())
#
# if __name__ == '__main__':
#     catordog=input('cat or dog')
#     id1=factory()
#     print(id1.score(catordog).speak())





# c 3 не разобрался
