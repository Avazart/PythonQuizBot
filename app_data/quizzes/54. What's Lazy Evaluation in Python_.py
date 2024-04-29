# # 1==========================================================================


# ? What is the main difference between eager and lazy evaluation in Python?


# + Eager evaluation computes values immediately, while lazy evaluation defers computation until necessary.
# - Eager evaluation can handle infinite data structures, while lazy evaluation cannot.
# - Eager evaluation defers error handling, while lazy evaluation handles errors immediately.
# - Lazy evaluation is used for all Python expressions, while eager evaluation is used for all statements.


# ! The main difference between eager and lazy evaluation in Python is that
# ! eager evaluation computes values immediately as the expression is
# / encountered, while
# ! lazy evaluation defers the computation of values until they are actually
# / needed in the program.


# * Consider the timing of when values are computed in each strategy.


# > https://realpython.com/quizzes/python-lazy-evaluation/


# # 2==========================================================================


# ? What is the key difference between a generator expression and a list
# / comprehension?


# + A generator expression is evaluated lazily, while a list comprehension is evaluated eagerly.
# - A generator expression can only create lists, while a list comprehension can create any iterable.
# - A generator expression raises a StopIteration exception, while a list comprehension does not.
# - A generator expression uses curly braces, while a list comprehension uses square brackets.


# ! The key difference between a generator expression and a list comprehension
# / is that
# ! a generator expression is evaluated lazily, while a list comprehension is
# / evaluated eagerly.
# ! This means that a list comprehension generates and stores all the items
# / immediately,
# ! whereas a generator expression generates the items on-the-fly as you
# / iterate over it.


# * The difference lies in their approach to memory and iteration.


# > https://realpython.com/quizzes/python-lazy-evaluation/


# # 3==========================================================================


# ? Which of the following are considered principle tools in functional
# / programming in Python?
# ? (Select all that apply.)


# + reduce() from the functools module
# + filter()
# - list()
# - function()
# + map()
# - iter()


# ! In functional programming, especially in Python, there are three principle
# / tools
# ! that are commonly used to work with data:


# * Each of these functions lets you avoid explicit looping and side effects.


# > https://realpython.com/quizzes/python-lazy-evaluation/

