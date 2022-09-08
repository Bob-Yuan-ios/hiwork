# 函数
from typing import Callable, Any


# 参数传递
def param_conversion(s):
    s += s
    print('函数体内的值:{}'.format(s))


# 默认参数
def default_value(a1, a2='world'):
    print('参数1', a1, '参数2', a2)


# 闭包函数
def nth_power(ex):
    def ex_of(data):
        return data ** ex

    return ex_of


# 匿名函数
add: Callable[[Any, Any], Any] = lambda x, y: x + y


# 系统函数举例
def start_special():
    a = 1
    s = 2
    exec('a = s')
    print('exec:', a)
    a = exec('1 + 3')
    print('exec:', a)
    a = eval('4 + 5')
    print('eval:', a)


