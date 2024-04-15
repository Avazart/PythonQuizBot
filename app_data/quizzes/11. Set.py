# # 1==========================================================================

# ? The <code>symmetric_difference()</code> method returns a set that contains
# ? all items from both sets, but not the items that are present in both sets.

# - False
# + True

# # ! <strong>Example</strong>: <strong>Output</strong>:

# > https://pynative.com/python-set-quiz/


# # 2==========================================================================

# ? What is the output of the following

sample_set = {"Yellow", "Orange", "Black"}
sample_set.discard("Blue")
print(sample_set)

# + {'Yellow', 'Orange', 'Black'}
# - KeyError: 'Blue'

# # ! <strong>Explanation</strong>: If the item to remove does not exist in the set, the <code>discard()</code> method will&nbsp;<strong>NOT</strong> raise an error. If we use <code>remove()</code> method to perform the same operation, we will receive a <code>keyError</code>.

# > https://pynative.com/python-set-quiz/


# # 3==========================================================================

# ? What is the output of the following code

sample_set = {1, "PYnative", ("abc", "xyz"), True}
print(sample_set)

# - TypeError
# - {'PYnative', 1, ('abc', 'xyz'), True}
# + {'PYnative', 1, ('abc', 'xyz')}

# # ! <strong>Explanation</strong>: Set already has <strong>1</strong> as item <strong><code>True</code> evaluates to 1</strong>. As you know set doesn't allow duplicate element

# > https://pynative.com/python-set-quiz/


# # 4==========================================================================

# ? What is the output of the following set operation

set1 = {"Yellow", "Orange", "Black"}
set2 = {"Orange", "Blue", "Pink"}

set3 = set2.difference(set1)
print(set3)

# - {'Yellow', ”Black', 'Pink', 'Blue'}
# + {'Pink', 'Blue'}
# - {'Yellow', ”Black'}

# # ! <strong>Explanation</strong>: The <code>difference()</code> method returns a set that contains the difference between two sets.<br> Here <code>set3 = set2.difference(set1)</code> so the returned set contains items that exist only in the first set, and not in both sets.

# > https://pynative.com/python-set-quiz/


# # 5==========================================================================

# ? Select all which is true for Python set

# + Sets are unordered set doesn't allow duplicate sets are written with curly brackets {}
# - Sets are unordered
# - set doesn't allow duplicate
# - sets are written with curly brackets {}
# - set object does support indexing set is mutable
# - set object does support indexing
# - set is mutable

# # ! <strong>Explanation</strong>:

# > https://pynative.com/python-set-quiz/


# # 6==========================================================================

# ? The isdisjoint() method returns True if none of the items are present in both sets, otherwise, it returns False.

# + True
# - False

# > https://pynative.com/python-set-quiz/


# # 7==========================================================================

# ? The union() method returns a new set with all items from both sets by removing duplicates

# + True
# - False

# > https://pynative.com/python-set-quiz/


# # 8==========================================================================

# ? What is the output of the following

sample_set = {"Yellow", "Orange", "Black"}
sample_set.add("Blue")
sample_set.add("Orange")
print(sample_set)

# - {'Blue', 'Orange', 'Yellow', 'Orange', 'Black'}
# + {'Blue', 'Orange', 'Yellow', 'Black'}

# # ! <strong>Explanation</strong>: Python <code>set</code> doesn't allow duplicate items.

# > https://pynative.com/python-set-quiz/


# # 9==========================================================================

# ? What is the output of the following set operation.

set1 = {"Yellow", "Orange", "Black"}
set2 = {"Orange", "Blue", "Pink"}

set1.difference_update(set2)
print(set1)

# + {'Black', 'Yellow'}
# - {'Yellow', 'Orange', 'Black', 'Blue', 'Pink'}

# # ! <strong>Explanation</strong>: The <code>difference_update()</code> method removes the items that exist in both sets. Here <code>set1.difference_update(set2)</code> removed the unwanted items from the original set1.

# > https://pynative.com/python-set-quiz/


# # 10=========================================================================

# ? What is the output of the following code

sample_set = {"Yellow", "Orange", "Black"}
print(sample_set[1])

# - Yellow
# + Syntax Error
# - Orange

# # ! <strong>Explanation</strong>: We cannot access items in a set by referring to an index because the 'set' object does support indexing (the set is unordered). if you try to access items using the index, you will get TypeError: 'set' object does not support indexing. Use a <a href="https://pynative.com/python-for-loop/">for loop</a> to access set items.

# > https://pynative.com/python-set-quiz/


# # 11=========================================================================

# ? What is the output of the following code

sample_set = {1, "PYnative", ["abc", "xyz"], True}
print(sample_set)

# - {1, 'PYnative', ['abc', 'xyz']}
# - {1, 'PYnative', ['abc', 'xyz'], True}
# + TypeError

# # ! <strong>Explanation</strong>: If you try to execute the above code you will get a <code>TypeError: unhashable type: 'list'</code>

# > https://pynative.com/python-set-quiz/


# # 12=========================================================================

# ? Select all the correct ways to copy two sets

# + set2 = set1.copy() set2 = set(set1) set2.update(set1)
# - set2 = set1.copy()
# - set2 = set(set1)
# - set2.update(set1)
# - set2 = set1
# - set2 = set1

# # ! <strong>Explanation</strong>: When you set&nbsp;<code>set2= set11</code>, you are making them refer to the same dict object, so when you modify one of them, all references associated with that object reflect the current state of the object. So don't use the assignment operator to copy the set instead use the&nbsp;<code>copy()</code>&nbsp;method or&nbsp;<code>set()</code> constructor.

# > https://pynative.com/python-set-quiz/


# # 13=========================================================================

# ? What is the output of the following

set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 10, 30, 40, 80, 20, 50}

print(set1.issubset(set2))
print(set2.issuperset(set1))

# - False False
# + True True

# > https://pynative.com/python-set-quiz/


# # 14=========================================================================

# ? Select all the correct options to remove “Orange” from the set.

sample_set = {"Yellow", "Orange", "Black"}

# - sample_set.pop("Orange")
# + sample_set.discard("Orange")
# - del sample_set ["Orange"]

# # ! <strong>Explanation</strong>: The <code>remove()</code> and <code>discard()</code> method removes the specified item from a set.

# > https://pynative.com/python-set-quiz/


# # 15=========================================================================

# ? What is the output of the following set operation

sample_set = {"Yellow", "Orange", "Black"}
sample_set.update(["Blue", "Green", "Red"])
print(sample_set)

# + {'Yellow', 'Orange', 'Red', 'Black', 'Green', 'Blue'}
# - {'Yellow', 'Orange', 'Black', [“Blue”, “Green”, “Red”]}
# - TypeError: update() doesn't allow list as a argument.

# # ! <strong>Explanation</strong>: We can update multiple items using the <code>update()</code> method.

# > https://pynative.com/python-set-quiz/


# # 16=========================================================================

# ? What is the output of the following union operation

set1 = {10, 20, 30, 40}
set2 = {50, 20, "10", 60}

set3 = set1.union(set2)
print(set3)

# - {40, 10, 50, 20, 60, 30}
# - {40, '10', 50, 20, 60, 30}
# + {40, 10, '10', 50, 20, 60, 30}
# - SynatxError: Different types cannot be used with sets

# # ! <strong>Explanation</strong>: The <code>union()</code> method returns a new set with all items from both sets by removing duplicates

# > https://pynative.com/python-set-quiz/
