# # 1==========================================================================


# ? What’s the main difference between raw and standard string literals in
# / Python?


# + Raw string literals disable the special treatment of escape character sequences.
# - Raw string literals are always longer than standard string literals.
# - Raw string literals can’t be used with the print() function.
# - Raw string literals can’t contain special characters.


# ! The main difference between raw and standard string literals in Python is
# / that
# ! <a
# / href="https://realpython.com/python-raw-strings/#in-short-python-raw-strings-disable-the-special-treatment-of-escape-character-sequences"
# / target="_blank">raw string literals disable the special treatment of
# / escape character sequences</a>.


# * Think about what happens when you use a backslash in a string.


# > https://realpython.com/quizzes/python-raw-strings/


# # 2==========================================================================


# ? You’re working on a Python script that needs to handle file paths on a
# / Windows system.
# ? Which of the following methods can you use to correctly represent a
# / Windows file path in your script?
# ? (Select all that apply.)


# - Enclosing the path in single quotes with no escape character
# + Using the pathlib module to define paths
# + Replacing each backslash with a double backslash in the path
# + Using a raw string literal


# ! In Python, you can represent a Windows file path in several ways:


# * Remember that the backslash character (<code>\</code>) is the path
# / separator symbol in Windows,
# * but it also serves as the escape character in Python.


# > https://realpython.com/quizzes/python-raw-strings/


# # 3==========================================================================


# ? Why is it considered a best practice to use raw strings when working with
# / regular expressions in Python?


# + They prevent conflicts between the regex syntax and Python’s escape character sequences.
# - They make the regular expressions run faster.
# - They provide additional regex features not available with normal strings.
# - They automatically validate the regular expression syntax.


# ! Using raw strings when working with regular expressions in Python is
# / considered a best practice because
# ! they prevent conflicts between the regex syntax and Python’s escape
# / character sequences.


# * Think about the special characters in regular expressions and Python
# / strings.


# > https://realpython.com/quizzes/python-raw-strings/


# # 4==========================================================================


# ? What happens when you try to end a raw string literal with an odd number
# / of consecutive backslash characters?


# + It raises a SyntaxError for an unterminated string literal
# - It treats the backslashes as escape characters
# - It raises a ValueError
# - It ignores the trailing backslashes


# ! If you try to end a raw string literal with an odd number of consecutive
# / backslash characters,
# ! then Python raises a <code>SyntaxError</code> for an unterminated string
# / literal.
# ! This is because such a string literal gets interpreted as having an
# / unclosed quotation mark:


# * Watch out for those trailing backslashes!


# > https://realpython.com/quizzes/python-raw-strings/


# # 5==========================================================================


# ? How do you escape a 32-bit Unicode character in a Python string literal?


# - Use the format \xhh with exactly two hexadecimal digits
# + Use the format \Uhhhhhhhh with exactly eight hexadecimal digits
# - Use the format \uhhhh with exactly four hexadecimal digits
# - Use the format \N{name} with the Unicode name of the character


# ! To escape a 32-bit Unicode character in a Python string literal,
# ! you use the format <code>\Uhhhhhhhh</code> with exactly eight hexadecimal
# / digits:


# * You need more than four hexadecimal digits for this one!


# > https://realpython.com/quizzes/python-raw-strings/

