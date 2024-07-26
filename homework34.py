# def log_errors(func):
#
#     def decorator(a, b, oper):
#         try:
#             return func(a, b, oper)
#         except:
#             msg = 'Функция {} выдала ошибку с параметрами: a={}, b={}, oper={}'.format(func.__name__, a, b, oper)
#             print(msg)
#
#         return None
#
#     return decorator
#
# @log_errors
# def calculate(a: int, b: int, oper: str):
#
#     expression = '{} {} {}'.format(a, oper, b)
#     res = eval(expression)
#     return res
#
# r = calculate(1, 2, '+')
# print(r)
#
# r = calculate(1, None, '+')
# print(r)
#
#
#
#
#
#
#
#
#
#
#
#
# from time import time, sleep
#
# def measure_time(func):
#
#     def decorator(*args, **kwargs):
#         t1 = time()
#         func()
#         t2 = time()
#         delta = t2 - t1
#         return delta
#     return decorator
#
#
# def f1():
#     """ Функция 1 """
#     sleep(.5)
#     return 'f1 result'
#
#
# def f2():
#     """ Функция 2 """
#     sleep(.5)
#     return 'f2 result'
#
# def f3():
#     """ Функция 3 """
#     sleep(1)
#     return 'f3 result'
#
# # декорируем функции, чтобы в результате они вычисляли время работы функции
# f1_decorated = measure_time(f1)
# f2_decorated = measure_time(f2)
# f3_decorated = measure_time(f3)
#
# # узнаём время работы функции
# time_of_f1 = f1_decorated()
# time_of_f2 = f2_decorated()
# time_of_f3 = f3_decorated()
#
# # выводим полученные данные
# print('Время работы f1:', round(time_of_f1, 2))
# print('Время работы f2:', round(time_of_f2, 2))
# print('Время работы f3:', round(time_of_f3, 2))