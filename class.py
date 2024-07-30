class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def myfunc(self):
        print(f"hello my name is {self.name} and I'm {self.age} years old") 
p1=Person("jhon", 36)
p1.myfunc()
