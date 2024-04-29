# # 1==========================================================================


# ? On a high level, what’s pyenv?


# + A tool for managing multiple Python versions
# - A Python-based version control system
# - A Python package for creating virtual environments


# ! <a href="https://realpython.com/intro-to-pyenv/"
# / target="_blank"><code>pyenv</code></a> is a popular tool
# ! used to install and manage multiple versions of Python on the same system.
# ! It allows you to easily switch between different versions of Python
# ! for various projects and development needs.


# > https://realpython.com/quizzes/intro-to-pyenv/


# # 2==========================================================================


# ? What are some reasons to avoid using the Python that comes pre-installed
# / with your operating system, also known as System Python?
# ? (Select all that apply.)


# + System Python may not support the latest Python features.
# - You can’t install new packages into System Python.
# + Some operating systems use the packaged Python for operation, so changing it could cause issues.
# + Installing packages globally can cause conflicts with other users.
# + It may not be the version of Python that you want to use.


# ! There are several reasons why you might want to
# ! <a href="https://realpython.com/intro-to-pyenv/#why-not-use-system-python"
# / target="_blank">avoid using <em>System Python</em></a>,
# ! which is a name for the Python that comes pre-installed with your
# / operating system:


# * Most of these are true.


# > https://realpython.com/quizzes/intro-to-pyenv/


# # 3==========================================================================


# ? You’ve installed pyenv and now you want to install a specific version of
# / Python. Which of the following commands would you use to install Python
# / 3.11.7?
# ? (Select all that apply.)


# + pyenv install 3.11.7
# + pyenv install -v 3.11.7
# - pyenv install python 3.11.7
# - pyenv install --version 3.11.7


# ! To <a
# / href="https://realpython.com/intro-to-pyenv/#using-pyenv-to-install-python"
# / target="_blank">install a specific version of Python with
# / <code>pyenv</code></a>,
# ! you use the <code>pyenv install</code> command
# ! followed by the version number. For example, to install Python 3.11.7, you
# / would run:


# * There are two correct solutions.


# > https://realpython.com/quizzes/intro-to-pyenv/


# # 4==========================================================================


# ? What does the -l or --list flag do when used with the pyenv install
# / command?


# - Lists all installed Python versions
# - Lists all Python versions that you’ve used before, starting with the most recent
# + Lists all Python versions available to install


# ! The <code>-l</code> or <code>--list</code> flag, when used with the
# / <code>pyenv install</code> command,
# ! <a href="https://realpython.com/intro-to-pyenv/#install"
# / target="_blank">lists all available Python versions</a>
# ! that you can install using <code>pyenv</code>.


# * Try running the command. It always gives you a long list!


# > https://realpython.com/quizzes/intro-to-pyenv/


# # 5==========================================================================


# ? What does the pyenv versions command display?


# - All Python versions that you use frequently
# - The latest Python version
# + All currently installed Python versions
# - The Python version your system uses


# ! The <a href="https://realpython.com/intro-to-pyenv/#versions"
# / target="_blank"><code>pyenv versions</code> command</a>
# ! displays all currently installed Python versions.
# ! It also shows which Python version is currently active, which is indicated
# / by a star (<code>*</code>):


# > https://realpython.com/quizzes/intro-to-pyenv/


# # 6==========================================================================


# ? How do you create a new virtual environment for a specific Python version
# / using pyenv and the pyenv-virtualenv plugin?


# - pyenv install 3.11.8 --env=myenv
# - pyenv newenv 3.11.8 myenv
# - pyenv create 3.11.8 myenv
# + pyenv virtualenv 3.11.8 myenv


# ! The correct command to <a
# / href="https://realpython.com/intro-to-pyenv/#creating-virtual-environments"
# / target="_blank">create a virtual environment</a>
# ! for a specific Python version using <code>pyenv</code> with the
# / <code>pyenv-virtualenv</code>
# ! plugin is the following:


# * The command involves the <code>pyenv-virtualenv</code> plugin
# * and specifies the Python version followed by the virtual environment’s
# / name.


# > https://realpython.com/quizzes/intro-to-pyenv/


# # 7==========================================================================


# ? How can you use the .python-version file with pyenv to automatically
# / activate virtual environments when you enter a folder that contains such a
# / file?


# - By typing the pyenv activate command so quickly each time you enter a folder that it feels automatic
# + By passing the name of the virtual environment when running pyenv local
# - By setting the PYENV_VERSION environment variable to match the content of the .python-version file


# ! When you run the command <code>pyenv local</code> and pass it the name of
# / your virtual environment
# ! instead of a Python version,
# ! then <code>pyenv</code> sets a local Python version that points to your
# / virtual environment.
# ! It saves that info into a <code>.python-version</code> file in the current
# / directory:


# * Consider how <code>pyenv</code> interacts with directory-specific settings
# / to manage Python versions.


# > https://realpython.com/quizzes/intro-to-pyenv/

