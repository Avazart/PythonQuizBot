# # 1==========================================================================

# ? Select which is true for for loop

# + Python's for loop used to iterates over the items of list, tuple, dictionary, set, or string
# + else clause of for loop is executed when the loop terminates naturally
# - else clause of for loop is executed when the loop terminates abruptly
# - We use for loop when we want to perform a task indefinitely until a particular condition is met

# # ! <strong>Explanation</strong>: We use <a href="https://pynative.com/python-while-loop/">while loop</a> when we want to perform a task indefinitely until a particular condition is true.

# > https://pynative.com/python-if-else-and-for-loop-quiz/


# # 2==========================================================================

# ? Given the nested if-else structure below, what will be the value of x after code execution completes

x = 0
a = 0
b = -5
if a > 0:
    if b < 0:
        x = x + 5
    elif a > 5:
        x = x + 4
    else:
        x = x + 3
else:
    x = x + 2
print(x)

# + 2
# - 0
# - 3
# - 4

# > https://pynative.com/python-if-else-and-for-loop-quiz/

# # 3==========================================================================

# ? What is the value of x after the following nested for loop completes its execution

x = 0
for i in range(10):
    for j in range(-1, -10, -1):
        x += 1
        print(x)

# - 99
# + 90
# - 100

# > https://pynative.com/python-if-else-and-for-loop-quiz/

# # 4==========================================================================

# ? What is the value of x

x = 0
while x < 100:
    x += 2
print(x)

# - 101
# - 99
# - None of the above, this is an infinite loop
# + 100

# > https://pynative.com/python-if-else-and-for-loop-quiz/

# # 5=========================================================================

# ? Given the nested if-else below, what will be the value x when the code executed successfully

x = 0
a = 5
b = 5
if a > 0:
    if b < 0:
        x = x + 5
    elif a > 5:
        x = x + 4
    else:
        x = x + 3
else:
    x = x + 2
print(x)

# - 0
# - 4
# - 2
# + 3

# > https://pynative.com/python-if-else-and-for-loop-quiz/

# # 6==========================================================================

# ? What is the output of the following for loop and  range() function

for num in range(-2, -5, -1):
    print(num, end=", ")

# - -2, -1, -3, -4
# - -2, -1, 0, 1, 2, 3,
# - -2, -1, 0
# + -2, -3, -4,

# > https://pynative.com/python-if-else-and-for-loop-quiz/


# # 7==========================================================================

# ? What is the output of the following range() function

for num in range(2, -5, -1):
    print(num, end=", ")

# - 2, 1, 0
# - 2, 1, 0, -1, -2, -3, -4, -5
# + 2, 1, 0, -1, -2, -3, -4

# > https://pynative.com/python-if-else-and-for-loop-quiz/

# # 8==========================================================================

# ? What is the output of the following nested loop

numbers = [10, 20]
items = ["Chair", "Table"]

for x in numbers:
    for y in items:
        print(x, y, end=";")

# + 10 Chair; 10 Table; 20 Chair; 20 Table;
# - 10 Chair; 10 Table;

# > https://pynative.com/python-if-else-and-for-loop-quiz/


# # 9==========================================================================

# ? What is the output of the following if statement

a, b = 12, 5
if a + b:
    print("True")
else:
    print("False")

# - False
# + True

# # ! <strong>Explanation</strong>: In Python, any non-zero value is considered <strong>TRUE</strong>. So it will evaluate to true

# > https://pynative.com/python-if-else-and-for-loop-quiz/


# # 10=========================================================================

# ? What is the output of the following loop

for l in "Jhon":
    if l == "o":
        pass
    print(l, end=", ")

# - J, h, n,
# + J, h, o, n,

# # ! <strong>Explanation</strong>: In Python, the <strong><code>pass</code></strong> is a null operation. The Python interpreter executes the <code>pass</code> statement without any activity. The <code>pass</code> statement is useful when you want to write the pseudo code that you want to implement in the future.

# > https://pynative.com/python-if-else-and-for-loop-quiz/


# # 11=========================================================================

# ? What is the value of the var after the for loop completes its execution

var = 10
for i in range(10):
    for j in range(2, 10, 1):
        if var % 2 == 0:
            continue
            var += 1
    var += 1
else:
    var += 1
print(var)

# - 20
# + 21
# - 10
# - 30

# # ! <strong>Explanation</strong>:

# > https://pynative.com/python-if-else-and-for-loop-quiz/

# # 12=========================================================================

# ? if -3 will evaluate to True

# + True
# - False

# # ! <strong>Explanation</strong>: In Python, any non-zero value or nonempty container is considered TRUE.

# > https://pynative.com/python-if-else-and-for-loop-quiz/


# # 13=========================================================================

# ? What is the output of the following nested loop?

for num in range(10, 14):
    for i in range(2, num):
        if num % i == 1:
            print(num)
            break

# + 10 11 12 13
# - 11 13

# # ! <strong>Explanation</strong>: We use a <code>break</code> statement to terminate the loop and transfer execution to the statement immediately following the loop.

# # * <strong>Hint</strong>: <a href="https://pynative.com/python-break-continue-pass/">Break and continue in Python</a>

# > https://pynative.com/python-if-else-and-for-loop-quiz/
