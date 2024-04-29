# # 1==========================================================================


# ? What does the term serialization refer to in the context of JSON?


# + Transforming data into a series of bytes
# - Decoding data from the JSON standard
# - Reading data into memory
# - Writing data to disk


# ! In the context of JSON, <a
# / href="https://realpython.com/python-json/#a-little-vocabulary"
# / target="_blank">serialization</a>
# ! refers to transforming data into a series of bytes.
# ! This process allows you to store the data or transmit it across a network.


# * Think about what you need to do when you want to store or transmit data
# / over a network.


# > https://realpython.com/quizzes/python-json/


# # 2==========================================================================


# ? How are Python data types converted to JSON using the json library?
# ? (Select all that apply.)


# + list → array
# + str → string
# - True → True
# + False → false
# + dict → object
# - tuple → string
# + tuple → array
# + int, long, and float → number
# - list → object
# + True → true
# + None → null


# ! The <code>json</code> library in Python <a
# / href="https://realpython.com/python-json/#serializing-json"
# / target="_blank">serializes</a>
# ! Python objects into JSON according to a specific conversion.


# * Remember that JSON data types are limited compared to Python’s,
# * so more than one Python data type may convert to the same JSON structure.


# > https://realpython.com/quizzes/python-json/


# # 3==========================================================================


# ? Which keyword argument allows you to change the indentation size for
# / nested structures in JSON when using json.dumps()?


# - tab
# - spacing
# + indent
# - format


# ! You can <a
# / href="https://realpython.com/python-json/#some-useful-keyword-arguments"
# / target="_blank">change the indentation size</a>
# ! for nested structures in JSON by using the <code>indent</code> keyword
# / argument in <code>json.dumps()</code>:


# * It’s all about the indentation.


# > https://realpython.com/quizzes/python-json/


# # 4==========================================================================


# ? What happens when you encode a tuple into JSON and then decode it back
# / into Python?


# + You get a list.
# - You get a string.
# - You get a dictionary.
# - You get a tuple.


# ! When you serialize a tuple into JSON and then <a
# / href="https://realpython.com/python-json/#deserializing-json"
# / target="_blank">deserialize</a>
# ! it back into Python, then you get a <a
# / href="https://realpython.com/python-list/" target="_blank">list</a>:


# * Remember, JSON doesn’t have the concept of tuples!


# > https://realpython.com/quizzes/python-json/


# # 5==========================================================================


# ? What function converts a Python object into a JSON string?


# - json.convert()
# + json.dumps()
# - json.save()


# ! You can <a href="https://realpython.com/python-json/#serializing-json"
# / target="_blank">convert a Python object into a JSON string</a>
# ! using <code>json.dumps()</code>. This is part of Python’s built-in
# / <code>json</code> module.


# * The <em>s</em> stands for <em>string</em>.


# > https://realpython.com/quizzes/python-json/


# # 6==========================================================================


# ? Fill in the blanks:
# ? To translate a custom object into JSON, you can provide an encoding
# / function
# ? to the dump() function’s _____ parameter. The json module will call
# ? this function on any objects that aren’t natively serializable.


# - decode
# - encoder
# + default


# ! To <a href="https://realpython.com/python-json/#encoding-custom-types"
# / target="_blank">encode a custom object</a>
# ! into JSON, you can provide an encoding function
# ! to the <code>dump()</code> function’s <code>default</code> parameter. The
# / <code>json</code> module will call
# ! this function on any objects that aren’t natively serializable.


# > https://realpython.com/quizzes/python-json/

