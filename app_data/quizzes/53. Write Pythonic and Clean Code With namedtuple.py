# # 1==========================================================================


# ? What’s the main advantage of using Python’s named tuple over regular
# / tuples?


# - Named tuples are mutable.
# - You can’t use regular tuples as dictionary keys.
# + You can access values using descriptive field names instead of integer indices.
# - Named tuples consume less memory than regular tuples.


# ! The main advantage of using Python’s named tuple
# ! over regular
# ! <a href="https://realpython.com/python-tuple/" target="_blank">tuples</a>
# ! is that you can access values using descriptive field names
# ! instead of integer indices. This
# ! <a
# / href="https://realpython.com/python-namedtuple/#using-namedtuple-to-write-pythonic-code"
# / target="_blank">improves code readability</a>
# ! and maintainability.


# * Named tuples make your code more Pythonic.


# > https://realpython.com/quizzes/python-namedtuple/


# # 2==========================================================================


# ? What does the rename argument do when you set it to True in a namedtuple?


# - It automatically renames the namedtuple using Python’s built-in LLM.
# + It automatically replaces invalid field names with positional names.
# - It automatically renames all field names to be lowercase, which is necessary for validity.


# ! You can use the <code>rename</code> argument in a <code>namedtuple</code>
# / to handle invalid field names.
# ! If you set <code>rename</code> to <code>True</code>, then all the invalid
# / field names are automatically replaced with positional names.


# * It helps you make sure that your field names are valid.


# > https://realpython.com/quizzes/python-namedtuple/


# # 3==========================================================================


# ? What’s the result of calling ._asdict() on a named tuple?


# + A new dictionary object
# - A new tuple object
# - A new named tuple object


# ! The <code>._asdict()</code> method returns a new dictionary
# ! that maps field names to their corresponding values in the original named
# / tuple.


# * Consider the name of the method.


# > https://realpython.com/quizzes/python-namedtuple/


# # 4==========================================================================


# ? Why might you use a named tuple when returning multiple values from a
# / function?


# - To avoid using lists or dictionaries
# - To make the function run faster
# + To provide context for each returned value


# ! You might use a named tuple when returning multiple values from a function
# ! to provide context for each returned value.
# ! This can make your code more readable because the returned values will
# / also
# ! provide some context for their content.


# * Named tuples can make your code more readable.


# > https://realpython.com/quizzes/python-namedtuple/


# # 5==========================================================================


# ? Which of the following statements about the key differences between named
# / tuples and data classes is true?


# - Named tuples are immutable, data classes are always mutable.
# - Named tuples can’t have default values for their fields.
# - Data classes can’t be iterated over.
# + Data classes have a larger memory footprint than named tuples.


# ! Named tuples and data classes in Python are similar in many ways, but they
# / also have some key differences:


# * When it’s really cold, even a data class can freeze!


# > https://realpython.com/quizzes/python-namedtuple/

