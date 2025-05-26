# # 1==========================================================================


# ? True or False:
# ? You can add a directory to the Python module search path at runtime by
# / appending the directory path to the module search path.


# + True
# - False


# ! Yes, you can add a directory to
# ! <a
# / href="https://realpython.com/python-modules-packages/#the-module-search-path"
# / target="_blank">the Python module search path</a>
# ! at runtime by using <code>sys.path.append()</code>.
# ! This method appends the directory to the end of the list
# / <code>sys.path</code>:


# > https://realpython.com/quizzes/python-modules-packages/


# # 2==========================================================================


# ? What does from &lt;module_name&gt; import * do?


# + It imports only the public objects from a module.
# - It imports all objects from a module into the local symbol table.
# - It raises a SyntaxError.
# - It imports the module as an alias named *.


# ! The <code>from &lt;module_name&gt; import *</code> statement in Python
# ! <a
# / href="https://realpython.com/python-modules-packages/#from-module_name-import-names"
# / target="_blank">imports all objects from a module</a>
# ! into the local symbol table, except for those that begin with an
# / underscore (<code>_</code>).
# ! These objects are <a
# / href="https://realpython.com/python-double-underscore/"
# / target="_blank">considered non-public</a> in Python.


# * Python doesn’t have private objects, but in the context of importing, it
# / has <em>public</em> objects.


# > https://realpython.com/quizzes/python-modules-packages/


# # 3==========================================================================


# ? You’ve seen how you can import individual objects under alternate names.
# / This approach also works for whole modules and packages.
# ? For example, how can you import the numpy package under the alternate name
# / np?


# - import numpy rename np
# - import np from numpy
# - import numpy alias np
# + import numpy as np


# ! In Python, you can
# ! <a
# / href="https://realpython.com/python-modules-packages/#import-module_name-as-alt_name"
# / target="_blank">import a package under an alternate name</a>
# ! using the syntax <code>import &lt;module_or_package_name&gt; as
# / &lt;alt_name&gt;</code>.
# ! This allows you to refer to the module or package using the alternate name
# / in your code:


# * It works similarly to importing specific objects under alternate names.


# > https://realpython.com/quizzes/python-modules-packages/


# # 4==========================================================================


# ? What does the __all__ list in a package’s __init__.py file control?


# - The order in which Python imports the modules
# + The modules that Python imports when you use from <package_name> import *
# - The classes and functions that Python imports when you use from <package_name> import *


# ! The <code>__all__</code> list in a package’s <code>__init__.py</code> file
# ! <a
# / href="https://realpython.com/python-modules-packages/#importing-from-a-package"
# / target="_blank">controls the modules that Python imports</a>
# ! when you use <code>from &lt;package_name&gt; import *</code>.


# > https://realpython.com/quizzes/python-modules-packages/


# # 5==========================================================================


# ? Fill in the blanks:
# ? You have a package pkg with the following structure:
# ? <code>pkg/
# ? ├── __init__.py
# ? ├── sub_pkg1/
# ? │ ├── __init__.py
# ? │ ├── mod1.py
# ? │ └── mod2.py
# ? └── sub_pkg2/
# ?   ├── __init__.py
# ?   ├── mod3.py
# ?   └── mod4.py</code>
# ? You can import mod1 from the subpackage sub_pkg1 using the following
# / syntax:
# ? import _____

# - sub_pkg1.mod1 from pkg
# + pkg.sub_pkg1.mod1
# - mod1
# - mod1 from pkg.sub_pkg1


# ! You can import a module from a <a
# / href="https://realpython.com/python-modules-packages/#subpackages"
# / target="_blank">subpackage</a>
# ! using the <code>import</code> keyword and the package’s dot notation:


# > https://realpython.com/quizzes/python-modules-packages/
