# 循环控制
import sys


def start_if():
    age = int(input('input you age:'))

    if age < 6:
        print('primary education for under 6')
        sys.exit()
    else:
        print('can primary')

    print('primary successful...')


def start_while():
    url = 'https://www.baidu.com'
    i = 0
    while i < len(url):
        print('{}'.format(url[i]), end=' ')     # 使用format不会换行
        i = i + 1
    print('\ncomplete while')


def start_for():
    url = 'https://www.baidu.com'
    for a in url:
        print(a, end='')    # 使用format会换行


