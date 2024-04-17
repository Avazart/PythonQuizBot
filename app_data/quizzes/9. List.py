# # 1==========================================================================


# ? What is the output of the following list function?


sample_list = [10, 20, 30, 40, 50]
sample_list.append(60)
print(sample_list)

sample_list.append(60)
print(sample_list)


# - [10, 20, 30, 40, 50, 60] [10, 20, 30, 40, 50, 60]
# + [10, 20, 30, 40, 50, 60] [10, 20, 30, 40, 50, 60, 60]


# ! <strong>Explanation:</strong> The <code>append()</code> method is used to
# / add an item at the end of a list. Also, the list allows duplicate items.


# > https://pynative.com/python-list-quiz/


# # 2==========================================================================


# ? What is the output of the following list operation


sample_list = [10, 20, 30, 40, 50]
print(sample_list[-2])
print(sample_list[-4:-1])


# + 40 [20, 30, 40]
# - IndexError: list index out of range


# ! <strong>Explanation:</strong> Use the range of negative indexes to search
# / from the end of the list.


# > https://pynative.com/python-list-quiz/


# # 3==========================================================================


# ? What is the output of the following list function?


sample_list = [10, 20, 30, 40, 50]
sample_list.pop()
print(sample_list)

sample_list.pop(2)
print(sample_list)


# - [20, 30, 40, 50] [10, 20, 40]
# - [10, 20, 30, 40] [10, 20, 30, 50]
# + [10, 20, 30, 40] [10, 20, 40]


# ! <strong>Explanation:</strong> The list's <code>pop()</code> function is
# / used to remove the item present at the specified index, (or the last item
# / if the index is not specified).


# > https://pynative.com/python-list-quiz/


# # 4==========================================================================


# ? Select all the correct options to join two lists in Python


list_one = ["a", "b", "c", "d"]
list_two = ["e", "f", "g"]


# + new_list = list_one + list_two
# - new_list = extend(list_one, list_two)
# + new_list = list_one.extend(list_two)
# - new_list.extend(list_one, list_two)


# ! <strong>Explanation:</strong>


# > https://pynative.com/python-list-quiz/


# # 5==========================================================================


# ? What is the output of the following


l = [None] * 10
print(len(l))


# + 10
# - 0
# - Syntax Error


# > https://pynative.com/python-list-quiz/


# # 6==========================================================================


# ? What is the output of the following


lst = [1, 2, 3, 4, 5, 6, 7]
pow2 = [2 * x for x in lst]
print(pow2)


# + [2, 4, 6, 8, 10, 12, 14]
# - [2, 4, 8, 16, 32, 64, 128]


# ! <strong>Explanation:</strong> Here we used list comprehension to multiply
# / each item of a list by 2.


# > https://pynative.com/python-list-quiz/


# # 7==========================================================================


# ? What is the output of the following code


list1 = ["xyz", "zara", "PYnative"]
print(max(list1))


# - PYnative
# + zara


# > https://pynative.com/python-list-quiz/


# # 8==========================================================================


# ? What is the output of the following code


lst = ["PYnative", [4, 8, 12, 16]]
print(lst[0][1])
print(lst[1][3])


# - P 8 Y 16
# - P 12
# + Y 16


# > https://pynative.com/python-list-quiz/


# # 9==========================================================================


# ? In Python, list is mutable


# - False
# + True


# ! <strong>Explanation</strong>: The list collection is ordered and
# / changeable. A mutable object can be changed after it is created. So we can
# / update or remove elements from a <code>list</code> once it is created.


# > https://pynative.com/python-list-quiz/


# # 10=========================================================================


# ? What is the output of the following list operation


lst = [10, 20, 30, 40, 50, 60, 70, 80]
print(lst[2:5])
print(lst[:4])
print(lst[3:])


# - [20, 30, 40, 50] [10, 20, 30, 40] [30, 40, 50, 60, 70, 80]
# + [30, 40, 50] [10, 20, 30, 40] [40, 50, 60, 70, 80]


# ! <strong>Explanation:</strong> Python list collection is ordered and
# / changeable. The list also allows duplicate members. To get a sublist out
# / of the list, we need to specify the range of indexes.&nbsp; To get a
# / sublist, we need to specify where to start and where to end the range.
# / <strong><em>Syntax</em></strong>: <code>list[start:end]</code> If start is
# / missing it takes <code>0</code> as the starting index


# > https://pynative.com/python-list-quiz/


# # 11=========================================================================


# ? What is the output of the following code?


sample_list = [10, 20, 30, 40]
del sample_list[0:6]
print(sample_list)


# + []
# - list index out of range.
# - [10, 20]


# > https://pynative.com/python-list-quiz/


# # 12=========================================================================


# ? What is the output of the following list assignment


lst = [4, 8, 12, 16]
lst[1:4] = [20, 24, 28]
print(lst)


# - [4, 20, 24, 28, 8, 12, 16]
# + [4, 20, 24, 28]


# ! <strong>Explanation</strong>: Use the assignment operator (<code>=</code>)
# / to replace an item or a range of items in a List.


# > https://pynative.com/python-list-quiz/


# # 13=========================================================================


# ? What is the output of the following code


my_list = ["Hello", "Python"]
print("-".join(my_list))


# - HelloPython-
# + Hello-Python
# - -HelloPython


# ! <strong>Explanation</strong>: The <code>join()</code> method will join all
# / items in a list into a string, using a hyphen character as a separator.


# > https://pynative.com/python-list-quiz/


# # 14=========================================================================


# ? What is the output of the following


lst = [5, 10, 15, 25]
print(lst[::-2])


# - [15, 10, 5]
# - [10, 5]
# + [25, 10]


# ! <strong>Explanation</strong>: <code>lst[::-2]</code> Start from the end of
# / the list with step value 2.


# > https://pynative.com/python-list-quiz/


# # 15=========================================================================


# ? Select all the correct options to copy a list


# - new_list = copy(lst)
# + new_list = lst.copy()
# - new_list.copy(lst)
# + new_list = list(lst)


# ! <strong>Explanation</strong>: The <code>copy()</code> method and
# / <code>list()</code> constructor can be used to create a copy of a list.
# / This will create a new list and any changes made in the original list will
# / not reflect in the new list. This is <strong>shallow copying</strong>.


# > https://pynative.com/python-list-quiz/


# # 16=========================================================================


# ? What is the output of the following list comprehension


res_list = [x + y for x in ["Hello ", "Good "] for y in ["Dear", "Bye"]]
print(res_list)


# + ['Hello Dear', 'Hello Bye', 'Good Dear', 'Good Bye']
# - ['Hello Dear', 'Good Dear', 'Hello Bye', 'Good Bye']


# > https://pynative.com/python-list-quiz/

