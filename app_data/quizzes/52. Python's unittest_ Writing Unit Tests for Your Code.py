# # 1==========================================================================


# ? What are the key concepts of Python’s unittest package?
# ? (Select all that apply.)


# + Test fixtures
# - Test debugger
# + Test suite
# - Test compiler
# + Test runner
# + Test case


# ! Python’s <code>unittest</code> package supports several key concepts that
# / facilitate test creation, organization, preparation, and automation:


# > https://realpython.com/quizzes/python-unittest/


# # 2==========================================================================


# ? Fill in the blanks:
# ? To make a test module executable in unittest, you can add the following
# ? code to the end of the module:
# ? Python
# ? if __name__ == "__main__":
# ?  unittest._____()


# - execute
# + main
# - run


# ! To make a test module executable in <code>unittest</code>, you can add the
# / following
# ! code to the end of the module:


# > https://realpython.com/quizzes/python-unittest/


# # 3==========================================================================


# ? What does the @unittest.skipUnless(condition, reason) decorator do in
# / Python’s unittest framework?


# + It skips the decorated test unless the condition is true
# - It runs the decorated test unless the condition is true
# - It skips the decorated test unconditionally
# - It skips the decorated test if the condition is true


# ! The <code>@unittest.skipUnless(condition, reason)</code> decorator in
# / Python’s <code>unittest</code> framework
# ! <a href="https://realpython.com/python-unittest/#skipping-tests"
# / target="_blank">skips the decorated test</a> unless the condition is true.
# ! This is useful for conditionally skipping tests based on dynamic
# / conditions, such as a platform or a Python version.


# * It’s all in the name!


# > https://realpython.com/quizzes/python-unittest/


# # 4==========================================================================


# ? What does the .assertTrue(x) method in unittest check for?


# - That x is equal to True
# + That bool(x) is True
# - That x is not equal to False
# - That x is not None


# ! The <code>.assertTrue(x)</code> method in <code>unittest</code> checks
# / that <code>bool(x)</code> is <code>True</code>.
# ! This is useful when you’re testing Boolean-valued functions, also known as
# / predicate functions.


# * It’s all about the truth!


# > https://realpython.com/quizzes/python-unittest/


# # 5==========================================================================


# ? Which method would you use to compare two dictionary objects in unittest?


# - .assertListEqual(a, b)
# + .assertDictEqual(a, b)
# - .assertSetEqual(a, b)


# ! In <code>unittest</code>, you can use the <a
# / href="https://realpython.com/python-unittest/#comparing-collections"
# / target="_blank"><code>.assertDictEqual(a, b)</code></a>
# ! method to compare two dictionary objects. This method checks if the two
# / dictionaries are equal in terms of their content. Here’s an example:


# * Think about the type of the objects you’re comparing.


# > https://realpython.com/quizzes/python-unittest/


# # 6==========================================================================


# ? How can you check the type of an object in a unittest test?


# - Use a == b or a != b
# - Use type(a) == b or type(a) != b
# - Use a is b or a is not b
# + Use .assertIsInstance(a, b) or .assertNotIsInstance(a, b)


# ! In Python’s <code>unittest</code> package, you can check the type of an
# / object using
# ! the <code>.assertIsInstance(a, b)</code> and <code>.assertNotIsInstance(a,
# / b)</code> methods.
# ! These methods are based on the built-in <code>isinstance()</code>
# / function, which checks
# ! whether the input object <code>a</code> is of a given type <code>b</code>.


# * There’s a dedicated method for this in Python’s <code>unittest</code>
# / module.


# > https://realpython.com/quizzes/python-unittest/


# # 7==========================================================================


# ? How can you test if a function raises a specific exception using Python’s
# / unittest framework?


# - Use the .assertEqual() method
# + Use the .assertRaises() method
# - Use the .assertFalse() method
# - Use the .assertTrue() method


# ! Say that you have the following function:


# * You’re looking for a method that checks if a function raises an exception.


# > https://realpython.com/quizzes/python-unittest/


# # 8==========================================================================


# ? What is a key benefit of using TestSuite in Python’s unittest framework?


# - It allows you to skip writing test cases
# - It runs tests faster than without using TestSuite
# - It automatically generates test cases for you
# + It allows you to create groups of tests and run them selectively


# ! The <code>TestSuite</code> class in Python’s <code>unittest</code>
# / framework allows you to create groups of tests and run them selectively.
# ! This can be particularly useful in complex projects with many features,
# / different testing levels, selective testing, and environment-specific
# / testing.
# ! You can learn more about it in the section on <a
# / href="https://realpython.com/python-unittest/#grouping-your-tests-with-the-testsuite-class"
# / target="_blank">grouping your tests</a>.


# * Think about how you might want to organize your tests.


# > https://realpython.com/quizzes/python-unittest/


# # 9==========================================================================


# ? What does the load_tests() function do in Python’s unittest framework?


# + It’s a hook for customizing test loading and suite creation.
# - It creates a new test case.
# - It runs all tests in a test suite.
# - It loads all tests from a specific test case.


# ! The <code>load_tests()</code> function in Python’s unittest framework is a
# / hook for
# ! <a
# / href="https://realpython.com/python-unittest/#creating-suites-with-the-load_tests-function"
# / target="_blank">customizing test loading and suite creation</a>.
# ! It takes three arguments: a test loader, a series of tests, and a test
# / discovery pattern.
# ! When you call <code>unittest.main()</code>, <code>load_tests()</code> gets
# / called automatically.


# * It’s all about loading and creating!


# > https://realpython.com/quizzes/python-unittest/


# # 10=========================================================================


# ? In the Test-Driven Development (TDD) methodology, what do you do before
# / writing the actual code?


# - Debug the function
# - Write the function
# + Convert the code’s requirements into test cases


# ! In the <a
# / href="https://realpython.com/python-unittest/#a-test-driven-example-rock-paper-and-scissors"
# / target="_blank">Test-Driven Development (TDD) methodology</a>,
# ! you convert the code’s requirements into test cases before writing the
# / actual code.
# ! This approach allows you to ensure that your code meets its requirements
# / and works as expected.
# ! You write tests for the functionality you want to implement, run the tests
# / (which should fail since you haven’t written the code yet),
# ! then write the code to make the tests pass. You repeat this process until
# / all functionality is implemented and all tests pass.


# * In TDD, you start with the tests, not the code!


# > https://realpython.com/quizzes/python-unittest/

