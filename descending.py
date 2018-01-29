"""Kata: Descending Order
#1 Best practices solution by laoris and others:

def Descending_Order(num):
    return int("".join(sorted(str(num), reverse=True)))
    
"""

def Descending_Order(num):
    digits = sorted([int(x) for x in str(num)], reverse=True)
    return int(''.join([str(x) for x in digits]))

