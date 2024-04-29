# # 1==========================================================================


# ? How do you let Django know that a new app you’ve created exists?


# + Add a reference in the INSTALLED_APPS list in settings.py
# - Add any new file to the app’s directory
# - Move the app’s code into a new directory called registered/
# - Run python manage.py startapp <app_name> in your terminal


# ! To let Django know that a new app you’ve created exists, you need to add a
# / reference to its configuration class
# ! in the <code>INSTALLED_APPS</code> list in <code>settings.py</code>.


# * It’s all about <em>setting</em> yourself up for success!


# > https://realpython.com/quizzes/get-started-with-django/


# # 2==========================================================================


# ? What type of brackets do you use in the notation to connect a URL to a
# / view function in Django when the URL includes a variable part?


# - Curly braces: {int:pk}
# - Parentheses: (int:pk)
# + Angular brackets: <int:pk>
# - Square brackets: [int:pk]


# ! In Django, you can connect a URL to a view function even when the URL
# ! <a href="https://realpython.com/get-started-with-django-1/#add-the-routes"
# / target="_blank">includes a variable part</a>.


# > https://realpython.com/quizzes/get-started-with-django/


# # 3==========================================================================


# ? Where do you define your database structure in a Django app?


# - In the settings.py module
# - In the views.py module
# - In the urls.py module
# + In the models.py module


# ! In a Django app, you
# ! <a href="https://realpython.com/get-started-with-django-1/#define-a-model"
# / target="_blank">define your database structure</a>
# ! in the <code>models.py</code> module.


# * Where do you put your classes that represent database tables?


# > https://realpython.com/quizzes/get-started-with-django/


# # 4==========================================================================


# ? What do you use Django’s Object Relational Mapper (ORM) for?


# - To create a new database
# - To create database migrations
# + To create classes that correspond to database tables


# ! An Object Relational Mapper (ORM) in Django is a programming technique
# ! that allows you to create classes that correspond to database tables.


# * An ORM maps Python objects to database information.


# > https://realpython.com/quizzes/get-started-with-django/


# # 5==========================================================================


# ? What are the key points to remember when creating Django templates?
# ? (Select all that apply)


# + You can use for loops to iterate over data and create HTML elements for each item.
# + You can access an object’s attributes using dot notation inside double curly brackets.
# + You can extend a base template to avoid repeating common elements across different templates.
# - You can only use for loops to iterate over data if the data is stored in a list.


# ! <a
# / href="https://realpython.com/get-started-with-django-1/#craft-the-templates"
# / target="_blank">Django’s template language</a>
# ! allows you to create dynamic HTML content.
# ! You can use <code>for</code> loops to iterate over data and create HTML
# / elements for each item.
# ! This is useful when you want to display a list of objects, such as
# / projects in a portfolio.


# * Start the party! You can create dynamic HTML content!


# > https://realpython.com/quizzes/get-started-with-django/


# # 6==========================================================================


# ? Which Django management command can you use to create a superuser for the
# / Django admin site?


# - startadmin
# - createadmin
# + createsuperuser
# - superuser


# ! You create a superuser for
# ! <a
# / href="https://realpython.com/get-started-with-django-1/#leverage-the-django-admin-site"
# / target="_blank">the Django admin site</a>
# ! by running the <code>createsuperuser</code> management command:


# > https://realpython.com/quizzes/get-started-with-django/

