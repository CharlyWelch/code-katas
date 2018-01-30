""" Kata: Sum of the first nth term of Series

#1 Best practices solution by  MMMAAANNN and others:

def series_sum(n):
    return '{:.2f}'.format(sum(1.0/(3 * i + 1) for i in range(n)))

"""


def series_sum(n):
    if n > 1:
        x = 1
        for num in range(0,n-1):
            x += 1/(4+(3*num))
        return "{0:.2f}".format(x)
    else: return "{0:.2f}".format(n)


# Series: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 +...