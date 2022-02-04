class Firstclass:
    a = 10
    b = 20
print(Firstclass)

class Firstclass:
    a = 10
    b = 20
f1 = Firstclass()
f2 = Firstclass()
print('The value of a is ',f1.b)
print('The value of b is ',f1.b)
print()
print('The value of a is ',f2.b)
print('The value of b is ',f2.b)





class User:
    def __init__(self, name):
        self.name = name
u1 = User('Amol')
u2 = User('Vijay')
print('The name is', u1.name)
print('The name is', u2.name)





class User:
    def __init__(self, name='Vijay', age=20, contact=123):
        self.name = name
        self.age = age
        self.contact = contact
u = User('Amol', 25, 123456)
user = User()
print('The name is', u.name)
print('The age is', u.age)
print('The contact is', u.contact)
print()
print('The name is', user.name)
print('The age is', user.age)
print('The contact is', user.contact)


class Method:
    def method1(self):
        print('This is method 1')

    def method2(self):
        print('This is method 2')
m = Method()
m.method1()
m.method2()


class Method:
    def __init__(self, name, email, city):
        self.name = name
        self.email = email
        self.city = city

    def method1(demo):
        print('The name is', demo.name)
        print('The email is', demo.email)
        print('The city is', demo.city)

m = Method('Amol', 'amol@gmail.com', 'Pune')
m.method1()


class Method:
    def __init__(self, name, email, city):
        self.name = name
        self.email = email
        self.city = city

    def method1(demo):
        print('The name is', demo.name)
        print('The email is', demo.email)
        print('The city is', demo.city)

m = Method('Amol', 'amol@gmail.com', 'Pune')
m.name = 'Vijay'                                  #change name
m.method1()


class Student:
    def check_pass_fail(self, name, marks):
        self.name = name
        self.marks = marks
        if self.marks >= 50:
            return True
        else:
            return False
student1 = Student()
student2 = Student()
print(student1.check_pass_fail('Mak', 50))
print(student2.check_pass_fail('John', 48))
