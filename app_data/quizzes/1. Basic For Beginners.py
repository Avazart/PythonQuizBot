# # 1==========================================================================

# ? What is the output of the following code?

for i in range(10, 15, 1):
    print(i, end=", ")

# + 10, 11, 12, 13, 14,
# - 10, 11, 12, 13, 14, 15,

# # ! <strong>Explanation</strong> Remember, the range doesn't include the stop number in the output. Read <a href="https://pynative.com/python-range-function/">Python range function</a> for more details.

# # * <strong>Hint</strong>: <a href="https://pynative.com/python-range-function/">Python range function</a>

# > https://pynative.com/basic-python-quiz-for-beginners/


# # 2==========================================================================

# ? What is the output of the following code?

sample_set = {"Jodi", "Eric", "Garry"}
sample_set.add(1, "Vicki")
print(sample_set)

# - {'Vicki', 'Jodi', 'Garry', 'Eric'}
# - {'Jodi', 'Vicki', 'Garry', 'Eric'}
# + The program executed with error

# # ! <strong>Explanation</strong>: The <a href="https://pynative.com/python-sets/">set</a> is an unordered data structure. Therefore, we cannot access/add/remove its elements by index number.

# > https://pynative.com/basic-python-quiz-for-beginners/


# # 3==========================================================================

# ? What is the output of the following code?

value_one = 5**2
value_two = 5**3

print(value_one, value_two)

# - 10 15
# + 25 125
# - Error: invalid syntax

# # ! <strong>Explanation</strong>: Using two multiplication symbols, we can make a power relationship in Python. We call <code>**</code> operator an exponent operator. For example, the result of expression <code>5 ** 3</code> is 125.

# > https://pynative.com/basic-python-quiz-for-beginners/


# # 4==========================================================================

# ? What is the output of the following code

salary = 8000


def print_salary():
    salary = 12000
    print("Salary:", salary, end=" ")


print_salary()
print("Salary:", salary)

# + Salary: 12000 Salary: 8000
# - Salary: 8000 Salary: 12000
# - The program failed with errors

# # ! <strong>Explanation</strong>: If you define a variable with the same name inside the function and global scope, a function will refer to the local variable by default.

# > https://pynative.com/basic-python-quiz-for-beginners/


# # 5==========================================================================

# ? What is the output of the following code?

s = "pynative"
print(s[1:3])

# - py
# + yn
# - pyn
# - yna

# # ! <strong>Explanation</strong> Remember, the index always starts from 0. Therefore, str [1 : 3] is “yn”

# > https://pynative.com/basic-python-quiz-for-beginners/


# # 6==========================================================================

# ? Can we use the “else” block for for loop?

for i in range(1, 5):
    print(i)
else:
    print("this is else block statement")

# - No
# + Yes

# # ! <strong>Explanation</strong> We can use the else block after the end of <a href="https://pynative.com/python-for-loop/">for loop</a> and <a href="https://pynative.com/python-while-loop/">while loop</a>. The else block is used to check the successful execution of a loop. If the loop executed successfully without any issues, the else block executes.

# > https://pynative.com/basic-python-quiz-for-beginners/


# # 7==========================================================================

# ? What is the output of the following code?

list_one = [20, 40, 60, 80]
list_two = [20, 40, 60, 80]

print(list_one == list_two)
print(list_one is list_two)

# - True True
# + True False
# - False True

# # ! <strong>Explanation</strong> The <code>==</code> (Equal To) operator used to compare the values of two objects and The <code>is</code> operator compares the identity of two objects.

# > https://pynative.com/basic-python-quiz-for-beginners/


# # 8==========================================================================

# ? What is the output of the following code?


def calculate(num1, num2=4):
    res = num1 * num2
    print(res)


calculate(5, 6)

# - 20
# - The program executed with errors
# + 30

# # ! <strong>Explanation</strong> In Python, we can set default values for arguments. If the function is called without the argument, the default value is used.

# # * <strong>Hint</strong>: <a href="https://pynative.com/python-functions/">functions in Python</a>

# > https://pynative.com/basic-python-quiz-for-beginners/


# # 9==========================================================================

# ? What is the output of the following code?

p, q, r = 10, 20, 30
print(p, q, r)

# - 10 20
# + 10 20 30
# - Error: invalid syntax

# # ! <strong>Explanation</strong> In Python, We can do simultaneous assignments to more than one <a href="https://pynative.com/python-variables/">variable</a>.

# > https://pynative.com/basic-python-quiz-for-beginners/


# # 10=========================================================================

# ? What is the output of the following code?

var = "James" * 2 * 3
print(var)

# + JamesJamesJamesJamesJamesJames
# - JamesJamesJamesJamesJames
# - Error: invalid syntax

# # ! <strong>Explanation</strong>: We can use <code>*</code> operator to repeat the string <code>n</code> number of times. For example, in the above question, First, we repeated the string two times, and again we repeated the output string three times.

# > https://pynative.com/basic-python-quiz-for-beginners/


# # 11=========================================================================

# ? What is the Output of the following code?

for x in range(0.5, 5.5, 0.5):
    print(x)

# - [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5]
# - [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
# + The Program executed with errors

# # ! <strong>Explanation</strong> We cannot use float numbers in <code>range()</code> function. Please refer to&nbsp;<a href="https://pynative.com/python-range-for-float-numbers/">How to generate a range of float numbers</a>.

# > https://pynative.com/basic-python-quiz-for-beginners/


# # 12=========================================================================

# ? What is the output of the following code?

var = "James Bond"
print(var[2::-1])

# - Jam
# - dno
# + maJ
# - dnoB semaJ

# # ! <strong>Explanation</strong>: Pick a range of items starting in the reverse direction starting from index 2 with step 1.

# > https://pynative.com/basic-python-quiz-for-beginners/


# # 13=========================================================================

# ? A string is immutable in Python?

# + True
# - False

# # ! <strong>Explanation</strong>: Yes, strings are immutable in Python. You cannot modify a string once created. If you change a string, Python builds a new string with the updated value and assigns it to the <a href="https://pynative.com/python-variables/">variable</a>. <em><strong>Example</strong></em>: <em><strong>Output</strong></em>: Earlier <code>str1</code> was pointing to memory address “140560663354704” now, it's pointing to “140560640152496” which means Python created a new string after you updated it.

# > https://pynative.com/basic-python-quiz-for-beginners/


# # 14=========================================================================

# ? Which operator has higher precedence in the following list

# - % (Modulus)
# - & (BitWise AND)
# + ** (Exponent)
# - > (Comparison)

# > https://pynative.com/basic-python-quiz-for-beginners/


# # 15=========================================================================

# ? What is the output of the following code?

var1 = 1
var2 = 2
var3 = "3"

print(var1 + var2 + var3)

# - 6
# - 33
# - 123
# + Error. Mixing operators between numbers and strings are not supported

# # ! <strong>Explanation</strong> We cannot add strings and numbers together using the <code>+</code> <a href="https://pynative.com/python-operators/">operator</a>. Either we can use the <code>+</code> operator to concatenate strings or add <a href="https://pynative.com/python-numbers/">numbers</a>.

# > https://pynative.com/basic-python-quiz-for-beginners/


# # 16=========================================================================

# ? What is the output of the following code?

sample_list = ["Jon", "Kelly", "Jessa"]
sample_list.append(2, "Scott")
print(sample_list)

# + The program executed with errors
# - ['Jon', 'Kelly', 'Scott', 'Jessa']
# - ['Jon', 'Kelly', 'Jessa', 'Scott']
# - ['Jon', 'Scott', 'Kelly', 'Jessa']

# # ! <strong>Explanation</strong>: The <code>append()</code> method appends an item to the end of the <a href="https://pynative.com/python-lists/">list</a>. Therefore, we cannot pass the index number to it.

# > https://pynative.com/basic-python-quiz-for-beginners/


# # 17=========================================================================

# ? The in operator is used to check if a value exists within an iterable object container such as a list. Evaluate to True if it finds a variable in the specified sequence and False otherwise.

# + True
# - False

# > https://pynative.com/basic-python-quiz-for-beginners/

# # 18=========================================================================

# ? What is the output of the following

x = 36 / 4 * (3 + 2) * 4 + 2
print(x)

# + 182.0
# - 37
# - 117
# - The Program executed with errors

# # ! <strong>Explanation</strong>: To choose the correct answer, You must know the operator precedence and associativity.

# # * <strong>Hint</strong>: <a href="https://pynative.com/python-operators/#h-python-operators-precedence" data-level="2">Python Operators Precedence</a>

# > https://pynative.com/basic-python-quiz-for-beginners/
