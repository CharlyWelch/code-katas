""" Kata: Who is going to pay for the wall
#1 best practices solution by gdebenito:

who_is_paying = lambda n: [n, n[:2]] if len(n)>2 else [n]

"""

def who_is_paying(name):
    names = []
    names.append(name)
    if len(name) > 2:
        names.append(name[:2])
    return names