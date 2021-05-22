def f(x):
    return x % 2 != 0 and x % 3 !=0
result = list(filter(f, range(1,20)))
# print(result)

class parent:
    def __init__(self, param):
        self.v1 = param

class child(parent):
    def __init__(self, param):
        self.v2 = param

obj = child(5)
# print("%d %d"%(obj.v1, obj.v2))

def f1():
    x, y = 15, 45
    res = x if x < y else y
    print(res)
# f1()

# x = 10
# def foo():
#     print(x)
#     x = x - 1
# foo()
# print(x)

class A:
    def __init__(self, i=0):
        self.i = i
class B(A):
    def __init__(self, j=0):
        self.j =j

# def main():
#     b = B()
#     print(b.i)
#     print(b.j)
# main()


# nums = list()
# i = 3
# while (i < 9):
#     nums.append(i)
#     i = i + 2
# print(nums)

# def foo(x=[]):
#     x.append(1)
#     print(x)
# foo()
# foo()
# foo()

class Book:
    def __init__(self, isbn):
        self.isbn = isbn
        isbn = "test"

# book = Book(12345)
# print(book.isbn)

def change_list(list1, list2):
    list1.append('four')
    list2 = ["we", "can", "not", "lie"]
outer_list1 = ["one", "two", "three"]
outer_list2 = ["we", "like", "porper", "English"]
# change_list(outer_list1, outer_list2)
# print(outer_list1)
# print(outer_list2)

