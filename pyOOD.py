class SchoolMember:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def get_name(self):
        print('---------------------')
        print('getting instance var name: ')
        print(self.name)
    def get_age(self):
        print('---------------------')
        print('getting instance var age: ')
        print(self.age)

class Student(SchoolMember):
    #class var ; default static class var, no need to delcare it clearly
    stu_num = 0
    def __init__(self, name, age,score, hobby):
        super().__init__(name, age)
        self.score = score
        Student.stu_num += 1 #way to get stu_num from class
        self.__hobby = hobby
    def get_score(self):
        print('---------------------')
        print('getting instance var score: ')
        print(self.score)
    #access private var
    def get_hobby(self):
        print('---------------------')
        print('getting private var: ')
        print(self.__hobby)

    @property
    def show_hobby(self):
        print('---------------------')
        print("show hobby with @property: ")  
        print(self.__hobby)
    
    @classmethod # default var for class method is cls NOT self
    def total(cls):
        print('---------------------')
        print("class student count from class method: ")
        return cls.stu_num
    
    def __private_total(self):
        print('---------------------')
        print("class student count from PRIVATE class method: ")
        print('access way: _Class__privateMethodName()')
        return Student.stu_num

    @staticmethod
    def func1():
        print('---------------------')
        print('this is static method')


if __name__ == '__main__':
    sm = SchoolMember('testName', 25)
    sm.get_age()
    sm.get_name()

    stu = Student('tom',15,89,'zuqiu')
    stu.get_age()
    stu.get_name()
    stu.get_score()
    print('---------------------')
    print('getting class var: 2ways')
    print(Student.stu_num)
    print(stu.__class__.stu_num)
    
    print(Student.total())
    stu.get_hobby()
    #print(stu.__hobby)
    #AttributeError: 'Student' object has no attribute '__hobby'
    #private attribute cannot be accessed from outside

    print(stu._Student__private_total())

    Student.func1()
    stu.show_hobby