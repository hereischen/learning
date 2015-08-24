# -*- coding: utf-8 -*-
from datetime import date


# def log(func):
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#     return wrapper


# def newlog(text):
#     def decorator(func):
#         def wrapper(*args, **kw):
#             print('%s %s():' % (text, func.__name__))
#             return func(*args, **kw)
#         return wrapper
#     return decorator


# @log
# def now():
#     print date.today()


if __name__ == '__main__':
    now()
    print now.__name__
