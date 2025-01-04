# # 1==========================================================================


# ? In Python, a dictionary is an implementation of:


# - Linked List
# - Dynamic array
# + Hash Table
# - Red Black Tree


# # 2==========================================================================


# ? What methods should a dict key have?


# - __gt__
# - __le__
# + __hash__
# - __contains__
# + __eq__


# # 3==========================================================================


# ? What is the algorithmic complexity of retrieving a value by
# ? key in a dictionary?


# - O(n)
# - O(n^2)
# - O(log n)
# - O(n log n)
# + O(1)


# # 4==========================================================================


# ? What will the following code output?


fruits = {"apple": 1, "banana": 2}
count = fruits["orange"]
print(count)


# - 0
# - None
# - ValueError
# - IndexError
# + KeyError

# > https://www.pythontutorial.net/python-basics/python-dictionary/

# # 5==========================================================================


# ? What will the following code output?


fruits = {"apple": 1, "banana": 2}
count = fruits.get("orange")
print(count)


# - 0
# + None
# - ValueError
# - IndexError
# - KeyError

# > https://www.pythontutorial.net/python-basics/python-dictionary/

# # 6==========================================================================


# ? What will the following code output?


fruits = {"apple": 1, "banana": 2}
count = fruits.get("orange", 0)
print(count)


# + 0
# - None
# - ValueError
# - IndexError
# - KeyError

# > https://www.pythontutorial.net/python-basics/python-dictionary/

# # 7==========================================================================


# ? What will the following code output?


fruits = {"apple": 1, "banana": 2, "orange": 3}
if count := fruits.get("orange"):
    print(count)
else:
    print("Orange not fount!")


# - 0
# + 3
# - None
# - ValueError
# - IndexError
# - KeyError
# - Orange not fount!


# > https://www.pythontutorial.net/python-basics/python-dictionary/

# # 8==========================================================================


# ? What will the following code output?


fruits = {"apple": 1, "banana": 2}
if count := fruits.get("orange", 0):
    print(count)
else:
    print("Orange not fount!")


# - 0
# - 3
# - None
# - ValueError
# - IndexError
# - KeyError
# + Orange not fount!

# > https://www.pythontutorial.net/python-basics/python-dictionary/

# # 9==========================================================================


# ? What will the following code output?


fruits = {"apple": 1, "banana": 2, "orange": 0}
if count := fruits.get("orange"):
    print(count)
else:
    print("Orange not fount!")


# - 0
# - 3
# - None
# - ValueError
# - IndexError
# - KeyError
# + Orange not fount!

# > https://www.pythontutorial.net/python-basics/python-dictionary/

# # 10=========================================================================


# ? What will the following code output?


fruits = {"apple": 1, "banana": 2, "orange": 0}
if (count := fruits.get("orange")) is not None:
    print(count)
else:
    print("Orange not fount!")


# + 0
# - None
# - False
# - True
# - ValueError
# - IndexError
# - KeyError
# - Orange not fount!

# > https://www.pythontutorial.net/python-basics/python-dictionary/

# # 11=========================================================================


# ? What will the following code output?


fruits = {"apple": 1, "banana": 2, "orange": 0}
if count := fruits.get("orange") is not None:
    print(count)
else:
    print("Orange not fount!")


# - 0
# - None
# - False
# + True
# - ValueError
# - IndexError
# - KeyError
# - Orange not fount!

# > https://www.pythontutorial.net/python-basics/python-dictionary/

# # 12=========================================================================


# ? What will the following code output?


fruits = {"apple": 1, "banana": 2}
count = fruits.setdefault("orange", 3)
print(count)


# - 0
# + 3
# - None
# - False
# - True
# - ValueError
# - IndexError
# - KeyError

# > https://www.pythontutorial.net/python-basics/python-dictionary/

# # 13=========================================================================


# ? What will the following code output?


fruits = {"apple": 1, "banana": 2, "orange": 3}
count = fruits.setdefault("orange", 5)
print(count)


# - 0
# + 3
# - 5
# - None
# - ValueError
# - IndexError
# - KeyError

# > https://www.pythontutorial.net/python-basics/python-dictionary/

# # 14=========================================================================


# ? What will the following code output?


fruits = {"apple": 1, "banana": 2}
count = fruits.setdefault("orange", 5)
print(count)


# - 0
# - 3
# + 5
# - None
# - ValueError
# - IndexError
# - KeyError

# > https://www.pythontutorial.net/python-basics/python-dictionary/

# # 15=========================================================================


# ? What will the following code output?


boxes = {}

box1 = boxes.setdefault("box1", [])
box1.append("apple")
box1.append("banana")

box2 = boxes.setdefault("box2", [])

print(boxes["box1"], boxes["box2"])


# - [ ] [ ]
# - [ ] None
# + ['apple', 'banana'] [ ]
# - ['apple', 'banana'] None
# - ValueError
# - IndexError
# - KeyError

# > https://www.pythontutorial.net/python-basics/python-dictionary/