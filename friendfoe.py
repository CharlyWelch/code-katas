""" Kata: High and Low
#1 Best practices solution by colbydauph and others:

def friend(x):
    return [f for f in x if len(f) == 4]
"""

def friend(x):
    return [friend for friend in x if len(friend) == 4]