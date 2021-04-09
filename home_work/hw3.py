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

print(get_length_of_number(124310))

#4
def invert_key_value(dict):
    return {val: key for key, val in dict.items()}

print(invert_key_value({1:2, 3:4}))

#5
class Person:

    def __init__(self, f_name, l_name):
        self.__f_name = f_name
        self.__l_name = l_name

    @property
    def first_name(self):
        return self.__f_name.capitalize()

    @first_name.setter
    def first_name(self, first_name):
        self.__f_name = first_name

    def last_name(self):
        return self.__l_name.capitalize()

    def full_name(self):
        return f"{self.__f_name.capitalize()} {self.__l_name.capitalize()}"

    def initials(self):
        return f"{self.__f_name.capitalize()[0]}." \
               f"{self.__l_name.capitalize()[0]}."


class Casino:
    visitors = {}
    id = 0

    def __init__(self, name):
        self.name = name

    def add_visitor(self, visitor):
        self.visitors[self.id] = visitor
        self.id +=1

    def get_info(self):
        print(f"Casino {self.name} contains {self.visitors}")

    def get_number_of_visitors(self):
        print(self.id)

    def __repr__(self):
        return f'Casino {self.name} '


person = Person('anN', 'ROBson')
person2 = Person('lola', 'bee')
print(person.first_name)
print(person.last_name())
print(person.full_name())
print(person.initials())

palace = Casino("Golden Palace")
person.first_name = 'albert'
palace.add_visitor(person.full_name())
palace.add_visitor(person2.full_name())
palace.get_info()
palace.get_number_of_visitors()

print(person.__repr__())
print(person2.__repr__())
print(person.__dict__)
print(palace.__dict__)

casino2 = Casino("Shazam")
casino3 = Casino("Shazam")
print(casino2.__repr__())
print(casino3.__repr__())
