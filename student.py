# link to lesson: https://nss-evening-curriculum.netlify.app/python/class-properties-solid-student


class Student:
    def __init__(self):
        self.__first_name = ""
        self.__last_name = ""
        self.__age = 0
        self.__cohort_number = 0

    # First name
    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        if isinstance(value, str):
            self.__first_name = value
        else:
            raise TypeError("First name must be a string")

    # Last name
    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        if isinstance(value, str):
            self.__last_name = value
        else:
            raise TypeError("Last name must be a string")

    # Age
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if isinstance(value, int):
            self.__age = value
        else:
            raise TypeError("Age must be an integer")

    # Cohort number
    @property
    def cohort_number(self):
        return self.__cohort_number

    @cohort_number.setter
    def cohort_number(self, value):
        if isinstance(value, int):
            self.__cohort_number = value
        else:
            raise TypeError("Cohort number must be an integer")

    # Full name (read-only)
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    # String representations
    def __str__(self):
        return f"{self.full_name} is {self.age} years old and is in cohort {self.cohort_number}"

    def __repr__(self):
        return self.__str__()
