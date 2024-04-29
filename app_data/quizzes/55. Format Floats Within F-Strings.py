# # 1==========================================================================


# ? How do you round a float to two decimal places within a Python f-string?


# - Use the round() function before the f-string
# + Use the format specifier .2f
# - Multiply the float by 100 and round it
# - Use the format specifier .2%


# ! To round a <code>float</code> to two decimal places within a Python
# / f-string, you use the format specifier <code>.2f</code>.
# ! The <code>.2</code> indicates the precision, which is the number of
# / decimal places, and the <code>f</code> is the presentation type
# ! for fixed-point number, which displays the number as a <code>float</code>:


# * The format specifier includes a precision and a presentation type.


# > https://realpython.com/quizzes/format-floats-within-f-strings/


# # 2==========================================================================


# ? How do you format the imaginary part of a complex number to one decimal
# / place using f-strings?


# - Use {value:i} within the f-string
# + Use {value.imag:.1f} within the f-string
# - Use {value.imaginary:.1} within the f-string
# - Imaginary parts can’t be formatted separately


# ! To format the imaginary part of a complex number to one decimal place
# / using f-strings,
# ! you use the <code>.imag</code> property of the complex number and apply
# / the format specifier <code>.1f</code>:


# * The imaginary part of a complex number has its own property.


# > https://realpython.com/quizzes/format-floats-within-f-strings/


# # 3==========================================================================


# ? Which of the following are valid ways to format strings in Python?
# ? (Select all that apply.)


# + Using the built-in format() function with format specifiers
# - Using the str.padding() method with format specifiers
# - Calling format_string() on a string object
# + Using f-strings with embedded expressions and format specifiers
# + Using the str.format() method with replacement fields and format specifiers


# ! Python provides several ways to format strings. The built-in
# / <code>format()</code> function allows
# ! you to format a single value at a time using format specifiers. F-strings,
# / introduced in
# ! Python 3.6, enable you to embed expressions inside string literals for
# / inline evaluations
# ! and formatting. The <code>str.format()</code> method is an earlier string
# / formatting method that
# ! uses replacement fields surrounded by curly braces <code>{}</code> as
# / placeholders for the values
# ! to be formatted.


# * Think about the different ways you’ve learned to include variables and
# / format specifiers
# * within a string.


# > https://realpython.com/quizzes/format-floats-within-f-strings/

