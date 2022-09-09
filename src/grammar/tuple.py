# 元组 不可修改
# 创建
def create_tuple():
    nums = (1, 2, 3, 4, 5)
    print('meta tuple {}'.format(nums))

    tup1 = tuple('hello')
    print('string to tuple {}'.format(tup1))

    list1 = ['1', '2', '3']
    tup2 = tuple(list1)
    print('list to tuple {}'.format(tup2))

    dic1 = {'a': '100', 'b': -1}
    tup3 = tuple(dic1)
    print('dict to tuple {}'.format(tup3))

    range1 = range(-1, 9)
    tup4 = tuple(range1)
    print('range to tuple {}'.format(tup4))


# 读
def read_tuple():
    url = tuple("http://c.biancheng.net/shell/")
    print('正向第一个元素:{}'.format(url[1]))
    print('反向第一个元素:{}'.format(url[-1]))

    print('9 - 18的内容:{}'.format(url[9: 18]))
    print('9 - 18且步长为3的内容:{}'.format(url[9: 18: 3]))
    print('-6 - -1且步长为3的内容:{}'.format(url[-6: -1: 2]))


# 写
def update_tuple():
    tup = (1, 2, 3, 4)
    print('before update {} {}'.format(tup, id(tup)))
    tup = ('hello', 'world')
    print('after update {} {}'.format(tup, id(tup)))
