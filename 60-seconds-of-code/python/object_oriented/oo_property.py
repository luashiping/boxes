class Student(object):

    def __init__(self, score=0):
        self._score = score

    @property
    def score(self):
        return self._score

    '''
    我们也不一定要使用score.setter这个装饰器，这时score就变成一个只读属性了
    '''
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s = Student()
print(s.score)
s.score = 100
print(s.score)
s.score = 101
print(s.score)
