"""Kata: High and Low
#1 Best practices solution by deantwo and others:

def high_and_low(numbers): #z.
    nn = [int(s) for s in numbers.split(" ")]
    return "%i %i" % (max(nn),min(nn))
  
"""

def high_and_low(numbers):
    numbers = numbers.split(" ")
    ints = list(map(lambda x: int(x), numbers))
    numbers = "{0} {1}".format(max(ints), min(ints))  
    return numbers

print(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"))