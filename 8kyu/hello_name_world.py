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

