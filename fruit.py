# YOUTUBE VIDEO: https://www.youtube.com/watch?v=Sz9G0iwwHQI&t=156s

#### INSTANTIATE CLASSS AND PROPERTIES ####

class Fruit:
  def __init__(self, name: str): # 8 this is type hinting. it doesn’t actually enforce anything at runtime; it’s just a way to communicate expectations to other developers or tools (e.g., linters, IDEs, or static analyzers).
    self._name = name
  
  
  ##### GETTER ######
  
  # 4a: GETTER. essentially gives us a method to access name so that we don't use the "forbidden" way of accessing it via fruit._name. by forbidden i mean: so we don't access it directly in a way that's discouraged by convention
  # 4b: The idea is to abstract access — so if the way we get or store the name changes later, outside code doesn't break.
  # 5: the decorator @property let's you call a method like it's just an attribute (not as a function, never call it as a fx). you can call get_name instead of get_name()
  @property
  def name(self): # 6: if you wanted to just name it name you could to make it like normal ish but i guess that kind of defeats the purpose of naming it _name in the first place, idk? 
    print('Getting name')
    return self._name
  #7: Why use the getter and setter? # Encapsulation: You're controlling how the internal variables are accessed and modified. This means you can add logic (like validation) when getting or setting values, and you can make the variable read-only if necessary.
  # Flexibility: If the internal implementation (e.g., how you store the name) changes, you don’t have to worry about breaking other code that’s using it because they’re just using the fruit.name property. This makes your code more maintainable and flexible.
  
  
  ##### SETTER ######
  
  #9: The @setter decorator in Python is used to define a method for setting the value of a property. It's part of Python's property mechanism, which allows you to manage attribute access in a controlled way. When you define a property using @property, you can also define a corresponding setter method using @<property_name>.setter. This setter method is called whenever you assign a value to the property
  #9b: The setter method allows you to control how a property is set (assigned). It’s part of Python's property mechanism, which allows you to define a controlled way to set values for attributes that have a corresponding getter (and optionally, a setter). The setter is used when you assign a value to the property (i.e., when you use the assignment operator = to set a value).
  #9c: in @xxx.setter, xxx can only be the name of a method that has already been wrapped in @property 
  #10: (see refined at bottom) I SORT OF GET IT? using getters and setters allows us to put restrictions on variables of the property name we specify (_name still won't have the restrictions, but the _ in the name hints we shouldn't mess with it). 
  # 10b: in the getter, we return self._name, which is the internal storage for the name property. so when we update _name in the setter, it updates _name correctly in the getter (which updates name property of the class because it's named the same as the getter method? noo.. not here) and in the _name property 
  #10c: so does this make accessing fruit.name (class property) have the restrictions from the getter/setter?
  # (skip this if reading? in main-old, a bit different, it shows how you could raise an error for the type there and set default if that is true. __price are only accessible in the getters and setters. idk )
  #10c: 
  @name.setter 
  def name(self, new_name: str):
    if type(new_name) is str:
      self._name = new_name
  
  
  
  #### LET'S DO SHIT W/ IT? ####
if __name__ == '__main__':
  fruit = Fruit('Banana')
  # 1: when we call the fruit, we don't get any of the variable names suggested to our fruit ( we don't get name, because it's _name). idk about that. it still suggested it for me 
  # fruit._name
  print(fruit._name) # 2: we can print it. it's not actually private. just naming convention to signal to other devs (to not touch it, only use w/in class), but doesn't actually do anything to prevent access or adjust privacy
  
  
# 3: so how can we actually  have some control over that?



# refined #10 comments s/o to chatgpt:
# 10: I SORT OF GET IT? 
# Using getters and setters allows us to put restrictions on a property (like 'name') 
# while still giving it a clean interface (fruit.name). 
# The actual value is stored in _name, which is conventionally 'private' — 
# we’re signaling not to touch it directly from outside the class.

# 10b: In the getter, we return self._name. 
# In the setter, we update self._name only if certain conditions are met. 
# Since both the getter and setter are tied to the same property name ('name'),
# calling fruit.name gets the value from the getter,
# and assigning to fruit.name (like fruit.name = "Peach") uses the setter. 
# So yes — updating _name in the setter makes sure the getter returns the right thing.

# 10c: So does this mean accessing fruit.name has the restrictions from the getter/setter?
# ✅ YES! That’s the whole point. fruit.name is now a "managed" attribute —
#    the getter controls what you see, the setter controls what you’re allowed to set.
#✅ Cleaned-up version:

# In the getter, we return self._name, which is the internal storage for the name property.
# In the setter, we update self._name — but only if the value meets our conditions (like being a string).
# So when we get fruit.name, it uses the getter and returns self._name.
# When we set fruit.name = "Peach", it uses the setter and updates self._name.

# The key is:
# 🔹 fruit.name is the public interface, with the restrictions.
# 🔹 self._name is the "private" internal variable that actually holds the value.

# We don’t access _name from outside the class — we use the controlled name property instead.
