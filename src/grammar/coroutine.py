# 协程 同一线程内
from collections import namedtuple
Result = namedtuple('Result', 'count average')


# 协程函数
def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield None   # 暂停， 等待主程序传入数据唤醒
        if term is None:
            break           # 决定是否退出
        total += term
        count += 1
        average = total/count   # 累计状态，包括上一次状态
    return Result(count, average)
