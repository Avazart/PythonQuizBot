# # 1==========================================================================


# ? What do you use the super() function for in the context of Python’s class
# / inheritance?


# + To call a method from the superclass
# - To check if a class is a subclass of another class
# - To override a method in the superclass


# ! In Python’s class inheritance, you use
# ! <a href="https://realpython.com/python-super/#super-in-single-inheritance"
# / target="_blank">the <code>super()</code> function</a>
# ! to call a method from the superclass. Doing this allows you to use methods
# / of the superclass in the subclass
# ! without repeating code.


# * It can help you to reuse code from the superclass.


# > https://realpython.com/quizzes/python-super/


# # 2==========================================================================


# ? What does the super() function return?


# - The superclass object
# + A temporary object of the superclass
# - The subclass object
# - None


# ! The <code>super()</code> function returns a temporary object of the
# / superclass that allows you to access its methods.
# ! This object is called a <a
# / href="https://realpython.com/python-super/#a-super-deep-dive"
# / target="_blank">proxy object</a>.


# * It’s not <em>quite</em> an object of the superclass, but it acts like one!


# > https://realpython.com/quizzes/python-super/


# # 3==========================================================================


# ? What’s the term for the order in which Python calls methods in a multiple
# / inheritance scenario?


# - Method Execution Sequence
# - Method Invocation Hierarchy
# + Method Resolution Order
# - Method Call Order


# ! The term for the order in which Python calls methods in a multiple
# / inheritance scenario is
# ! <a href="https://realpython.com/python-super/#method-resolution-order"
# / target="_blank">Method Resolution Order (MRO)</a>.


# * Python uses it to <em>resolve</em> which method to call.


# > https://realpython.com/quizzes/python-super/


# # 4==========================================================================


# ? What does the Method Resolution Order (MRO) in Python determine?


# - The order in which you should define methods in a class
# - The order in which Python imports modules
# - The order in which Python executes methods in a class
# + The order in which Python looks for inherited methods


# ! When you call a method on a class that inherits from multiple classes that
# / all implement that method, Python needs to decide which of the available
# / methods to execute.


# * It’s all about inheritance!


# > https://realpython.com/quizzes/python-super/


# # 5==========================================================================


# ? What’s a mixin in Python?


# - A method that mixes the functionality of two other methods.
# - A way to include multiple parent classes in a single child class.
# + A specialized class that you can include in any number of other classes.
# - A class that you can only inherit from but can’t instantiate.


# ! An <a
# / href="https://realpython.com/python-super/#multiple-inheritance-alternatives"
# / target="_blank">alternative to multiple inheritance</a>
# ! in Python is using a <a
# / href="https://realpython.com/inheritance-composition-python/#mixing-features-with-mixin-classes"
# / target="_blank">mixin</a>.
# ! This is a specialized class that you can include in any number of other
# / classes.


# * Mixins allow you to add extra ingredients to the recipe of your class!


# > https://realpython.com/quizzes/python-super/

