# # 1==========================================================================


# ? Choose the correct function to get the character from ASCII number


# - ascii(number)
# - char(number)
# + chr(number)


# ! <strong>Explanation</strong>: The <code>chr()</code> function is used to
# / get the character from the ASCII number. Example:
# / <code>print(chr(112))</code> will print <code>p</code>


# > https://pynative.com/python-string-quiz/


# # 2==========================================================================


# ? Which method should I use to convert String "welcome to the beautiful
# / world of python" to "Welcome To The Beautiful World Of Python"


# - capitalize()
# + title()


# ! <strong>Explanation</strong>: The <code>title()</code> function
# / capitalize() the first letter of every word of the String.


# > https://pynative.com/python-string-quiz/


# # 3==========================================================================


# ? Select the correct output of the following string operations


my_string = "pynative"
string_list = ["abc", "pynative", "xyz"]

print(string_list[1] == my_string, end=" ")
print(string_list[1] is my_string, end=" ")


# - True False
# + True True


# ! <strong>Explanation:</strong> See: <a
# / href="https://pynative.com/python-operators/">Operators in Python</a>


# > https://pynative.com/python-string-quiz/


# # 4==========================================================================


# ? Guess the correct output of the following code?


s = "PYnative"
print(s[1:4], s[:5], s[4:], s[0:-1], s[:-1])


# - PYn PYnat ive PYnativ vitanYP
# - Yna PYnat tive PYnativ vitanYP
# + Yna PYnat tive PYnativ PYnativ


# ! <strong>Explanation</strong>: We can
# / use a slice operator <code>[]</code> to get a substring.
# / Syntax: <code>s[start:end]</code>


# > https://pynative.com/python-string-quiz/


# # 5==========================================================================


# ? What is the output of the following code


s1 = "My salary is 7000"
s2 = "7000"

print(s1.isdigit(), s2.isdigit())


# + False True
# - False False
# - True False


# > https://pynative.com/python-string-quiz/


# # 6==========================================================================


# ? Guess the correct output of the following String operations


s = "Welcome"

print(s * 2)


# + WelcomeWelcome
# - TypeError unsupported operand type(s)


# ! <strong>Explanation</strong>: In the case of a string, the <code>*</code>
# / operator is used to repeat a string. For example, <code>"PYnative" *
# / 4</code> will display “PYnative” 4 times.


# > https://pynative.com/python-string-quiz/


# # 7==========================================================================


# ? Python does not support a character type; a single character is treated as
# / strings of length one.


# - False
# + True


# > https://pynative.com/python-string-quiz/


# # 8==========================================================================


# ? What is the output of the following string comparison


print("John" > "Jhon")
print("Emma" < "Emm")


# + True False
# - False False


# > https://pynative.com/python-string-quiz/


# # 9==========================================================================


# ? What is the output of the following string operations


s = "My salary is 7000"
print(s.isalnum())


# - True
# + False


# ! <strong>Explanation</strong>: Space is not an alpha numberic character.


# > https://pynative.com/python-string-quiz/


# # 10=========================================================================


# ? Strings are immutable in Python, which means a string cannot be modified.


# + True
# - False


# ! <strong>Explanation</strong>: Yes, strings are immutable in Python. You
# / cannot modify the string once created. If you change a string, Python
# / creates a new string with the updated value and assigns it to the
# / variable. For example: Output: Earlier <code>s</code> was pointing to
# / memory address “140560663354704” now, it's pointing to “140560640152496”
# / which means Python created a new string after you updated it.


# > https://pynative.com/python-string-quiz/


# # 11=========================================================================


# ? Select the correct output of the following String operations


s1 = "pynative"
s2 = "pynative"
print(s1 == s2, s1 is s2)


# - False False
# + True True
# - True False
# - False True


# > https://pynative.com/python-string-quiz/


# # 12=========================================================================


# ? Choose the correct function to get the ASCII code of a character


# - char('char')
# + ord('char')
# - ascii('char')


# ! <strong>Explanation</strong>: The <code>ord()</code> function is used to
# / get the ASCII code of the character. Example: <code>print(ord('p'))</code>
# / will print 112


# > https://pynative.com/python-string-quiz/


# # 13=========================================================================


# ? Select the correct output of the following String operations


s = "my name is James bond"
print(s.capitalize())


# - My Name Is James Bond
# - TypeError: unsupported operand type(s) for * or pow(): 'str' and 'int'
# + My name is james bond


# ! <strong>Explanation</strong>: The <code>capitalize()</code> function
# / converts only a first character to a capital letter and all remaining
# / characters to lowercase.


# > https://pynative.com/python-string-quiz/


# # 14=========================================================================


# ? Select the correct output of the following String operations


s = "my isname isisis jameis isis bond"
sub = "is"
print(s.count(sub, 4))


# - 5
# + 6
# - 7


# > https://pynative.com/python-string-quiz/


# # 15=========================================================================


# ? Select the correct output of the following String operations


s = "Welcome"
print(s[:6] + " PYnative")


# - Welcome PYnative
# - WelcomPYnative
# + Welcom PYnative
# - WelcomePYnative


# ! <strong>Explanation</strong>: Syntax: <code>str[start:end]</code> If start
# / is missing it takes <code>0</code> as the starting index.


# > https://pynative.com/python-string-quiz/
