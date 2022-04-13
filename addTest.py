
from random import uniform

class StudentClass():
    '''
    学生类：主要包含，年龄，成绩，姓名，性别属性和考试，打印成绩单方法
    '''

    def __init__(self,name,sex,age,score = None):
        '''
        类的初始化方法
        '''
        self.name = name  # 绑定name属性
        self.sex = sex    # 绑定sex属性
        self.age = age
        self.score = score

    def test(self):
        score = uniform(0,100)
        print(score)
        self.score =score

    def printer(self):
        print('''
        -----------------------------
        name:%s
        sex:%s
        age:%d
        sore:%f
        -----------------------------
        '''%(self.name,self.sex,self.age,self.score))

if __name__ == '__main__':
    stu1 = StudentClass('lpl','男',17)
    stu1.test()
    stu1.printer()





