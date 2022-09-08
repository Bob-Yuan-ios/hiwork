# 字典
def create_dictionary():
    s1 = {'A': 1, 'B': 2, 'C': 3}
    print('create dictionary {}'.format(s1))

    s2 = {(1, 100): 'hello', 1: ['world']}
    print('create dictionary {}'.format(s2))

    course = ['a', 'b', 'c']
    s3 = dict.fromkeys(course, 100)
    print('create dictionary {}'.format(s3))


def read_dictionary():
    tup = (['one', 1], ['two', 2])
    dic1 = dict(tup)
    print('one = {}'.format(dic1['one']))
    print('three = {}'.format(dic1.get('three', 'key is not exist')))


def update_dictionary():
    dic1 = {'a': 1, 'b': 2, 'c': 3}
    print('before delete {} contain a {}'.format(dic1, ('a' in dic1)))
    del dic1['a']
    print('after delete {} contain a {}'.format(dic1, ('a' in dic1)))
    dic1['a'] = 101
    print('after add {} contain a {}'.format(dic1, ('a' in dic1)))
    dic1.update({'a': 1, 'b': 100})
    print('after update {}'.format(dic1))
    dic1.popitem()
    print('after popItem {}'.format(dic1))
    dic1.pop('b')
    print('after pop {}'.format(dic1))