# This is a sample Python script.
import time

import websocket

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
#


# from utils.Coroutine import averager
#
# # 协程触发
# coro_avg = averager()
# # 协程预激活
# next(coro_avg)
# # 调用者给协程提供数据
# coro_avg.send(5)
# coro_avg.send(6)
# coro_avg.send(13)
# try:
#     coro_avg.send(None)
# except StopIteration as exc:
#     result = exc.value  # 执行完成会抛出异常，返回值包含在属性value里
#
# print('Record count is {},average is {}.'.format(result.count, result.average))


# from grammar.list import *
# # read_list()
# update_list()


# from grammar.tuple import *
# update_tuple()


# from grammar.dict import *
# update_dictionary()


# from grammar.control import *
# start_while()


# a = '123'
# print('before function a is:', a)
# param_conversion(a)
# print('after function a is:', a)
#
# b = ['1', '2']
# print('before function b is:', b)
# param_conversion(b)
# print('after function b is:', b)


# default_value('123456')
# square = nth_power(2)
# cube = nth_power(3)
# print(square(2))
# print(cube(2))


# print(add(2, 3))
# print(start_special())

# from types import MethodType
# from proto.course import *
#
# software = Course('software')
# software.hello_course()
#
# # 动态新增属性
# software.level = 1
# print('add property with value', software.level)
#
#
# def info(self):
#     print('__binding function__', self)
#
#
# # 动态新增函数
# software.foo = info
# software.foo(software)
#
# # 通过lambda，动态新增函数
# software.bind_method = lambda self: print('__lambda express__', self)
# software.bind_method(software)
#
#
# def add_function_with_method_type(self):
#     print('__methodType function__', self)
#
#
# # 通过MethodType，动态新增函数
# software.add_method_type = MethodType(add_function_with_method_type, software)
# # 第一个参数已经绑定，所以可以不传
# software.add_method_type()
#
# print('\n')
# stock = Stock('stock')
# stock.hello_course()
# Stock.hello_class_method('__class method__')
# stock.hello_static_method()
# print('stock all vars:', vars(stock))

# from flask import Flask
# from flask_restful import Api
# from services.demoRequest import *
#
# app = Flask(__name__)
# api = Api(app)
#
#
# api.add_resource(TodoList, '/todos')
# # % curl http://localhost:5000/todos
# # {
# #     "todo1": {
# #         "task": "init restful api"
# #     },
# #     "todo2": {
# #         "task": "hello"
# #     },
# #     "todo3": {
# #         "task": "world"
# #     }
# # }
# # curl http://localhost:5000/todos -X POST -H 'Content-Type: application/json' -d '{"task":"have a nice day",
# # "optional_argument": 1}'
# # { "task": "have a nice day" }
# api.add_resource(Todo, '/todos/<todo_id>')
# # curl http://localhost:5000/todos/todo3
# # {
# #     "task": "world"
# # }
# if __name__ == '__main__':
#     app.run(debug=True)

# from src.utils.spark.WordCount import *
# WordCount.test_word_count()

# from grammar.concurrency import *
# import time
# import asyncio
#
# sites = ['https://en.wikipedia.org/wiki/Portal:Arts',
#          'https://en.wikipedia.org/wiki/Portal:History',
#          'https://en.wikipedia.org/wiki/Portal:Society',
#          'https://en.wikipedia.org/wiki/Portal:Biography',
#          'https://en.wikipedia.org/wiki/Portal:Mathematics',
#          'https://en.wikipedia.org/wiki/Portal:Technology',
#          'https://en.wikipedia.org/wiki/Portal:Geography',
#          'https://en.wikipedia.org/wiki/Portal:Science',
#          'https://en.wikipedia.org/wiki/Computer_science',
#          'https://en.wikipedia.org/wiki/Python_(programming_language)',
#          'https://en.wikipedia.org/wiki/Java_(programming_language)',
#          'https://en.wikipedia.org/wiki/PHP',
#          'https://en.wikipedia.org/wiki/Node.js',
#          'https://en.wikipedia.org/wiki/The_C_Programming_Language',
#          'https://en.wikipedia.org/wiki/Go_(programming_language)'
#          ]
# start_time = time.perf_counter()
# # downTask = ConcurrentFutures()
# # downTask.download_all(sites)
#
# downTask = ConcurrentAsyncio()
# asyncio.run(downTask.download_all(sites))
#
# end_time = time.perf_counter()
# print('Download {} site\n in {} seconds'.format(sites, end_time - start_time))


# from services.restTickerRequest import *
# RestTicker = RestTicker()
# RestTicker.getBtcTicker()


from services.socketTicker import *

print('hello world')
# wsRequest = SocketTicker(url="wss://api.gemini.com/v1/marketdata/btcusd?top_of_book=true&offers=true", count=2)
wsRequest = SocketTicker()
wsRequest.start()
