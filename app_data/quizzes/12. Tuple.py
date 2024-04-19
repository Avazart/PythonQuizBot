# # 1==========================================================================


# ? Choose the correct way to access value 20 from the following tuple


tpl = ("Orange", [10, 20, 30], (5, 15, 25))


# - tpl[1:2][1]
# - tpl[1:2](1)
# - tpl[1:2][1]
# + tpl[1][1]


# > https://pynative.com/python-tuple-quiz/


# # 2==========================================================================


# ? Select which is true for Python tuple


# + A tuple maintains the order of items
# - A tuple is unordered
# + We cannot change the tuple once created
# - We can change the tuple once created


# > https://pynative.com/python-tuple-quiz/


# # 3==========================================================================


# ? What is the type of the following variable


tpl = "Orange"
print(type(tpl))


# - list
# - tuple
# - array
# + str


# ! <strong>Explanation</strong>: To create a tuple with a single item, you
# / need to add a comma after the item. Otherwise, Python will not recognize
# / the variable as a tuple, and it will treat it as a string type. For
# / <strong>example</strong>: <strong>Output</strong>:


# > https://pynative.com/python-tuple-quiz/


# # 4==========================================================================


# ? What is the output of the following


tpl = (10, 20, 30, 40, 50, 60, 70, 80)
print(tpl[2:5], tpl[:4], tpl[3:])


# + (30, 40, 50) (10, 20, 30, 40) (40, 50, 60, 70, 80)
# - (20, 30, 40, 50) (10, 20, 30, 40) (30, 40, 50, 60, 70, 80)


# ! <strong>Explanation</strong>: To get a sub tuple out of the tuple, we need
# / to specify the range of indexes.&nbsp; We need to specify where to start
# / and where to end the range. <em><strong>Syntax</strong></em>:
# / <code>tuple[start:end]</code> If the start is missing it takes 0 as the
# / starting index.


# > https://pynative.com/python-tuple-quiz/


# # 5==========================================================================


# ? What is the output of the following


tuple1 = (1120, "a")
print(max(tuple1))


# + TypeError
# - 1120
# - 'a'


# ! <strong>Explanation</strong>: TypeError: <code>'&gt;'</code> not supported
# / between instances of 'str' and 'int'


# > https://pynative.com/python-tuple-quiz/


# # 6==========================================================================


# ? What is the output of the following tuple operation


tpl = (100, 200, 300, 400, 500)
tpl.pop(2)
print(tpl)


# - (100, 200, 400, 500)
# - (100, 300, 400, 500)
# + AttributeError


# ! <strong>Explanation</strong>: A tuple is immutable. Once a tuple is
# / created, you cannot remove its items, but you can delete the tuple
# / completely. If you try to remove the item from the tuple, you will receive
# / an <code>AttributeError: 'tuple' object has no attribute 'pop'</code>.


# > https://pynative.com/python-tuple-quiz/


# # 7==========================================================================


# ? What is the output of the following


tpl = "Yellow", 20, "Red"
a, b, c = tpl
print(a)


# - ('Yellow', 20, 'Red')
# - TyepeError
# + Yellow


# ! <strong>Explanation</strong>: The tuple unpacking is also possible


# > https://pynative.com/python-tuple-quiz/


# # 8==========================================================================


# ? What is the output of the following tuple operation


tpl = (100,)
print(tpl * 2)


# - TypeError
# + (100, 100)
# - (200)


# ! <strong>Explanation</strong>: We can use <code>*</code> operator to repeat
# / the tuple values <code>n</code> number of times. For example:


# > https://pynative.com/python-tuple-quiz/


# # 9==========================================================================


# ? What is the output of the following code


tpl = (100, 200, 300, 400, 500)
print(tpl[-2])
print(tpl[-4:-1])


# - IndexError: tuple index out of range
# + 400 (200, 300, 400)


# ! <strong>Explanation</strong>: Use the range of negative indexes to start a
# / search from the end of the tuple.


# > https://pynative.com/python-tuple-quiz/


# # 10=========================================================================


# ? Select true statements regarding the Python tuple


# - We can remove the item from tuple but we cannot update items of the tuple
# - We cannot delete the tuple
# + We cannot remove the items from the tuple
# + We cannot update items of the tuple.


# ! <strong>Explanation</strong>: A tuple is immutable. The following action
# / is not valid for tuples


# > https://pynative.com/python-tuple-quiz/


# # 11=========================================================================


# ? A Python tuple can also be created without using parentheses


# - False
# + True


# ! <strong>Explanation</strong>: A tuple can also be created without using
# / parentheses. It is called tuple packing. For example:


# > https://pynative.com/python-tuple-quiz/


# # 12=========================================================================


# ? What is the output of the following code


tpl = (100, 200, 300, 400, 500)
tpl[1] = 800
print(tpl)


# + TypeError
# - (100, 800, 200, 300, 400, 500)
# - (800, 100, 200, 300, 400, 500)


# ! <strong>Explanation</strong>: <span data-preserver-spaces="true">A tuple
# / is&nbsp;</span><strong><span
# / data-preserver-spaces="true">immutable.&nbsp;</span></strong><span
# / data-preserver-spaces="true">Once a tuple is created, you cannot change
# / its values. If you try to change its value, you will receive a&nbsp;
# / </span><code>TypeError: 'tuple' object does not support item
# / assignment</code>


# > https://pynative.com/python-tuple-quiz/
