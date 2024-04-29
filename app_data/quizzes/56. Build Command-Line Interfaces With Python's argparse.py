# # 1==========================================================================


# ? Fill in the blanks:
# ? In Python, you can create full-featured command-line interfaces (CLIs)
# ? with the _____ module from the standard library.


# - os
# + argparse
# - click


# ! Python’s <a href="https://docs.python.org/3/library/argparse.html"
# / target="_blank"><code>argparse</code></a>
# ! module is a powerful tool for creating command-line interfaces (CLIs)
# ! that ships with Python in its comprehensive standard library.


# > https://realpython.com/quizzes/command-line-interfaces-python-argparse/


# # 2==========================================================================


# ? What are two common types of user interfaces in programming?
# ? (Select two options.)


# + Command-Line Interfaces (CLIs)
# - Utility-Based User Interfaces (UBUIs)
# + Graphical User Interfaces (GUIs)
# - Application Programming Interfaces (APIs)


# ! Two common types of user interfaces in programming are
# ! <a href="https://realpython.com/learning-paths/python-gui-programming/"
# / target="_blank">Graphical User Interfaces (GUIs)</a>
# ! and
# ! <a
# / href="https://realpython.com/command-line-interfaces-python-argparse/#getting-to-know-command-line-interfaces"
# / target="_blank">Command-Line Interfaces (CLIs)</a>.


# * One type is more visual, while the other is more text-based.


# > https://realpython.com/quizzes/command-line-interfaces-python-argparse/


# # 3==========================================================================


# ? What are the two types of command-line arguments recognized by the
# / argparse module?
# ? (Select all that apply.)


# + Optional arguments
# - Mandatory arguments
# - Keyword arguments
# + Positional arguments


# ! The <code>argparse</code> module recognizes two types of command-line
# / arguments:


# * One type of argument is named after its position in the command construct.
# * The other type isn’t mandatory and can modify the behavior of the command.


# > https://realpython.com/quizzes/command-line-interfaces-python-argparse/


# # 4==========================================================================


# ? Which method do you use to customize the command-line arguments and
# / options of your CLI?


# - .customize_option()
# - .add_option()
# + .add_argument()
# - .customize_argument()


# ! You use the <a
# / href="https://realpython.com/command-line-interfaces-python-argparse/#fine-tuning-your-command-line-arguments-and-options"
# / target="_blank"><code>.add_argument()</code></a>
# ! to customize the command-line arguments and options of your CLI.


# * You’re adding something to your CLI.


# > https://realpython.com/quizzes/command-line-interfaces-python-argparse/


# # 5==========================================================================


# ? What does .parse_args() return when you call it on an argparse parser?


# - A string containing all the arguments and options provided at the command line
# - A dictionary mapping arguments to their corresponding values
# + A Namespace object containing all the arguments and options provided at the command line and their corresponding values
# - A list of all the arguments and options provided at the command line


# ! The <code>.parse_args()</code> method, when called on an
# / <code>argparse</code> parser,
# ! returns a <code>Namespace</code> object. This object contains all the
# / arguments and options
# ! provided at the command line and their corresponding values.


# * It’s a custom thing.


# > https://realpython.com/quizzes/command-line-interfaces-python-argparse/


# # 6==========================================================================


# ? What’s the purpose of the __main__.py file in the app layout of the CLI
# / project discussed in the tutorial?


# - It lists the project’s external dependencies.
# - It specifies the project’s build system and other configurations.
# + It provides the application’s entry-point script or executable file.
# - It contains unit tests for the application’s components.


# ! In the <a
# / href="https://realpython.com/command-line-interfaces-python-argparse/#setting-up-your-cli-apps-layout-and-build-system"
# / target="_blank">tutorial’s CLI project</a>,
# ! the <code>__main__.py</code> file provides the application’s
# ! entry-point script. This is where your application starts running.


# * Think about what <code>main()</code> functions are often used for in a
# / program.


# > https://realpython.com/quizzes/command-line-interfaces-python-argparse/


# # 7==========================================================================


# ? You’re using argparse to parse command-line arguments for your Python
# / script. You want to provide a great user experience by providing helpful
# / usage instructions.
# ? Which of the following can you do to improve the help and usage content?
# ? (Select all that apply.)


# + Define the program’s description and epilog message.
# + Set the program’s name.
# + Display grouped help for arguments and options.
# - Add images to the help message.
# - Change the color of the help message.


# ! <code>argparse</code> provides several ways to improve the help and usage
# / content of your Python scripts:


# * <code>argparse</code> is a <em>text</em>-based library.


# > https://realpython.com/quizzes/command-line-interfaces-python-argparse/


# # 8==========================================================================


# ? When you add an option or flag to a command-line interface with argparse,
# / you can define how you want to store the option’s value in the resulting
# / Namespace object by using the action argument to .add_argument().
# ? Which of the following are valid values for the action argument?
# ? (Select all that apply.)


# + "version"
# - "store_list"
# + "store_true"
# - "store_dict"
# + "store"
# + "append_const"
# + "append"
# + "store_const"
# + "count"
# + "store_false"


# ! The <code>action</code> argument to <code>.add_argument()</code> can take
# / one of several possible values:


# * The <code>action</code> argument can take one of several possible values.
# * Each value corresponds to a specific way of handling the option’s value.


# > https://realpython.com/quizzes/command-line-interfaces-python-argparse/


# # 9==========================================================================


# ? How can you customize the help message for a specific argument in
# / argparse?


# - Use the usage argument in the .add_argument() method
# - Use the epilog argument in the .add_argument() method
# + Use the help argument in the .add_argument() method


# ! You can customize the help message for a specific argument in
# / <code>argparse</code> by using the <code>help</code> argument in the
# ! <a
# / href="https://realpython.com/command-line-interfaces-python-argparse/#providing-and-customizing-help-messages-in-arguments-and-options"
# / target="_blank">.add_argument()</a>
# ! method:


# * Well… let’s just say the argument has a quite descriptive name.


# > https://realpython.com/quizzes/command-line-interfaces-python-argparse/


# # 10=========================================================================


# ? What does a nonzero exit status typically indicate when terminating a CLI
# / application?


# - The application is still running
# + Abnormal termination or failure
# - Successful termination
# - The application is taking a prolonged holiday


# ! In CLI applications, a nonzero exit status typically indicates an
# ! <a
# / href="https://realpython.com/command-line-interfaces-python-argparse/#handling-how-your-cli-apps-execution-terminates"
# / target="_blank">abnormal termination or failure</a>.


# * Not good.


# > https://realpython.com/quizzes/command-line-interfaces-python-argparse/

