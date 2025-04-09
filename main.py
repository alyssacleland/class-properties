# using w/ student.py
from student import Student



alyssa = Student()
# alyssa.first_name = alyssa # TypeError: First name must be a string
alyssa.first_name = "Alyssa" #works
alyssa.last_name = "Cleland"
print(alyssa.first_name)
print(alyssa.full_name)
# alyssa.full_name = "a c" #AttributeError: can't set attribute ( it is a read-only, computed property, not a stored one!)
