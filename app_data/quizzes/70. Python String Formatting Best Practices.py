# # 1==========================================================================


# ? What’s the main advantage of using f-strings in Python?


# - You can use them to comment your code.
# + You can embed arbitrary Python expressions inside string constants.
# - You can embed special characters in your strings.


# ! F-strings are the most commonly used string formatting and interpolation
# / approach
# ! in modern Python code.


# * F-strings allow you to do something that you can’t do with regular
# / strings.


# > https://realpython.com/quizzes/python-string-formatting/


# # 2==========================================================================


# ? Which formatting method should you use to format user-supplied strings?


# - % operator
# + Template strings
# - F-strings
# - .format()


# ! Following a <a
# / href="https://realpython.com/python-string-formatting/#which-string-formatting-method-should-you-use"
# / target="_blank">rule of thumb</a>,
# ! it may be most secure to use
# ! <a
# / href="https://realpython.com/python-string-formatting/#4-template-strings-standard-library"
# / target="_blank">template strings</a>
# ! to format user-supplied strings.
# ! This helps you avoid security issues.


# * More complex isn’t always better!


# > https://realpython.com/quizzes/python-string-formatting/


# # 3==========================================================================


# ? You’re looking at a flowchart for deciding which string formatting method
# / to use in Python:
# ? Python String Formatting Rule of Thumb
# ? Which of the following options accurately reflect the rule of thumb that
# / this graphic represents?
# ? (Select all the correct options.)


# + Use str.format() if you’re using a version of Python 3 that’s older than 3.6.
# - Use old-style string formatting with the % operator when dealing with user-supplied format strings.
# + Use template strings when your format strings are user-supplied.
# - Use str.format() exclusively, no matter the circumstances.
# + Use f-strings if you’re using Python 3.6 or newer and you’re not handling user-supplied format strings.


# ! The flowchart for choosing a Python string formatting method recommends
# / the following:


# * Pay attention to user-supplied format strings, and also consider the
# / Python version that you’re working with.


# > https://realpython.com/quizzes/python-string-formatting/

