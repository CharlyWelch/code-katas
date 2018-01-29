""" Kata: Creating a string for an array of objects from a set of words
#1 Best practices solution by **** and others:

"""
def words_to_object(s):
    objects = s.split()
    
print(words_to_object("1 red 2 white 3 violet 4 green"))

# { _key : _value(_key) for _key in _container }