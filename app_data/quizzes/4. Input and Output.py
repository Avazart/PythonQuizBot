# # 1==========================================================================

# ? What will be displayed as an output on the screen

x = float('NaN')
print('%f, %e, %F, %E' % (x, x, x, x))

# + nan, nan, NAN, NAN
# - nan, NaN, nan, NaN
# - NaN, NaN, NaN, NaN,

# # ! <strong>Explanation</strong>: <code>%f</code>, <code>%e</code> produces lowercase output, and <code>%F</code>, <code>%E</code> produces uppercase output.

# > https://pynative.com/python-input-and-output-quiz/


# # 2==========================================================================

# ? What is the output of 

print('%x, %X' % (15, 15))

# - 15 15
# - F F
# - f f
# + f F

# # ! <strong>Explanation</strong>: In output formatting, We use <code>type</code> <code>%x</code> and <code>%X</code> to convert decimal number to hexadecimal number on the screen. <code>%x</code>&nbsp;produces lowercase output, and&nbsp;<code>%X</code>&nbsp;produces uppercase output.

# > https://pynative.com/python-input-and-output-quiz/


# # 3==========================================================================

# ? What is the output of 

print('[%c]' % 65)

# - 65
# - A
# + [A]
# - Syntax Error

# # ! <strong>Explanation</strong>: The <code>c</code> conversion type supports character conversion from ASCII code to the character. It also works for the Unicode

# > https://pynative.com/python-input-and-output-quiz/


# # 4==========================================================================

# ? What is the output of the following code

print('PYnative ', end='//')
print(' is for ', end='//')
print(' Python Lovers', end='//')

# - PYnative / is for / Python Lovers /
# - PYnative // is for // Python Lovers //
# + PYnative // is for // Python Lovers//
# - PYnative / is for / Python Lovers/

# # ! <strong>Explanation</strong>: When we use the keyword argument <code>end</code>, it causes output to be terminated by its content instead of the default newline.

# > https://pynative.com/python-input-and-output-quiz/


# # 5==========================================================================

# ? In Python 3, which functions are used to accept input from the user

# + input()
# - raw_input()
# - rawinput()
# - string()

# # ! <strong>Explanation</strong>: In Python3, we use <code>input()</code> function to accept input from the user. The<code>raw_input()</code> function is removed from Python 3 and onwards.

# > https://pynative.com/python-input-and-output-quiz/


# # 6==========================================================================

# ? Use the following file to predict the output of the code
# ? <b>test.txt Content</b>:
# ? <code>aaa
# ? bbb
# ? ccc
# ? ddd
# ? eee
# ? fff
# ? ggg</code>

with open("test.txt", "r") as f:
    print(f.readline(3))

# - bbb
# - Syntax Error
# + aaa
# - aa

# # ! <strong>Explanation</strong>: <code>fileObject.readline(size)</code>. Here <code>size</code>&nbsp;is the number of bytes to be read from the file.

# # * <strong>Hint</strong>: <a href="https://pynative.com/python-read-file/">Read file in Python</a>.

# > https://pynative.com/python-input-and-output-quiz/


# # 7==========================================================================

# ? What is the output of the following <code>print()</code> function

print(sep='--', 'Ben', 25, 'California')

# + Syntax Error
# - Ben–25–California
# - Ben 25 California
# - Ben–25 California

# # ! <strong>Explanation</strong>: <code>sep</code> is keyword argument Any keyword arguments passed to <code>print()</code> function must come at the end, after the objects to display. Otherwise, you will get a Syntax Error positional argument that follows the keyword argument. The correct way is <code>print('Ben', 25, 'California', sep='--')</code>

# > https://pynative.com/python-input-and-output-quiz/


# # 8==========================================================================

# ? What is the output of the following print() function

print('%d %d %.2f' % (11, '22', 11.22))

# - 11 22 11.22
# + TypeError
# - 11 '22' 11.22

# # ! <strong>Explanation</strong>: when we mention <code>%d</code> in <code>print()</code> function to read string value we will get <code>TypeError: %d format: a number is required, not str</code> It Should be like this <code>print('%d %s %.2f' % (11, '22', 11.22))</code>

# > https://pynative.com/python-input-and-output-quiz/


# # 9==========================================================================

# ? Which of the following is incorrect file handling mode in Python.

# - r
# - x
# + t+
# - b

# # * <strong>Hint</strong>: <a href="https://pynative.com/python/file-handling/">File handling in Python</a>.

# > https://pynative.com/python-input-and-output-quiz/


# # 10=========================================================================

# ? What is true for file mode x

# - create a file if the specified file does not exist
# + Create a file, returns an error if the file exists
# - Create a file if it doesn't exists else Truncate the existed file

# # * <strong>Hint</strong>: <a href="https://pynative.com/python-create-file/">Create File in Python</a>

# > https://pynative.com/python-input-and-output-quiz/


# # 11=========================================================================

# ? Which of the following is incorrect file handling mode in Python

# - wb+
# - ab
# + xr
# - ab+

# > https://pynative.com/python-input-and-output-quiz/


# # 12=========================================================================

# ? In Python3, Whatever you enter as input, the input() function converts it into a string

# - False
# + True

# # ! <strong>Explanation</strong>: If you want to accept number input from the user, you need to convert an input value to the integer type.

# > https://pynative.com/python-input-and-output-quiz/


