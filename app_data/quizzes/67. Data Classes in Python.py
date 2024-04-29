# # 1==========================================================================


# ? What’s a disadvantage of using a namedtuple instead of a data class?


# + Namedtuples are immutable so you can’t modify them after creation.
# - Namedtuples require a third-party library.
# - Namedtuples are equivalent to data classes.
# - Namedtuples don’t allow comparison to other namedtuples.


# ! <a href="https://realpython.com/python-namedtuple/"
# / target="_blank">Namedtuples</a>
# ! are a viable <a
# / href="https://realpython.com/python-data-classes/#alternatives-to-data-classes"
# / target="_blank">alternative to data classes</a>.
# ! However, namedtuples are <strong>immutable</strong>, which means that you
# / can’t modify them after you’ve created them.


# * Think about what happens when you try to change a value in a namedtuple.


# > https://realpython.com/quizzes/python-data-classes/


# # 2==========================================================================


# ? How can you add default values to the fields of a data class in Python?


# - By passing the default values to the dataclass decorator.
# - By defining a .__defaults__() method in the class.
# + By assigning the default values in the class definition.


# ! You can add <a
# / href="https://realpython.com/python-data-classes/#default-values"
# / target="_blank">default values</a>
# ! to the fields of a data class by assigning the default values in the class
# / definition:


# * It’s as straightforward as assigning a value to a variable.


# > https://realpython.com/quizzes/python-data-classes/


# # 3==========================================================================


# ? What’s the role of type hints in data classes?


# - Type hints are only mandatory for defining a frozen data class.
# - Type hints are optional, like anywhere else in Python.
# + Type hints are mandatory for defining fields in a data class.


# ! In Python data classes, <a
# / href="https://realpython.com/python-data-classes/#type-hints"
# / target="_blank">type hints</a>
# ! are mandatory when defining fields.


# * Python is dynamically typed, but there’s a certain structure to data
# / classes.


# > https://realpython.com/quizzes/python-data-classes/


# # 4==========================================================================


# ? Can you add your own methods to a Python data class?


# + Yes
# - No
# - Yes, but only class methods


# ! Yes, you can <a
# / href="https://realpython.com/python-data-classes/#adding-methods"
# / target="_blank">add your own methods</a>
# ! to a Python data class.
# ! A data class is just a regular class, so you can freely add methods to it.


# * Remember, a data class is just a regular class.


# > https://realpython.com/quizzes/python-data-classes/


# # 5==========================================================================


# ? How can you make instances of a data class comparable?


# - Add the @comparable decorator above the @dataclass decorator.
# + Set order=True in the @dataclass decorator.
# - Implement a .__compare__() method in the class.
# - Set __eq__=True in the @dataclass decorator.


# ! You can make instances of a data class <a
# / href="https://realpython.com/python-data-classes/#comparing-cards"
# / target="_blank">comparable</a>
# ! by setting <code>order=True</code> in the <code>@dataclass</code>
# / decorator:


# * Data classes make creating classes more readable and straightforward.


# > https://realpython.com/quizzes/python-data-classes/


# # 6==========================================================================


# ? What happens when you try to assign a new value to a field of an instance
# / of a frozen data class?


# - It raises a TypeError
# - It changes the value of the field
# + It raises a FrozenInstanceError
# - It silently ignores the assignment


# ! When you try to assign a new value to a field of an instance
# ! of a frozen data class, it raises a <code>FrozenInstanceError</code>:


# * Frozen means that you won’t be able to change the values after creation.


# > https://realpython.com/quizzes/python-data-classes/


# # 7==========================================================================


# ? What happens if you try to add a field without a default value to a
# / subclass of a data class, where the base class has fields with default
# / values?


# - It removes the default values from the base class fields
# + It raises a TypeError
# - It ignores the new field
# - It works without any issues


# ! If a field in a <a
# / href="https://realpython.com/python-data-classes/#inheritance"
# / target="_blank">base class of a Python data class</a>
# ! has a default value, then all new fields added in a subclass must also
# / have default values.


# * Python has some rules about default values and the order of parameters.


# > https://realpython.com/quizzes/python-data-classes/

