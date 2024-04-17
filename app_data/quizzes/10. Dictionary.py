# # 1==========================================================================


# ? What is the output of the following


sample_dict = dict([("first", 1), ("second", 2), ("third", 3)])
print(sample_dict)


# - [ ('first', 100), ('second', 200), ('third', 300) ]
# - Options: SyntaxError: invalid syntax
# + {'first': 1, 'second': 2, 'third': 3}


# ! <strong>Explanation:</strong> We can create a dictionary by specifying a
# / list of tuples (comma-separated <code>key: value</code> pairs) enclosed in
# / curly braces.


# > https://pynative.com/python-dictionary-quiz/


# # 2==========================================================================


# ? Items are accessed by their position in a dictionary and All the keys in a
# / dictionary must be of the same type.


# - True
# + False


# ! <strong>Explanation</strong>: dictionary elements are accessed by key.
# / Unlike with list indexing, the order of the items in a dictionary plays no
# / role in how the items are accessed.


# > https://pynative.com/python-dictionary-quiz/


# # 3==========================================================================


# ? Select the correct ways to get the value of marks key.


student = {"name": "Emma", "class": 9, "marks": 75}


# - m = student.get(2)
# + m = student.get('marks')
# - m = student[2])
# + m = student['marks'])


# ! <strong>Explanation</strong>:


# > https://pynative.com/python-dictionary-quiz/


# # 4==========================================================================


# ? Select the all correct way to remove the key marks from a dictionary


student = {"name": "Emma", "class": 9, "marks": 75}


# + student.pop("marks")
# + del student["marks"]
# - student.remove("marks")
# - student.popitem("marks")


# ! <strong>Explanation</strong>:


# > https://pynative.com/python-dictionary-quiz/


# # 5==========================================================================


# ? Select correct ways to create an empty dictionary


# + sample_dict = {}
# + sample_dict = dict()
# - sample_dict = dict{}


# > https://pynative.com/python-dictionary-quiz/


# # 6==========================================================================


# ? What is the output of the following code


d1 = {"key1": 1, "key2": 2}
d2 = {"key2": 2, "key1": 1}
print(d1 == d2)


# + True
# - False


# ! <strong>Explanation</strong>: We can use the <code>==</code> and
# / <code>!=</code> <a
# / href="https://pynative.com/python-operators/">operators</a> to check
# / whether the dictionary contains the same items.


# > https://pynative.com/python-dictionary-quiz/


# # 7==========================================================================


# ? Select all correct ways to copy a dictionary in Python


# + d2 = d1.copy()
# + d2 = dict(d1)
# - d2 = d1


# ! <strong>Explanation</strong>: You cannot copy a dictionary just by doing
# / <code>d2 = d1</code>, because: <code>d2</code> will only be
# / a&nbsp;reference&nbsp;to <code>d1</code>, and changes made in
# / <code>d1</code> will be reflected in <code>d2</code>.


# > https://pynative.com/python-dictionary-quiz/


# # 8==========================================================================


# ? Select the correct way to access the value of a history subject


sample_dict = {
    "class": {
        "student": {"name": "Mike", "marks": {"physics": 70, "history": 80}}
    }
}


# + sample_dict['class']['student']['marks']['history']
# - sample_dict['class']['student']['marks'][1]
# - sample_dict['class'][0]['marks']['history']


# > https://pynative.com/python-dictionary-quiz/


# # 9==========================================================================


# ? What is the output of the following dictionary operation


d1 = {"name": "Mike", "salary": 8000}
temp = d1.get("age")
print(temp)


# - KeyError: 'age'
# + None


# ! <strong>Explanation:</strong> The <code>get()</code> method returns a
# / value of the key. If the key is not found, it returns <code>None</code>,
# / instead of throwing a <code>KeyError</code> exception.


# > https://pynative.com/python-dictionary-quiz/


# # 10=========================================================================


# ? In Python, Dictionaries are immutable


# + False
# - True


# ! <strong>Explanation</strong>: &nbsp;


# > https://pynative.com/python-dictionary-quiz/


# # 11=========================================================================


# ? Please select all correct ways to empty the following dictionary


student = {"name": "Emma", "class": 9, "marks": 75}


# - del student
# - del student[0:2]
# + student.clear()


# ! <strong>Explanation</strong>:


# > https://pynative.com/python-dictionary-quiz/


# # 12=========================================================================


# ? Dictionary keys must be immutable


# + True
# - False


# ! <strong>Explanation:</strong> Dictionary keys must be immutable. It means
# / you can use strings, numbers, or <a
# / href="https://pynative.com/python-tuples/">tuples</a> as dictionary keys.
# / And you can't use any mutable object as the key, such as a <a
# / href="https://pynative.com/python-lists/">list</a>.


# > https://pynative.com/python-dictionary-quiz/


# # 13=========================================================================


# ? Select the correct way to print Emma's age.


student = {
    1: {"name": "Emma", "age": "27", "sex": "Female"},
    2: {"name": "Mike", "age": "22", "sex": "Male"},
}


# - student[0][1]
# + student[1]["age"]
# - student[0]["age"]


# > https://pynative.com/python-dictionary-quiz/


# # 14=========================================================================


# ? What is the output of the following dictionary operation


d1 = {"name": "Mike", "salary": 8000}
temp = d1.pop("age")
print(temp)


# + KeyError: 'age'
# - None


# ! <strong>Explanation:</strong> The <code>pop()</code> method removes the
# / item from the dictionary. A KeyError will be thrown if the key doesn't
# / exist.


# > https://pynative.com/python-dictionary-quiz/

