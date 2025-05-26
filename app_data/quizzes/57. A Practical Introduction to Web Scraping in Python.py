# # 1==========================================================================


# ? Why should you always check a website’s acceptable use policy before
# / scraping it?


# + To see if using automated tools violates its terms of use
# - To find out if the website uses cookies
# - To check if the website is mobile-friendly


# ! Before you use your Python skills for
# ! <a
# / href="https://realpython.com/python-web-scraping-practical-introduction/#scrape-and-parse-text-from-websites"
# / target="_blank">web scraping</a>,
# ! you should always check
# ! your target website’s acceptable use policy.
# ! This is because accessing the website with automated tools
# ! might be a violation of its terms of use.


# * Not all websites welcome scrapers with open arms.


# > https://realpython.com/quizzes/python-web-scraping-practical-introduction/


# # 2==========================================================================


# ? What are some of the challenges you might face when trying to extract text
# / from HTML using Python string methods?
# ? (Select all that apply.)


# + Small differences in HTML tags can cause errors in extraction.
# - String methods don’t work with HTML.
# + HTML can be unpredictable and vary greatly from page to page.
# - HTML content is always too large to process with string methods.


# ! While it’s possible to extract text from HTML using string methods,
# ! this approach can be problematic due to the unpredictable and varied
# / nature of HTML.
# ! For example, even small differences in HTML tags can cause errors in
# / extraction.


# * HTML is just text, but text can be messy.


# > https://realpython.com/quizzes/python-web-scraping-practical-introduction/


# # 3==========================================================================


# ? What does the dot symbol (.) represent in a Python regular expression?


# - Any number of characters
# - The start of a string
# - The end of a string
# + Any single character


# ! In a <a
# / href="https://realpython.com/python-web-scraping-practical-introduction/#get-to-know-regular-expressions"
# / target="_blank">Python regular expression</a>,
# ! the dot symbol (<code>.</code>) represents any single character.


# > https://realpython.com/quizzes/python-web-scraping-practical-introduction/


# # 4==========================================================================


# ? What’s the purpose of the regular expression &lt;.*?&gt; in the context of web
# / scraping?


# + It matches all HTML tags.
# - It matches all email addresses.
# - It matches all non-HTML text.
# - It matches all URLs.


# ! The regular expression <code>&lt;.*?&gt;</code> matches all HTML tags.
# ! It uses the non-greedy <code>.*?</code> to match any text enclosed in
# / <code>&lt;</code> and <code>&gt;</code>.


# * Think about what’s generally between <code>&lt;</code> and
# / <code>&gt;</code> in HTML text.


# > https://realpython.com/quizzes/python-web-scraping-practical-introduction/


# # 5==========================================================================


# ? What are the two arguments you need to pass when creating a BeautifulSoup
# / object?


# - The method to extract data
# + The parser
# + The HTML
# - The URL


# ! When <a
# / href="https://realpython.com/python-web-scraping-practical-introduction/#create-a-beautifulsoup-object"
# / target="_blank">creating a BeautifulSoup object</a>,
# ! you need to pass two arguments:


# * When constructing a <code>BeautifulSoup</code> object, think about what
# / you already have
# * and what you need to add meaning to it.


# > https://realpython.com/quizzes/python-web-scraping-practical-introduction/


# # 6==========================================================================


# ? Which of the following statements about BeautifulSoup objects are true?
# ? (Select all that apply.)


# + You can use .find_all() to return a list of all instances of a particular tag.
# - You can use .fill() to fill out and submit HTML forms.
# + You can use .get_text() to extract all the text from the document and automatically remove any HTML tags.


# ! BeautifulSoup is a Python library for parsing HTML and XML documents.
# ! It creates parse trees that are helpful to extract the data easily.


# * BeautifulSoup is a powerful tool for parsing HTML, but it has its
# / limitations.
# * It can only interpret the text that you get back from a server.


# > https://realpython.com/quizzes/python-web-scraping-practical-introduction/


# # 7==========================================================================


# ? How can you fill out a form using MechanicalSoup?


# + Use .select() to select the inputs and assign values to them.
# - Use .fill() and pass it a dictionary of values to fill the input fields with.
# - Use .write() to write values into the inputs.


# ! With <a
# / href="https://realpython.com/python-web-scraping-practical-introduction/#submit-a-form-with-mechanicalsoup"
# / target="_blank">MechanicalSoup</a>,
# ! you can fill out a form by using the <code>.select()</code> method to
# / select the inputs and assign values to them:


# * MechanicalSoup is designed to interact with forms on a webpage
# * similarly to how you might when using a browser.


# > https://realpython.com/quizzes/python-web-scraping-practical-introduction/


# # 8==========================================================================


# ? What is a headless browser in the context of web scraping with Python?


# - A browser that doesn’t track user data.
# - A browser that doesn’t support JavaScript.
# + A web browser that you control programmatically and doesn’t have a graphical user interface.


# ! A <a
# / href="https://realpython.com/python-web-scraping-practical-introduction/#interact-with-html-forms"
# / target="_blank">headless browser</a>
# ! is a web browser with no graphical user interface that you control
# / programmatically via a Python program.


# * Consider the primary function of a browser when you use it manually,
# * and think about how that might be different when a computer script
# * needs to perform similar tasks without the need for visual output.


# > https://realpython.com/quizzes/python-web-scraping-practical-introduction/

