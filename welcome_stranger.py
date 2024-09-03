# Create a function that takes 2 arguments, a list and a dictionary. 
# The list will contain 2 or more elements that, when joined with spaces, 
# will produce a person's name. The dictionary will contain two keys, 
# "title" and "occupation", and the appropriate values. 
# Your function should return a greeting that uses the person's full name, and mentions the person's title.

# Create a function that takes a list and joins the list with spaces


def greetings(name, info):
    space = ' '
    return f'Hello, {space.join(name)}! Nice to have a {info["title"]} {info["occupation"]} around.'

greeting = greetings(
    ["John", "Q", "Doe"],
    {"title": "Master", "occupation": "Plumber"},
)
print(greeting)
# Hello, John Q Doe! Nice to have a Master Plumber around.