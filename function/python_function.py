#first function
def first_function(): #----------------------------------------------> define function
    print('Hello')
    print('This is first function')
first_function() #---------------------------------------------------> calling function




#passing multiple argument in function
def add(n1,n2):
    print(n1+n2) #-----------------------------------------------------------------> Method 01
add(20.30,30)

def add(n1,n2):
    result = n1 + n2 #-------------------------------------------------------------> Method 02
    print('The sum is',result)
add(20.30,30)

def add(n1,n2):
    result = n1+n2
    return result  #-----------------------------------------------------------------> Method 03
result = add(20,30.30)
print('The sum is',result)

def add(n1,n2):
    result = n1+n2
    return result #-----------------------------------------------------------------> Method 04
number1 = 20
number2 = 30.30
result = add(number2,number1)
print('The sum is',result)

# another example
def add(a, b):
    print('sum =', a + b) #------------------------------------------------------------> Method 05

a = float(input('enter a'))
b = float(input('enter b'))
add(a, b)




#passing single argument in function
def first_function(name): #-------------------------->formal argumrnt
    print('Hello',name)
    print('This is first function')
first_function('Jack')   #--------------------------->position argument



# default argument
def default(name='Amol', age=30, number=1234567890):
    print('My name is', name)
    print('My age is', age)
    print('My number is', number)
default('Chet',25,12345)
default(age=45,number=4520,name='Vijay')  #-----------------> keyword argument
default()



def sum(a,*b): #-----------------> variable length argument
    c = a
    for i in b:
        c += i
    print(c)
sum(20,40,15,5)


def sum(*b): #-----------------> variable length argument
    c = 0
    for i in b:
        c += i
    print(c)
sum(20,40,15,5)


def person(name,**data): #-----------------> keywarded variable length argument
    print(name)
    print(data)
person('Amol',age=25,City='Pune',contact=123456)


def person(name,**data): #-----------------> keywarded variable length argument
    print(name)
    for i,j in data.items():
        print(i,j)
person('Amol',age=25,City='Pune',contact=123456)




# passing a List as an argument
def showList(lang):
    for x in lang:
        print(x)
lang = ['HTML', 'CSS', 'Boostrap', 'Python']
showList(lang)

# another example
def List1(list1):
    list1.append(20)
    list1.append(30)
    print(list1)
list1 = [10, 50, 40, 60]
List1(list1)




# Lambda function
i = lambda a: a + 5
print(i(5))

x = lambda i, j: i * j
print(x(2, 3))

z = lambda a,b,c: a * b * c
print(z(5,7,4))

x = lambda i, j: i / j
print(x(20,10))




# function example
def add_numbers(n1, n2):
    return n1 + n2
def multiply_numbers(n1, n2):
    return n1 * n2
n1 = 10
n2 = 20
result = add_numbers(n1, n2)
print('The addition of n1 and n2 is', result)
result = multiply_numbers(n1, n2)
print('The multiplication of n1 and n2 is', result)




# function example to find average marks and grade
def find_avg_marks(marks):
    total_marks = sum(marks)
    total_subject = len(marks)
    avg_marks = total_marks/ total_subject
    return avg_marks

def find_grade(avg_marks):
    if avg_marks >=80:
        grade = 'A'
    elif avg_marks >=60:
        grade = 'B'
    elif avg_marks >=50:
        grade = 'C'
    else:
        grade = 'D'
    return grade
marks = [75,80,70,80,60]
avg_marks = find_avg_marks(marks)
grade = find_grade(avg_marks)
print('The average marks are',avg_marks)
print('The grade is',grade)