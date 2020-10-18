def hello(name=None):
    if name == '':
        return 'Hello, World!'
    elif name is None:
        return 'Hello, World!'
    else:
        return 'Hello, ' + name.capitalize() + '!'
    pass

print (hello('fede'))
print (hello('vale'))
print (hello(''))
print(hello())



# Instructions
#
#     Define a method hello that returns "Hello, Name!" to a given name, or says Hello, World! if name is not given (or passed as an empty String).
#     Assuming that name is a String and it checks for user typos to return a name with a first capital letter (Xxxx).