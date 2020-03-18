# Custom objetcs: Classes
# Everything in oython is an object
# - strings, integers, lists, dictionaries, tuples, sets, functions etc.
# You can create your own custom objects
# - if an existing type is not adequate for your needs, build your own using classes
# Functions associated with instances of Objects are known as methods


# Objects and Objects Oriented Programming (a programming paradigm)
# 1. uses inheritance, polymorphism, encapsulation and more
# 2. used extensively in software development
# 3. clean, efficient way of packaging, reusing and maintaining code
# 4. can be a course in itself, we will cover customer objects, creation of classses and methods, which are the basis of all OOP
# 5. will demo inheritance and subclasses since it's important to see how it's done, but not in detail, not necessary for this course either

# Build student class
class Student:

    def __init__(self, first, last, course=None):
        self.first_name = first
        self.last_name = last
        if course == None:
            self.course = []
        else:
            self.course = course

    def add_course(self, course):
        if course not in self.course:
            self.course.append(course)
        else:
            print(f'{self.first_name} is already enrolled in the {course} course')

    def remove_course(self, course):
        if course in self.course:
            self.course.remove(course)
        else:
            print(f'{course} not found')

    def __len__(self):
        return len(self.course)

    def __repr__(self):
        return f"Student('{self.first_name}', '{self.last_name}', '{self.course}')"

    def __str__(self):
        return f"First name: {self.first_name.capitalize()}\nLast name: {self.last_name.capitalize()}\
        \nCourse: {','.join(map(str.capitalize, self.course))}"

course_1 = ['python', 'rails', 'javascript']
course_2 = ['java', 'rails', 'c']
mashrur = Student('mashrur','hossain', course_1)
mashrur.add_course('rails')
mashrur.add_course('java')
john = Student('john','doe', course_2)
john.remove_course('c')
john.remove_course('python')

print(mashrur.first_name, mashrur.last_name, mashrur.course)
print(john.first_name, john.last_name, john.course)

print(mashrur)
print(john)
print(dir(mashrur))
print(mashrur.__dict__)

print(len(mashrur))
print(repr(john))
