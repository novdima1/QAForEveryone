"""
Home_work_2, Week 2, 17 March 2021
1. Write a Python program to print a specified list after removing the 0th, 4th, and 5th elements.
2. Write a Python program to generate and print a list except for the first 5 elements
3. Write a Python program to assign a number to a and b and print the result of sum, subtraction, multiplication, division
4. Write a Python program to assign a number to either a or b and another should be a string and print the result of the multiplication. Also, print change both to string and print out "a + any word + b" 10 times where a and b are your values.
5. Write a Python program to print a list of integers without minimum and maximum values
6. Write a Python program to sort and then print reverse list: ['b', 'n', 'A', 'g', 'S', 'p', 'm', 'r', 'R', 'X', 'z', 'B', 'I', 'H', 'A', 'e', 't', 'k', 'k', 'k', 'l', 'c', 'g', 'S', 'P', 'q', 'Y', 'Q']
"""

# 1
def print_sp_list():
    N = 5 #int(input("Enter a number\n"))
    A = [x for x in range(N) if x != 0 if x != 4 if x != 5]
    print(A)
print_sp_list()

list = list(range(10))
print(list)
list.pop(0)
list.pop(3)
list.pop(3)
print(list)

# 2
# list = list(range(10)) # -> TypeError: 'list' object is not callable
list = [*range(1,10)]
print(list[5:])


# 3
a, b = 1, 2
print(f"Sum: {a+b}")
print("Sub:",  a-b)
print(f"Mult: {a*b}")
print(f"Div: {a/b}")


class Operation:

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def subt(self):
        if self.a > self.b:
            return (self.a - self.b)
        return (self.b - self.a)

    def mult(self):
        return self.a * self.b

    def div(self):
        return (self.a / self.b)

numbers = Operation(10, 50)
print(numbers.add())
print(numbers.subt())
print(numbers.mult())
print(numbers.div())

# 4
def str_or_int(a, b):
    a = int(a)
    b = int(b)
    c = "greater then"
    if a > b:
        print(a, c, b)
    elif a < b:
        print(b, c, a)
    else:
        print(b, "equal", a)
str_or_int(1,2)
str_or_int(5,2)
str_or_int(2,2)


# 5
list = [*range(1,11)]
list.append(1)
list.append(11)
origin_list = list.copy()
list_min = min(list)
list_max = max(list)
list = [x for x in list if x != list_min if x != list_max]
print(f"Original list: {origin_list}", f"\nFinal list: {list}")

# 6
list = ['b', 'n', 'A', 'g', 'S', 'p', 'm', 'r', 'R', 'X', 'z', 'B', 'I', 'H', 'A', 'e', 't', 'k', 'k', 'k', 'l', 'c', 'g', 'S', 'P', 'q', 'Y', 'Q']
res = sorted(list)
res.reverse()
print(res)

list = ['b', 'n', 'A', 'g', 'S', 'p', 'm', 'r', 'R', 'X', 'z', 'B', 'I', 'H', 'A', 'e', 't', 'k', 'k', 'k', 'l', 'c', 'g', 'S', 'P', 'q', 'Y', 'Q']
list.sort(reverse=True)
print(list)
