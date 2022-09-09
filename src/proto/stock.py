from .course import *


class Stock(Course):
    @classmethod
    def hello_class_method(cls, name):
        print('__current is calling class method__', name)

    @staticmethod
    def hello_static_method():
        print('__current is calling static method__')
