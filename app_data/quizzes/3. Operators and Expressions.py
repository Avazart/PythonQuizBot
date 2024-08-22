# # 1==========================================================================


# ? What is the output of the following code


x = 100
y = 50

print(x and y)


# - True
# - 100
# - False
# + 50


# ! <strong>Explanation:</strong> In Python, When we join two non-Boolean
# / values using a <code>and</code> operator, the value of the expression is
# / the second operands, not <code>True</code> or <code>False</code>.


# > https://pynative.com/python-operators-and-expression-quiz/


# # 2==========================================================================


# ? What is the output of


print(2 * 3 ** 3 * 4)


# + 216
# - 864


# ! <strong>Explanation</strong>: The exponent (<code>**</code>) operator has
# / higher precedence than multiplication (<code>*</code>). Therefore the
# / statement <code>print(2 * 3 ** 3 * 4)</code> evaluates to <code>print(2 *
# / 27 * 4)</code>


# > https://pynative.com/python-operators-and-expression-quiz/


# # 3==========================================================================


# ? 4 is 100 in binary and 11 is 1011. What is the output of the following
# / bitwise operators?


a = 4
b = 11
print(a | b)
print(a >> 2)


# + 15 1
# - 14 1


# ! <strong>Explanation</strong>: Bitwise right shift
# / operator(<code>&gt;&gt;</code>): The a's value is moved right by the 2
# / bits.


# > https://pynative.com/python-operators-and-expression-quiz/


# # 4==========================================================================


# ? What is the output of the expression


print(-18 // 4)


# - -4
# - 4
# + -5
# - 5


# ! <strong>Explanation</strong>: In the case of <strong>floor
# / division</strong> operator (<code>//</code>), when the result is negative, the result is
# / rounded down to the next smallest (big negative) integer.


# > https://pynative.com/python-operators-and-expression-quiz/


# # 5==========================================================================


# ? What is the output of


print(2%6)


# - ValueError
# - 0.33
# + 2


# ! <strong>Explanation</strong>: The first number is the numerator, and the
# / second is the denominator. here, 2 is divided by 6. So the remainder is 2.
# / Therefore the result is 2


# > https://pynative.com/python-operators-and-expression-quiz/


# # 6==========================================================================


# ? What is the value of the following Python Expression


print(36 / 4)


# + 9.0
# - 9


# ! <strong>Explanation</strong>: Remember the result of a <strong>division
# / operator(<code>/</code>)</strong>, is always float value.


# > https://pynative.com/python-operators-and-expression-quiz/


# # 7==========================================================================


# ? What is the output of


print(10 - 4 * 2)


# + 2
# - 12


# ! <strong>Explanation</strong>: The multiplication(*) operator has higher
# / precedence than minus(-) operator


# > https://pynative.com/python-operators-and-expression-quiz/


# # 8==========================================================================


# ? Which of the following operators has the highest precedence?


# - not
# - &
# + *
# - +


# * <strong>Hint</strong>: 
# / <a href="https://pynative.com/python-operators/#h-python-operators-precedence">Python operators precedence</a>


# > https://pynative.com/python-operators-and-expression-quiz/


# # 9==========================================================================


# ? Bitwise shift operators (&lt;&lt;, &gt;&gt;) has higher precedence than Bitwise And(&amp;)
# / operator


# - False
# + True


# > https://pynative.com/python-operators-and-expression-quiz/


# # 10=========================================================================


# ? What is the output of the following code


print(bool(0), bool(3.14159), bool(-3), bool(1.0+1j))


# - True True False True
# + False True True True
# - True True False True
# - False True False True


# > https://pynative.com/python-operators-and-expression-quiz/


# # 11=========================================================================


# ? What is the output of the following Python code


x = 10
y = 50
if x ** 2 > 100 and y < 100:
    print(x, y)


# - 100 500
# - 10 50
# + None


# > https://pynative.com/python-operators-and-expression-quiz/


# # 12=========================================================================


# ? What is the output of the following assignment operator


y = 10
x = y += 2
print(x)


# - 12
# - 10
# + SynatxError


# ! <strong>Explanation</strong>: <code>x = y += 2</code> expression is
# / Invalid


# > https://pynative.com/python-operators-and-expression-quiz/


# # 13=========================================================================


# ? What is the output of the following code


x = 6
y = 2
print(x ** y, x // y)


# - 66 0
# - 36 0
# - 66 3
# + 36 3


# > https://pynative.com/python-operators-and-expression-quiz/


# # 14=========================================================================


# ? What is the output of


print(2 ** 3 ** 2)


# - 64
# + 512


# ! <strong>Explanation</strong>: Remember, we have not used brackets here.
# / And Exponent operator <code>**</code> has right-to-left associativity in
# / Python.


# > https://pynative.com/python-operators-and-expression-quiz/


# # 15=========================================================================


# ? What is the output of the following addition (+) operator


a = [10, 20]
b = a
b += [30, 40]

print(a, b)


# + [10, 20, 30, 40] [10, 20, 30, 40]
# - [10, 20] [10, 20, 30, 40]


# ! <strong>Explanation</strong>: Because both <code>b</code> and
# ! <code>a</code> refer to the same object, when we use addition assignment
# ! <code>+=</code> on <code>b</code>, it changes both <code>a</code> and
# ! <code>b</code>


# > https://pynative.com/python-operators-and-expression-quiz/

