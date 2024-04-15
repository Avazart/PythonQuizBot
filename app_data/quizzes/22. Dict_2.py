# # iteration, pop

# # 1==========================================================================

# ? What will the following cofruitse output?

fruits = {"apple": 1, "banana": 2}
for x, y in fruits:
    print(x, y)
    break

# - apple 1
# - 1 apple
# - SyntaxError
# + ValueError
# - KeyError

# # 2==========================================================================

# ? What will the following cofruitse output?

fruits = {"apple": 1, "banana": 2}
for x in fruits:
    print(x)
    break

# - 1
# + apple
# - SyntaxError
# - ValueError
# - KeyError

# # 3==========================================================================

# ? What will the following cofruitse output?

fruits = {"apple": 1, "banana": 2}
for x in fruits.keys():
    print(x)
    break

# - 1
# + apple
# - SyntaxError
# - ValueError
# - KeyError

# # 4==========================================================================

# ? What will the following cofruitse output?

fruits = {"apple": 1, "banana": 2}
for x in fruits.values():
    print(x)
    break

# + 1
# - apple
# - SyntaxError
# - ValueError
# - KeyError

# # 5==========================================================================

# ? What will the following cofruitse output?

fruits = {"apple": 1, "banana": 2}
for p in fruits.items():
    print(p)
    break

# - 'apple', 1
# + ('apple', 1)
# - (1, 'apple')
# - SyntaxError
# - ValueError
# - KeyError

# # 6==========================================================================

# ? What will the following cofruitse output?

fruits = {"apple": 1, "banana": 2}
for x, y in fruits.items():
    print(x, y)
    break

# + apple 1
# - 1 apple
# - SyntaxError
# - ValueError
# - KeyError

# # 7==========================================================================

# ? What will the following cofruitse output?
lst = [(111, "apple"), (2, "banana"), (111, "orange")]

fruits = {}
for k, v in lst:
    fruits[k] = v

print(list(fruits.values()))

# - [111, 2, 111]
# - ['apple', 'banana', 'orange']
# + ['orange', 'banana']
# - SyntaxError
# - ValueError
# - KeyError

# # 8==========================================================================

# ? What will the following cofruitse output?

lst = [(111, "apple"), (111, "banana"), (2, "apple")]
fruits = dict(lst)

print(list(fruits.keys()))

# - ['orange', 'banana', 'orange']
# - [111, 111, 2]
# + [111, 2]
# - SyntaxError
# - ValueError
# - KeyError

# # 9==========================================================================

# ? What will the following cofruitse output?

tpl = "apple", "banana"
fruits = {e: i for i, e in enumerate(reversed(tpl), 1)}

print(fruits)

# - { 'banana': 1, 'apple': 0 }
# - { 'banana': 0, 'apple': 1 }
# - { 'apple': 1, 'banana': 2 }
# + { 'banana': 1, 'apple': 2 }
# - SyntaxError
# - ValueError


# # 10=========================================================================

# ? What will the following cofruitse output?

d1 = {"apple": 1, "banana": 2}
d2 = {"apple": 4, "orange": 3}

d1.update(d2)

print(d1)

# - {'apple': 1, 'banana': 2}
# - {'apple': 1, 'banana': 2, 'orange': 3}
# + {'apple': 4, 'banana': 2, 'orange': 3}
# - {'apple': 4, 'orange': 3}
# - AttributeError


# # 11=========================================================================

# ? What will the following cofruitse output?

d1 = {"apple": 1, "banana": 2}
d2 = {"apple": 4, "orange": 3}

d = d1 | d2

print(d)

# - {'apple': 1, 'banana': 2}
# + {'apple': 4, 'banana': 2, 'orange': 3}
# - {'apple': 1, 'banana': 2, 'orange': 3}
# - {'apple': 4, 'orange': 3}
# - AttributeError

# # 12=========================================================================

# ? What will the following cofruitse output?

fruits = {"apple": 1, "banana": 2, "orange": 3}

del fruits["apple"]

print(fruits)

# - {'apple': 1, 'banana': 2, 'orange': 3}
# + {'banana': 2, 'orange': 3}
# - SyntaxError
# - KeyError
# - AttributeError

# # 13=========================================================================

# ? What will the following cofruitse output?

fruits = {"apple": 1, "banana": 2}
x = fruits.pop("banana")
print(x, fruits)

# - None {'apple': 1, 'banana': 2}
# - None {'apple': 1}
# + 2 {'apple': 1}
# - banana {'apple': 1}
# - SyntaxError
# - KeyError
# - AttributeError


# # 14=========================================================================

# ? What will the following cofruitse output?

fruits = {"apple": 1, "orange": 3}
x = fruits.pop("banana")
print(x, fruits)

# - None {'apple': 1, 'orange': 3}
# - 0 {'apple': 1, 'orange': 3}
# - banana {'apple': 1}
# - SyntaxError
# + KeyError
# - AttributeError

# # 15=========================================================================

# ? What will the following cofruitse output?

fruits = {"apple": 1, "orange": 3}
x = fruits.pop("banana", 2)
print(x, fruits)

# - None {'apple': 1, 'orange': 3}
# + 2 {'apple': 1, 'orange': 3}
# - banana {'apple': 1}
# - SyntaxError
# - KeyError
# - AttributeError

# # 16=========================================================================

# ? What will the following cofruitse output?

fruits = {"apple": 1, "banana": 2}
item = fruits.popitem()

print(item, fruits)

# - 1 {'banana': 2}
# - 2 {'apple': 1}
# - None {'apple': 1}
# + ('banana', 2) {'apple': 1}
# - ('apple', 1) {'banana': 2}
# - SyntaxError
# - KeyError
# - AttributeError
