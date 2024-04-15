# # 1==========================================================================

# ? What is the output of the following function call


def fun1(num):
    return num + 25


fun1(5)
print(num)

# - 25
# - 5
# + NameError

# # ! <strong>Explanation</strong>: We must accept the return value of a function into a <a href="https://pynative.com/python-variables/">variable</a>. so we can access it in outside function like this

# > https://pynative.com/python-functions-quiz/


# # 2==========================================================================

# ? What is the output of the following display() function call


def display(**kwargs):
    for i in kwargs:
        print(i)


display(emp="Kelly", salary=9000)

# - TypeError
# - Kelly 9000
# - ('emp', 'Kelly') ('salary', 9000)
# + emp salary

# # ! <strong>Explanation</strong>: To <strong>accept Variable Length of Keyword Arguments</strong>, i.e., To create functions that take <code>n</code> number of <strong>Keyword arguments</strong> we use <code>**kwargs</code> (prefix a parameter name with a double asterisk <code>**</code> ). keyword arguments: <code>display(emp="Kelly", salary=9000)</code> This <code>**kwargs</code> collects all passed arguments into a new <a href="https://pynative.com/python-dictionaries/">dictionary</a>, where the argument names are the keys, and their values are the key's values. So to get the values we need to iterate the <code>kwargs</code> dictionary like this <b>Example</b>:

# > https://pynative.com/python-functions-quiz/


# # 3==========================================================================

# ? Select which is true for Python function

# - A Python function can return only a single value
# + A function can take an unlimited number of arguments.
# + A Python function can return multiple values
# - Python function doesn't return anything unless and until you add a return statement

# > https://pynative.com/python-functions-quiz/


# # 4==========================================================================

# ? Given the following function fun1() Please select all the correct function calls


def fun1(name, age):
    print(name, age)


# + fun1("Emma", age=23)
# + fun1(age=23, name="Emma")
# - fun1(name="Emma", 23)
# - fun1(age=23, "Emma")

# # ! <strong>Explanation</strong>: We can pass either use either <strong>positional arguments</strong>&nbsp;or <strong>keyword arguments</strong>, not both at the same time. If you try to do you will get syntax Error The positional argument follows keyword argument <strong>Possible correct function calls</strong>

# > https://pynative.com/python-functions-quiz/


# # 5==========================================================================

# ? What is the output of the following function call


def outer_fun(a, b):
    def inner_fun(c, d):
        return c + d

    return inner_fun(a, b)
    return a


result = outer_fun(5, 10)
print(result)

# - 5
# + 15
# - (15, 5)
# - Syntax Error

# # ! <strong>Explanation</strong>: Adding multiple return statements doesn't perform any task. Once function execution is encountered with the return statement, it stops the execution by returning whatever specified by the return statement.

# > https://pynative.com/python-functions-quiz/


# # 6==========================================================================

# ? Choose the correct function declaration of  fun1() so that we can execute the following function call successfully

fun1(25, 75, 55)
fun1(10, 20)

# - def fun1(**kwargs)
# - No, it is not possible in Python
# - def fun1(args*)
# + def fun1(*data)

# # ! To accept multiple values or if the number of arguments is unknown, we can add <code>*</code> before the parameter name to accept arbitrary arguments. i.e., To <strong>accept Variable Length of Positional Arguments</strong>, i.e., To create functions that take n number of Positional arguments we use <code>*args</code>(prefix a parameter name with an asterisk <code>*</code> ). <em>Example:</em>

# > https://pynative.com/python-functions-quiz/


# # 7==========================================================================

# ? Select which true for Python function

# + A function is a code block that only executes when called and always returns a value.
# + A function only executes when it is called and we can reuse it in a program
# - Python doesn't support nested function

# > https://pynative.com/python-functions-quiz/


# # 8==========================================================================

# ? What is the output of the following function call


def fun1(name, age=20):
    print(name, age)


fun1("Emma", 25)

# + Emma 25
# - Emma 20

# # ! <strong>Explanation</strong>: We can specify default values for arguments when defining a function. the function uses the default value if the value for an argument is missing in a function call. <em>Example</em>: <em>Output</em>: <code>Emma 25</code>

# > https://pynative.com/python-functions-quiz/


# # 9==========================================================================

# ? Python function always returns a value

# - False
# + True

# # ! <strong>Explanation</strong>: If you do not include any <code>return</code> statement in function, it automatically returns&nbsp;<code>None</code>. So, in Python function always returns a value. <em>Example</em>: <em>Output</em>: <code>None</code>

# > https://pynative.com/python-functions-quiz/


# # 10=========================================================================

# ? What is the output of the following display_person() function call


def display_person(*args):
    for i in args:
        print(i)


display_person(name="Emma", age="25")

# + TypeError
# - Emma 25
# - name age

# # ! <strong>Explanation</strong>: To <strong>accept Variable Length of Keyword Arguments</strong>, i.e., To create functions that take n number of Keyword arguments we use <code>**kwargs</code> (prefix a parameter name with a double asterisk <code>**</code> ). keyword arguments: <code>fun1(name='Emma', age=23)</code> <em>Example</em>: Use <code>*args</code> to get the variable number of positional arguments. Example:

# > https://pynative.com/python-functions-quiz/


# # 11=========================================================================

# ? What is the output of the following code?


def outer_fun(a, b):
    def inner_fun(c, d):
        return c + d

    return inner_fun(a, b)


res = outer_fun(5, 10)
print(res)

# + 15
# - Syntax Error
# - (5, 10)

# # ! <strong>Explanation</strong>: Python supports the <strong>nested function</strong>. We can create a nested function to avoid loop or repetition of a code block

# > https://pynative.com/python-functions-quiz/


# # 12=========================================================================

# ? What is the output of the add() function call


def add(a, b):
    return a + 5, b + 5


result = add(3, 2)
print(result)

# - 15
# - 8
# + (8, 7)
# - Syntax Error

# # ! <strong>Explanation</strong>: In Python, we can <strong>return multiple values</strong> from a function. You can do this by separating return values with a comma.

# > https://pynative.com/python-functions-quiz/
