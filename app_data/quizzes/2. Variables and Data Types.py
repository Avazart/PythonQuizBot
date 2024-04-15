# # 1==========================================================================

# ? What is the data type of

print(type(0xFF))

# - number
# - hexint
# - hex
# + int

# # ! <strong>Explanation</strong>: We can represent integers in binary, octal and hexadecimal formats.

# > https://pynative.com/python-variables-and-data-types-quiz/


# # 2==========================================================================

# ? Select all the right ways to create a string literal Ault'Kelly

# - s = 'Ault\\'Kelly'
# + s = 'Ault\'Kelly'
# + s = """Ault'Kelly"""

# > https://pynative.com/python-variables-and-data-types-quiz/


# # 3==========================================================================

# ? What is the output of the following code?

x = 50

def fun1():
    x = 25
    print(x)
    
fun1()
print(x)

# - NameError
# - 25 25
# + 25 50

# # ! <strong>Explanation</strong>: A variable declared outside of all functions has a GLOBAL SCOPE. Thus, it is accessible throughout the file. And variable declared inside a function is a local variable whose scope is limited to its function.

# > https://pynative.com/python-variables-and-data-types-quiz/


# # 4==========================================================================

# ? What is the output of the following variable assignment?

x = 75

def myfunc():
    x = x + 1
    print(x)

myfunc()
print(x)

# + Error
# - 76
# - 1
# - None

# # ! <strong>Explanation</strong>: Here we have not used a <code>global</code> keyword to reassign a new value to global variable <code>x</code> into <code>myfunc()</code> so Python assumes that <code>x</code> is a local variable. It means you are accessing a local variable before defining it. that is why you received a <code>UnboundLocalError: local variable 'x' referenced before assignment</code> <strong>The correct way</strong> to modify the global variable inside a function:

# > https://pynative.com/python-variables-and-data-types-quiz/


# # 5==========================================================================

# ? What is the output of the following code

print(bool(0), bool(3.14159), bool(-3), bool(1.0+1j))

# - False True False True
# - True True False True
# - True True False True
# + False True True True

# # ! <strong>Explanation</strong>:

# > https://pynative.com/python-variables-and-data-types-quiz/


# # 6==========================================================================

# ? What is the data type of 

print(type(10))

# - float
# - integer
# + int

# > https://pynative.com/python-variables-and-data-types-quiz/


# # 7==========================================================================

# ? What is the output of 

print(type({}) is set)

# - True
# + False

# # ! <strong>Explanation</strong>: When the object is created without any items inside the curly brackets ( <code>{}</code> ) then it will be created as a <strong><a href="https://pynative.com/python-dictionaries/">dictionary</a>&nbsp;</strong>which is another built-in data structure in Python. So whenever you wanted to create an empty <a href="https://pynative.com/python-sets/">set</a> always use the&nbsp;<code>set()</code>&nbsp;constructor

# > https://pynative.com/python-variables-and-data-types-quiz/


# # 8==========================================================================

# ? What is the data type of the following

tpl = (1, 'Jhon', 1+3j)
print(type(tpl[2:3]))

# - list
# - complex
# + tuple

# # ! <strong>Explanation</strong>: When we access a tuple using the subscript <code>tpl[start : end]</code> operator, it will always return a tuple. We also call it tuple slicing. (taking a subset of a tuple using the range of indexes).

# > https://pynative.com/python-variables-and-data-types-quiz/


# # 9==========================================================================

# ? Select all the valid String creation in Python

# + s = 'abc'; s = "abc";  s = '''abc'''
# - s = 'abc'; s = "abc""; s = '''abc''
# - s = str(Jessa)

# # ! <strong>Explanation</strong>: Strings in Python are surrounded by either single quotation marks or double quotation marks. Also, You can create a multiline string using three quotation marks.

# > https://pynative.com/python-variables-and-data-types-quiz/


# # 10=========================================================================

# ? Please select the correct expression to reassign a global variable "x" to 20 inside a function fun1()

x = 50

def fun1():
    # your code to assign global x = 20
    
fun1()
print(x) # it should print 20

# - global x = 20
# - global var x; x = 20
# - global.x = 20
# + global x; x = 20

# > https://pynative.com/python-variables-and-data-types-quiz/


# # 11=========================================================================

# ? In Python 3, what is the output of code (What data type it will return).

print(type(range(5)))

# - int
# - list
# + range
# - None

# # ! <strong>Explanation</strong>: in Python 3, the <code>range()</code>&nbsp; function returns range object, not <a href="https://pynative.com/python-lists/">list</a>.

# # * <strong>Hint</strong>: <a href="https://pynative.com/python-range-function/">range() in Python</a>

# > https://pynative.com/python-variables-and-data-types-quiz/


# # 12=========================================================================

# ? What is the output of the following code

def func1():
    x = 50
    return x
    
func1()
print(x)

# - 50
# + NameError
# - None
# - 0

# # ! <strong>Explanation</strong>: You will get a <code>NameError: name 'x' is not defined</code>. To access the function's return value we must accept it using an assignment operator like this

# > https://pynative.com/python-variables-and-data-types-quiz/


# # 13=========================================================================

# ? What is the result of 

print(type([]) is list)

# - False
# + True

# > https://pynative.com/python-variables-and-data-types-quiz/


