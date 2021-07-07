class Employee:
    '所有员工的基类'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print
        "Total Employee %d" % Employee.empCount

    def displayEmployee(self):
        print
        "Name : ", self.name, ", Salary: ", self.salary


print("Employee.__doc__:", Employee.__doc__)
print("Employee.__name__:", Employee.__name__)
print("Employee.__module__:", Employee.__module__)
print("Employee.__bases__:", Employee.__bases__)
print("Employee.__dict__:", Employee.__dict__)

print("---------------------------------------------------------------------------------------------------------------")

def scope_test():
    def do_local():
        spam = "local spam"
        print(spam)

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"
        print(spam)

    def do_global():
        global spam
        spam = "global spam"
        print(spam)

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)

print("-----------------------------------------------------------------------------------------------------------------")

class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'

    def __init__(self):
        data = [23,25]
        self.data=data
        self.data.append(34)

xyz = MyClass()
print(xyz.f())

data = [1, 2, 3]
print(data)

print(xyz.data)

print("-----------------------------------------------------------------------------------------------------------------")

class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)
p1 = Person("John", 36)
p1.myfunc()


print("-----------------------------------------------------------------------------------------------------------------")
class Warehouse:
        purpose = 'storage'
        region = 'west'

w1 = Warehouse()
print(w1.purpose, w1.region)

w2 = Warehouse()
w2.region = 'east'
print(w2.purpose, w2.region)

print("-----------------------------------------------------------------------------------------------------------------")

class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        print(self.tricks.append(trick))

d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
d.tricks = ['roll over']
e.tricks = ['play dead']

tricks = ["roll over"]


# print(d.add_trick('roll over'))
print("----------------------------------------------------------------------------------------------------------------")

class av:
    def __init__(self, num):
        self.num = num

aavv = av
lst = []
lst.append(aavv(14))
lst.append(aavv(12))
print(str(lst[0]) + str(lst[1]))

print("-----------------------------------------------------------------------------------------------------------------")

class av:
    def __init__(self, num):
        self.num = num

lst = []
lst.append(av(14))
lst.append(av(12))
print(str(lst[0]) + str(lst[1]))

#Python3 code here creating class

print("-------------------------------------------------------------------------------------------------------------------")
class geeks:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    # creating list


list = []

# appending instances to list
list.append(geeks('Akash', 2))
list.append(geeks('Deependra', 40))
list.append(geeks('Reaper', 44))

for obj in list:
    print(obj.name, obj.roll, sep=' ')

# We can also access instances attributes
# as list[0].name, list[0].roll and so on.

print("-----------------------------------------------------------------------------------------------------------------")

# Python3 code here for creating class
class geeks:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def Sum(self):
        print(self.x + self.y)

    # creating list


list = []

# appending instances to list
list.append(geeks(2, 3))
list.append(geeks(12, 13))
list.append(geeks(22, 33))

for obj in list:
    # calling method
    obj.Sum()

# We can also access instances method
# as list[0].Sum, list[1].Sum and so on.

print("----------------------------------------------------------------------------------------------------------------")

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)

print("-----------------------------------------------------------------------------------------------------------------")
class Bag:
    data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)

y = Bag()
y.add(1)
y.addtwice(1)
print(y.data)
