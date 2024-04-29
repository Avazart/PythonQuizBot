# # 1==========================================================================


# ? What’s the main difference between pipx and pip when installing Python
# / packages?


# - pipx supports installing runnable Python modules
# - pipx requires superuser permissions to install packages
# - pipx can only install packages from PyPI
# + pipx automatically creates and manages virtual environments for each package


# ! The main difference between <code>pipx</code> and <code>pip</code> is that
# / <code>pipx</code> automatically creates and manages virtual environments
# / for every package that you install. This isolates the dependencies of each
# / package, preventing conflicts between different projects that might
# / require the same Python library in different versions. Additionally,
# / <code>pipx</code> adds symbolic links to your <code>PATH</code> variable
# / for every command-line script exposed by the installed packages, so you
# / can invoke these scripts directly from the command line.


# * Consider where each tool installs Python packages.


# > https://realpython.com/quizzes/python-pipx/


# # 2==========================================================================


# ? How can you install pipx? Select all that apply.


# + Using pip
# - By compiling it from source code
# + Using your operating system’s package manager
# + Using pipx


# ! Because <code>pipx</code> is a Python package, you can install it with
# / either <code>pip</code> or <code>pipx</code>,
# ! although the latter method is discouraged. The officially recommended way
# / to
# ! install <code>pipx</code> is through your operating system’s package
# / manager, such as
# ! Scoop on Windows, Homebrew on macOS, or APT on Debian-based Linux
# / distributions.
# ! Doing so makes <code>pipx</code> a standalone command that you can run
# / from anywhere in your file system.
# ! You can learn more about this in the section on <a
# / href="https://realpython.com/python-pipx/#install-pipx-as-a-standalone-tool"
# / target="_blank">installing <code>pipx</code> as a standalone tool</a> in
# / the Real Python <code>pipx</code> tutorial.


# * Remember, <code>pipx</code> is a pure-Python package.


# > https://realpython.com/quizzes/python-pipx/


# # 3==========================================================================


# ? What does the pipx ensurepath command do?


# - It installs pipx
# + It adds the necessary folder paths to your PATH environment variable
# - It checks if pipx is installed correctly
# - It updates pipx to the latest version


# ! The <code>pipx ensurepath</code> command adds the necessary folder paths
# / to your <code>PATH</code> environment variable.
# ! This is a crucial step in using <code>pipx</code> to its fullest. If you
# / forget about this step, then <code>pipx</code> will remind you about it
# / and provide a helpful message.
# ! You can learn more about this in the section on <a
# / href="https://realpython.com/python-pipx/#configure-pipx-before-the-first-run"
# / target="_blank">configuring <code>pipx</code> before the first run</a>.


# * Ensure your path is correct!


# > https://realpython.com/quizzes/python-pipx/


# # 4==========================================================================


# ? Fill in the blanks:
# ? The pipx run command allows you to run Python scripts without having to
# ? install the associated package into one of your existing projects.
# ? It does this by downloading the latest version of the requested package
# ? from PyPI and installing it into a _____.
# ? The command is then run from within that environment without ever touching
# ? your project’s dependencies.


# - permanent virtual environment
# - global environment
# + temporary virtual environment
# - system environment


# ! The <code>pipx run</code> command allows you to run Python scripts without
# / having to
# ! install the associated package into one of your existing projects.


# > https://realpython.com/quizzes/python-pipx/


# # 5==========================================================================


# ? Fill in the blanks:
# ? To install the Python package ruff globally, you would use the command:
# ? _____
# ? This command makes Ruff globally available and you can run it directly by
# / typing
# ? ruff in your terminal.


# - install ruff
# + pipx install ruff
# - pip install ruff
# - python install ruff


# ! To install a Python package globally while keeping your system’s
# / interpreter intact,
# ! you can use <code>pipx</code>.


# > https://realpython.com/quizzes/python-pipx/


# # 6==========================================================================


# ? How can you list all of the installed apps and their commands using pipx?


# - By typing pipx apps in your terminal
# + By typing pipx list in your terminal
# - By typing pipx --list in your terminal
# - By typing pipx --apps in your terminal


# ! You can list all of the installed apps and their commands by typing <a
# / href="https://realpython.com/python-pipx/#list-the-installed-apps"
# / target="_blank"><code>pipx list</code></a> in your terminal. This command
# / shows the location of virtual environments managed by <code>pipx</code>, a
# / folder with symbolic links to the executable entry points, and a folder
# / with manual pages serving as documentation that some packages provide. It
# / also includes the installed packages, their versions, and the Python
# / interpreter used by the associated virtual environment. Additionally,
# / every package contains a list of commands that you can invoke in your
# / terminal.


# * You’re looking for a simple subcommand here.


# > https://realpython.com/quizzes/python-pipx/


# # 7==========================================================================


# ? How can you upgrade all Python packages installed in separate virtual
# / environments with pipx to their latest versions, in one step?


# + Use the upgrade-all subcommand
# - Use the --upgrade flag with the install command
# - Use the install-all subcommand
# - It’s not possible to upgrade all packages at once with pipx


# ! With <code>pipx</code>, you can upgrade all packages installed in separate
# / virtual environments to their latest versions
# ! by using the <code>upgrade-all</code> subcommand:


# * Run <code>pipx --help</code> to check if there’s a suitable option or
# / subcommand.


# > https://realpython.com/quizzes/python-pipx/


# # 8==========================================================================


# ? Think of how you would downgrade a Python package installed with pipx to a
# / specific version. For example, to downgrade Poetry to version 1.1.11,
# / which of the following commands would you use?


# - pipx downgrade --force poetry==1.1.11
# - pipx reinstall --force poetry==1.1.11
# + pipx install --force poetry==1.1.11
# - You can’t downgrade packages with pipx


# ! To downgrade a Python package installed with <code>pipx</code> to a
# / specific version,
# ! you need to use the <code>--force</code> flag with the <code>pipx
# / install</code> command. For example:


# * Think about how you’d achieve this using the regular <code>pip</code>
# / command.


# > https://realpython.com/quizzes/python-pipx/


# # 9==========================================================================


# ? What does the pipx uninstall-all command do?


# + It uninstalls all packages managed by pipx along with their environments
# - It uninstalls all packages, but keeps their virtual environments
# - It uninstalls pipx
# - It uninstalls all Python packages, regardless of how they were installed


# ! The <code>pipx uninstall-all</code> command removes all packages and their
# / virtual environments that are managed by <code>pipx</code>.
# ! It also deletes any related manual pages and symbolic links from your
# / shell.
# ! After running this command, you won’t be able to use these packages
# / anymore.


# * Think again about what <em>all</em> could mean in this context.


# > https://realpython.com/quizzes/python-pipx/


# # 10=========================================================================


# ? Fill in the blanks:
# ? If you need to add an optional plugin to a package installed with pipx,
# ? then you can use the _____ command. This command expects the original
# ? package name, followed by one or more extra dependencies.


# + pipx inject
# - pipx install
# - pipx add
# - pipx append


# ! If you need to add an optional dependency to a package installed with
# / <code>pipx</code>,
# ! then you can use the <a
# / href="https://realpython.com/python-pipx/#inject-dependencies-into-managed-environments"
# / target="_blank"><code>pipx inject</code></a>
# ! command. This command expects the original package name, followed by one
# / or
# ! more extra dependencies.


# > https://realpython.com/quizzes/python-pipx/


# # 11=========================================================================


# ? How can you specify a different Python interpreter when installing a
# / package with pipx? Select all that apply.


# + Set the PIPX_DEFAULT_PYTHON environment variable
# + Use the --python parameter
# - Use the --interpreter parameter
# - Set the PYTHONPATH environment variable


# ! When installing a package with <code>pipx</code>, you can specify a
# / different Python interpreter by using the <code>--python</code> parameter
# ! or setting the <code>PIPX_DEFAULT_PYTHON</code> environment variable.


# * Think about the Python interpreter that <code>pipx</code> uses by default.


# > https://realpython.com/quizzes/python-pipx/


# # 12=========================================================================


# ? How can you make your Python package compatible with pipx?


# - Make it runnable by defining the __main__.py module
# - Package it as a Python ZIP application
# + Define one or more entry points in pyproject.toml
# - Include a shell script named main.bat or main.sh


# ! <code>pipx</code> looks for entry points in your Python package, which are
# / typically defined in the <code>pyproject.toml</code> configuration file.
# / It then registers each entry point as a symbolic link in your shell so you
# / can run them directly as standalone commands globally.


# * Think of the standard way of defining scripts in Python distribution
# / packages.


# > https://realpython.com/quizzes/python-pipx/

