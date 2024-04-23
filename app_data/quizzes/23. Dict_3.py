# # 1==========================================================================


# ? What is the output of the following code?


tpl = "apple", "banana"
fruits = {}.fromkeys(tpl)
print(fruits)


# - {'apple', 'banana'}
# + {'apple': None, 'banana': None}
# - {'apple': 0, 'banana': 0}
# - SyntaxError
# - KeyError
# - AttributeError

# > https://docs.python.org/3/library/stdtypes.html#dict.fromkeys

# # 2==========================================================================


# ? What is the output of the following code?


tpl = "apple", "banana"

fruits = {}.fromkeys(tpl, 0)

print(fruits)


# - {'apple', 'banana'}
# - {'apple': None, 'banana': None}
# + {'apple': 0, 'banana': 0}
# - SyntaxError
# - AttributeError

# > https://docs.python.org/3/library/stdtypes.html#dict.fromkeys


# # 3==========================================================================


# ? What is the output of the following code?


lst = [3, 1, 2, 1, 2, 3]

fruits = {}.fromkeys(lst)

print(list(fruits))


# - [1, 2, 3]
# + [3, 1, 2]
# - {1, 2, 3}
# - SyntaxError
# - AttributeError

# > https://docs.python.org/3/library/stdtypes.html#dict.fromkeys

# # 4==========================================================================


# ? What is the output of the following code?


d1 = {"apple": 1}

d2 = d1
d1["banana"] = 2

print(d1 is d2, d1 == d2)


# + True True
# - False True
# - True False
# - False False
# - SyntaxError
# - ValueError
# - KeyError

# > https://www.pythontutorial.net/advanced-python/python-is-operator/
# > https://www.programiz.com/python-programming/shallow-deep-copy

# # 5==========================================================================


# ? What is the output of the following code?


box = ["apple", "banana"]
d1 = {"box": box}

d2 = d1.copy()  #  d2 = dict(d1)
d1["box"].append("orange")

print(d1 is d2, d1 == d2)


# - True True
# + False True
# - True False
# - False False
# - SyntaxError
# - ValueError
# - KeyError

# > https://www.pythontutorial.net/advanced-python/python-is-operator/
# > https://docs.python.org/3/library/copy.html
# > https://www.programiz.com/python-programming/shallow-deep-copy

# # 6==========================================================================


# ? What is the output of the following code?


from copy import deepcopy

box = ["apple", "banana"]
d1 = {"box": box}

d2 = deepcopy(d1)
d1["box"].append("orange")

print(d1 is d2, d1 == d2)


# - True True
# - False True
# - True False
# + False False
# - SyntaxError
# - ValueError
# - KeyError

# > https://www.pythontutorial.net/advanced-python/python-is-operator/
# > https://docs.python.org/3/library/copy.html
# > https://www.programiz.com/python-programming/shallow-deep-copy