""" Kata: Beginner Series #3 Sum of Numbers
#1 Best practices solution by hiasen and others:

def get_sum(a,b):
    return sum(xrange(min(a,b), max(a,b)+1))
"""

def get_sum(a,b):
    if b > a:
        return sum(x for x in range(a,b+1))
    else:
        return sum(x for x in range(b,a+1))