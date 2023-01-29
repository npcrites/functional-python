#!/usr/bin/python3
'''
Complete each function below so that the test cases pass.
Your solutions should use the map and filter functions,
and not for loops or list comprehensions.
'''

def evens(n):
    if n > 0:
        xs = filter(lambda n: n%2 == 0, range(n+1))
        print(list(xs))
    
    elif n < 0:
        xs = []
        print(list(xs))

    else:
        xs = [0]
        print(xs)


def threes(n):
    xs1 = filter(lambda n: '3' in str(n), range(n+1))
    print(list(xs1))


def small_words(text):
    '''
    Returns a list of all words in the input text that are less than 5 characters long.

    HINT:
    Recall that text.split() converts the text variable into a list of words.
    '''

    xs2 = filter(lambda text: len(text) < 5 ,text.split())
    print(list(xs2))

def squares(n):

    '''
    Returns a list of all square number between 1 and n inclusive.
    Recall that the nth square number is defined to be n*n.

    >>> squares(1)
    [1]
    >>> squares(2)
    [1, 4]
    >>> squares(3)
    [1, 4, 9]
    >>> squares(10)
    [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    '''

    xs3 = map(lambda n: n**2, range(n+1))
    print(list(xs3))

def lengths(strings):
    '''
    Given a list of strings, returns a list of the lengths of the corresponding strings.

    >>> lengths([])
    []
    >>> lengths(['test'])
    [4]
    >>> lengths(['this','is','a','test'])
    [4, 2, 1, 4]
    '''

    xs4 = map(lambda strings: len(strings), strings)
    print(list(xs4))
