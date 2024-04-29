# # 1==========================================================================


# ? Fill in the blanks:
# ? In Python, a sequence is a _____ that has certain characteristics
# ? and supports specific operations.


# + category of data types
# - subclass of list
# - fundamental data type


# ! In Python, a <a href="https://realpython.com/python-sequences/"
# / target="_blank">sequence</a>
# ! is a <strong>category of data types</strong> that has certain
# / characteristics and supports specific operations.


# > https://realpython.com/quizzes/python-sequences/


# # 2==========================================================================


# ? What are the common characteristics of Python sequences?
# ? (Select all that apply.)


# - Elements in a sequence can be accessed by key
# + Sequences are iterable
# - Sequences are mutable
# - Sequences have a fixed size
# + Elements in a sequence can be accessed by index
# + Sequences have a length


# ! Python sequences have three common characteristics:


# * Think about what you can do with lists, tuples, and strings.


# > https://realpython.com/quizzes/python-sequences/


# # 3==========================================================================


# ? Fill in the blanks:
# ? Not all Python sequences support _____.


# - iteration
# - indexing
# + slicing


# ! While most sequences in Python support
# ! <a
# / href="https://realpython.com/python-sequences/#slicing-in-python-sequences"
# / target="_blank">slicing</a>,
# ! not all of them do.
# ! For example, the <code>deque</code> data type in Python’s
# / <code>collections</code> module
# ! is a sequence that doesn’t support slicing:


# > https://realpython.com/quizzes/python-sequences/


# # 4==========================================================================


# ? What happens when you try to concatenate a list and a tuple in Python?


# - It creates a new list of tuples
# + It raises a TypeError
# - It creates a new list
# - It creates a new tuple


# ! In Python, you generally can’t concatenate sequences of different types.
# ! If you try to add a list and a tuple, Python raises a
# / <code>TypeError</code>:


# * Not all sequences play well together.


# > https://realpython.com/quizzes/python-sequences/


# # 5==========================================================================


# ? How do you make a class iterable in Python?


# + Define the .__iter__() special method in the class
# - Define the .__index__() special method in the class
# - Define the .__next__() special method in the class


# ! To <a
# / href="https://realpython.com/python-sequences/#making-the-class-iterable-using-__iter__"
# / target="_blank">make a class iterable</a>,
# ! you need to define the <code>.__iter__()</code> special method in the
# / class.
# ! This method must return an iterator, which Python uses in its iteration
# / protocol.


# * Your class needs to follow Python’s iteration protocol.


# > https://realpython.com/quizzes/python-sequences/


# # 6==========================================================================


# ? What happens when you try to create an instance of a class that inherits
# / from the Sequence abstract base class, but doesn’t implement the
# / __getitem__() and __len__() methods?


# - It creates an instance, but you can’t iterate over it, index it, or get its length.
# - It creates an instance without any issues.
# + It raises a TypeError.


# ! When you try to create an instance of a class
# ! that inherits from the <code>Sequence</code> abstract base class,
# ! but doesn’t implement <code>.__getitem__()</code> and
# / <code>.__len__()</code>,
# ! then Python raises a <code>TypeError</code>:


# * The <code>Sequence</code> abstract base class has some requirements.


# > https://realpython.com/quizzes/python-sequences/


# # 7==========================================================================


# ? When you inherit from collections.abc.MutableSequence, you get several
# / methods for free.
# ? Which of the following methods are not included by default?
# ? (Select all that apply.)


# - .__iadd__()
# - .pop()
# + .__len__()
# + .__getitem__()
# - .remove()
# + .insert()
# + .__setitem__()
# + .__delitem__()
# - .append()


# ! When you inherit from <code>collections.abc.MutableSequence</code>,
# ! you get several methods for free, including:


# * The <code>collections.abc.MutableSequence</code> abstract base class
# / provides a lot of methods,
# * but not all of them. You need to implement some methods in the inheriting
# / class.


# > https://realpython.com/quizzes/python-sequences/

