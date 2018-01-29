"""Kata: High and Low
#1 Best practices solution by javafreak and others:

def getCount(inputStr):
    return sum(1 for let in inputStr if let in "aeiouAEIOU")

"""

    num_vowels = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for x in inputStr:
        if x in vowels:
            num_vowels += 1
    return num_vowels

print(getCount("aeiou yes"))