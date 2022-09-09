
class Course(object):

    name = ''
    score = ''

    def __init__(self, name, score=0):
        self.name = name
        self.score = score

    # 如果传递参数，需要类属性关联使用，不然会报警告
    def hello_course(self):
        print('welcome to learning:', self.name)
