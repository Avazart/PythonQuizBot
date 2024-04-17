# # 1==========================================================================


# ? What is the output of the following number conversion


z = complex(1.25)


# + (1.25+0j)
# - Value Error: Missing an imaginary part of a complex number


# ! <strong>Explanation:</strong> The <code>complex(1.25)</code>&nbsp; will
# / convert 1.25 to the real part and the imaginary part is zero.


# > https://pynative.com/python-numbers-quiz/


# # 2==========================================================================


# ? Select correct float numbers


# + a = 10.1256; b = -10.5
# + c = 42e3;    d = -68.7e100


# ! <strong>Explanation:</strong> We use float to denotes scientific numbers
# / with an “e” to indicate the power of 10.


# > https://pynative.com/python-numbers-quiz/


# # 3==========================================================================


# ? What is the type of the following variable


x = -5j


# - int
# + complex
# - real
# - imaginary


# > https://pynative.com/python-numbers-quiz/


# # 4==========================================================================


# ? What is the output of


print(abs(-45.300))


# + 45.3
# - -45.3
# - -45.300
# - 45.300


# ! <strong>Explanation:</strong> <code>abs(x)</code> method returns the
# / absolute value of x


# > https://pynative.com/python-numbers-quiz/


# # 5==========================================================================


# ? Select which is right for Python integers


# + An integer is a whole number that can be positive or negative
# + In Python 3, Integers have unlimited precision


# > https://pynative.com/python-numbers-quiz/


# # 6==========================================================================


# ? What is the output of the following math function


import math

print(math.ceil(252.4), math.floor(252.4))


# - 252 252
# - 252 253
# + 253 252


# ! <strong>Explanation:</strong>


# > https://pynative.com/python-numbers-quiz/


# # 7==========================================================================


# ? What is the output of the following number comparison function call


# - True
# + False


# ! <strong>Explanation:</strong> <code>(1.1 + 2.2)</code> is not equal to
# / 3.3, It is <code>3.3000000000000003</code>. Use the <code>round()</code>
# / function to compare exact values. For example: <code>print(round(1.1 +
# / 2.2, 10) == round(3.3, 10))</code>


# > https://pynative.com/python-numbers-quiz/


# # 8==========================================================================


# ? What is the output of the following code


print(0b101, 0o10, 0x1F)


# - 101 10 1F
# + 5 8 31
# - Syntax Error: Invalid Token


# ! <strong>Explanation:</strong> We can represent integers in binary, octal
# / and hexadecimal formats.


# > https://pynative.com/python-numbers-quiz/


# # 9==========================================================================


# ? What is the output of the following isinstance() function


from decimal import Decimal
from fractions import Fraction
from numbers import Number

print(isinstance(2.0, Number), end=" ")
print(isinstance(Decimal("2.0"), Number), end=" ")
print(isinstance(Fraction(2, 1), Number), end=" ")
print(isinstance("2", Number), end=" ")


# - True False True True
# - True True True True
# - True False True False
# + True True True False


# > https://pynative.com/python-numbers-quiz/


# # 10=========================================================================


# ? In Python 3, the integer ranges from -2,147,483,648 to +2,147,483,647


# + False
# - True


# ! <strong>Explanation:</strong> In Python 3, Integer can have as many digits
# / as your computer’s memory space allows.


# > https://pynative.com/python-numbers-quiz/


# # 11=========================================================================


# ? What is the output of the following round() function call


print(round(100.2563, 3), end=" ")
print(round(100.000056, 3), end=" ")


# - 100.256 100
# - 100.256 100.000
# + 100.256 100.0


# ! <strong>Explanation</strong>: The <code>round()</code> function returns a
# / rounded version of the specified floating-point number, with the specified
# / number of decimals. The second argument of this function is the number of
# / decimals to use when rounding the number.


# > https://pynative.com/python-numbers-quiz/


# # 12=========================================================================


# ? What is the output of the following code


print(int(2.999))


# - ValueError: invalid literal for int()
# - 3
# + 2


# ! <strong>Explanation:</strong> We can convert float to int using the
# / <code>int()</code> constructor.


# > https://pynative.com/python-numbers-quiz/

