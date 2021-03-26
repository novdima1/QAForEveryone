"""
1.  Write function for list of integers (create own) which returns list but with each element's index added to itself.
E.g function_name([0, 1, 3, 5]) => [0, 2, 5, 8]

2. Write function for list of elements (create own) that will return indices of all occurrences of that item in list
e.g. function_name([ 1, 2, 4, 'b', 'b', 'b', 1], 'b') => [3, 4, 5]
e.g. function_name([ 1, 2, 4, 'b', 'b', 'b', 1], 1) => [0, 6]
e.g. function_name([ 1, 2, 4, 'b', 'b', 'b', 1], 'c') => []

3. Create a function that takes an integer and returns its length.
e.g. function_name(8) => 1
e.g. function_name(88) => 2
e.g. function_name(83894) => 5
(Can't use len)

4. Write a function that inverts the keys and values of a dictionary.
e.g. function_name({ 'a': 'b', 'c': 'd' }) => { 'b': 'a', 'd': 'c' }
e.g. function_name({ 'fruit': 'apple', 'meat': 'beef' }) => { 'apple': 'fruit', 'beef': 'meat' }

5. Create a class with attributes for last name and first name, full name and initials. Add functions to print full name, last name, first name, and initials
object_name = ClassName('john', 'DOE')
object_name.attribute_for_name => 'John Doe'
object_name.attribute_for_last_name => 'Doe'
object_name.attribute_for_first_name => 'John'
object_name.attribute_for_initials => 'J.D.'
object_name.print_full_name() => 'John Doe'
"""

# 1
def add_index_to_element(lst):
    return list(map(lambda n: n+lst.index(n), lst))

print(add_index_to_element([1,2,3,4,5,10]))

#2
def indices_of_all_occurrences(lst, item):
    return [i for i, v in enumerate(lst) if v == item]

print(indices_of_all_occurrences([1,'f',3,'f',3], 'f'))

#3
def get_length_of_number(out):
    return sum(not out not in out for out in str(out))

print(get_length_of_number(1231))

#4
def invert_key_value(dict):
    return {val: key for key, val in dict.items()}

print(invert_key_value({1:2, 3:4}))

#5
class Person:

    def __init__(self, f_name, l_name):
        self.f_name = f_name
        self.l_name = l_name

    def first_name(self):
        return self.f_name.capitalize()

    def last_name(self):
        return self.l_name.capitalize()

    def full_name(self):
        return f"{self.f_name.capitalize()} {self.l_name.capitalize()}"

    def initials(self):
        return f"{self.f_name.capitalize()[0]}.{self.l_name.capitalize()[0]}."


person = Person('anN', 'ROBson')
print(person.first_name())
print(person.last_name())
print(person.full_name())
print(person.initials())