class Student():
  first_name = ""
  last_name = ""
  age = None
  cohort_number = None
  __full_name = first_name + " " + last_name
  
  # define getters for all properties
  @property
  def first_name(self):
    try:
      return self.__first_name
    except AttributeError:
      return None
  
  # define a setter for all but the read only properties
  
  
  
  # str method
  def __str__(self):
    return f"{self.full_name} is {self.age} years old and is in cohort {self.cohort_number}."
