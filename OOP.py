"""
"""
class MyBook:
    # name = "Ignited Minds"

    def __init__(self, name):
        self.name = name

# book1 = MyBook("Ignited Minds")
# print(book1.name)

class Polygon:
    def __init__(self, sides):
        self.sides = sides
    def area(self, length):
        return length * length

class Square(Polygon):
    def __init__(self, sides): # will totally overwite the parent one
        super().__init__(sides)    # inherate from parent, without it, sqr.sides will error
        # self.perimeter = perimeter

class Triangle(Polygon):
    def area(self, height, base):
        return 0.5 * height * base

sqr = Square(4)
tri = Triangle(3)
print(sqr.area(10))
print(tri.area(5, 6))

print(sqr.sides)
print(sqr.perimeter)

# to print the instance of which class
print(isinstance(sqr, Polygon))
print(isinstance(sqr, Triangle))
print(isinstance(sqr, Square))
# is the 1st class is inhereted from the 2nd
print(issubclass(Square, Polygon))
print(issubclass(Square, Triangle))
print(issubclass(Square, Square))

"""
"""
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Dancer:
    def __init__(self, style):
        self.style = style

# 1. Not correct
class Stdudent1(Human, Dancer): # multi inhereted
    pass
# John = Stdudent1("John", 48, "Hip-Hop") # Error: will only read the 1st Class by default

# 2. Correct
class Stdudent2(Human, Dancer):
    def __init__(self, name, age, style):
        Human.__init__(self, name, age) # pass self as an instance
        Dancer.__init__(self, style)
# John = Stdudent2("John", 48, "Hip-Hop")
# print(John.name)
# print(John.age)
# print(John.style)

"""
"""
class Book:
    def __init__(self, price):
        self.price = price

    # override the default add function
    def __add__(self, other):
        return self.price + other.price

    def __lt__(self, other):
        return self.price < other.price

# book1 = Book(10)
# book2 = Book(20)
# total_price = book1.price + book2.price
# # the same as:
# total_price = int.__add__(book1.price, book2.price)
# print(total_price)

# # the following should return error, but since we overloade the operator, it can be ok
# total_price = book1 + book2
# print(total_price)
# lessthen = book1 < book2
# print(lessthen)

"""
"""
class Payment1:
    def __init__(self, price):
        self.payment = price + 0.5 * price

# pay = Payment1(12)
# print(pay.payment)

# # Some bad guy may do:
# pay.payment = 0
# print(pay.payment)

# encapsulation and private
class Payment2:
    def __init__(self, price):
        self._payment = price + 0.5 * price  # single under score warns private
        self.__final = price + 0.05 * price  # double under score restrict private

    # geter can get private variabel
    def get_final(self):
        return self.__final
    # setter can set private variabel
    def set_final(self, discount):
        self.__final = self.__final - self.__calculate_discount(discount)

    # private method, now no one can change the formula
    def __calculate_discount(self, discount):
        return self.__final * (discount / 100)

# pay = Payment2(12)
# print(pay._payment)

# pay.__final = 0      # no err, but won't influence get_final()
# # print(pay.__final) # error, can not be seen
# print(pay.get_final())

# pay.set_final(10)
# print(pay.get_final())

# # NOTE: python only has global, public and private, nothing else

"""
"""
class Language:
    def say_hello(self):
        raise NotImplementedError("Please use say_hello class in child class.")

class French(Language):
    def say_hello(self):
        print("Bonjour")

class Chinese(Language):
    def say_hello(self):
        print("你好")

class Japanese(Language):
    pass

def intro(lang):        # can pass in an instance
    lang.say_hello()

# Atom = French()
# Sheldon = Chinese()
# Lizi = Japanese()
# intro(Atom)
# intro(Sheldon)
# intro(Lizi)

"""
"""

# nested function
def operation(opt_type):
    def add(n1, n2):
        return n1 + n2
    def sub(n1, n2):
        return n1 - n2

    if opt_type == 'add':
        return add  # no brackets means return without calling
    else:
        return sub

addition = operation("add")
print(addition)  # just return inner function add without execution
print(addition(1, 2)) # execute inner function
substract= operation("sub")
print(substract(12, 3))

# decorator
def decorator(func):
    def dummy(*args): # single start means no matter how many arguments are
        print("before")
        func(*args)
        print("after")
    return dummy

# an easy way to under stand decorator
def operation(text1, text2):
    print(text1, text2)
# NOTE: try to comment or uncomment and check the result
operation = decorator(operation)  # add() is the decorator
operation("hello", "world")       # execute, print "before" "Hello" "after"

# in python way
@decorator
def operation(text): # the arguments number can change, because we use a star in inner function in decorator
    print("Hello", text)
operation("there")


# the power of decorator
def addition(func):
    def dummy(*args):
        total = 0
        for a in args:
            total = total + a
        return func("addition", total)
    return dummy

def multiply(func):
    def dummy(*args):
        total = 1
        for a in args:
            total = total * a
        return func("multiply", total)
    return dummy

@addition
def operation(operation, result):
    return f'{operation} gives result as {str(result)}'

print(operation(1, 2, 3, 4))

@multiply
def operation(operation, result):
    return f'{operation} gives result as {str(result)}'

print(operation(1, 2, 3, 4))


"""
"""

class Payment:
    def __init__(self, method):
        self.__method = method

    def get_method(self):
        return self.__method

pay = Payment("paypal")
print(pay.get_method())  # how can user use .method instead of .get_method()

# property decorator
METHODS = ['paypal', 'stripe']
class PaymentX:
    def __init__(self, method):
        self.__method = method

    @property
    def method(self):
        return self.__method

    @method.setter
    def method(self, mthd):
        if mthd in METHODS:
            self.__method = mthd

    @method.deleter
    def method(self):
        print("deleting")
        self.__method = ''

pay = PaymentX("stripe")
print(pay.method)     # return the property method
# print(pay.method()) # Error: become property not method
pay.method = "paypal" # set the setter method
print(pay.method)
del pay.method
print(pay.method)
