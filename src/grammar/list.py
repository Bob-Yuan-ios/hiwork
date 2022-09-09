# 数组 可修改

# 字符串/元组/字典 创建数组
def create_list():
    l1 = list('helloworld')
    print('string to list:{}'.format(l1))

    t1 = ('hello', 'world')
    l2 = list(t1)
    print('tuple to list:{}'.format(l2))

    d1 = {'a': 100, 'b': 101}
    l3 = list(d1)
    print('dictionary to list:{}'.format(l3))


# 数组读操作
def read_list():
    url = list('https://www.baidu.com/happy')
    print(url[3])
    print(url[-4])
    print(url[9: 18])
    print(url[9: 18: 3])
    print(url[-6: -1])


# 数组更新操作
def update_list():
    nums = [1, 2, 3, 40, 36, 91, 91, 91, 5]

    # 元素36的索引
    print(nums.index(36))
    # 截取第4个元素之后的子数组  元素91索引 找到第一个就结束
    print(nums.index(91, 4))
    # 子数组5到7 元素91索引（左闭右开）找到第一个就结束
    print(nums.index(91, 5, 7))
    print('contain element 91 total:{}'.format(nums.count(91)))

    # 更新单个元素
    print('before update {}'.format(nums))
    nums[2] = -1001
    nums[-3] = 990
    print('after update {}'.format(nums))

    # 更新多个元素
    print('before update {}'.format(nums))
    nums[1:4] = [2, 3, 4]
    print('after update {}'.format(nums))

    # 插入元素
    print('before update {}'.format(nums))
    nums[1:1] = [1]
    print('after update {}'.format(nums))

    # 字符串数组元素替换
    s = list('hello')
    print('before update {}'.format(s))
    s[2:4] = 'ABCDEFG'
    print('after update {}'.format(s))
