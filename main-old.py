# 1.
# class Product():

#     def __init__(self):
#         self.price = 0
#         self.title = ""
#         self.description = ""

# kite = Product()
# kite.price = 14.99
# kite.title = "A red kite"
# kite.description = "Flies up to 150 meters in the air. Made of nylon."

# # Since Python is a dynamically typed language, I can set
# # the value of those variable to anything
# kite.price = dict()  # No complaints here
# kite.description = 1024  # Python don't care


# 2.
class Product():

  def __init__(self):
    self.price = 0.0
    self.title = ""
    self.description = ""

  # the purpose of getters and setters is to have more control over the values
  @property  # The getter
  # The @property decorator lets you call a method like it's just an attribute:
  # When calling NEVER call as a function
  def price(self):
    try:
      return self.__price  # Note there are 2 underscores here: it is a private variable
    except AttributeError:
      return 0 # if price hasn't been set yet, it returns 0 instead of crashing

  @price.setter  # The setter
  # When assigning you will ALWAYS use the assignment operator
  def price(self, new_price):
    if type(new_price) is float:
      self.__price = new_price
    else:
      raise TypeError('Please provide a floating point value for the price')


p = Product()
# p.price = 1  # TypeError: Please provide a floating point value for the price
p.price = 2.0  # Everything works ok
# p.price = 3.0  # Everything works ok
print(p.price)

# 3.
print(dir(p))
