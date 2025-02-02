def memory(n):
    """ 返回一个使用传入的函数修改n的函数
    >>> f = memory(10)
    >>> f(lambda x: x * 2)
    20
    >>> f(lambda x: x- 7)
    13
    >>> f(lambda x: x > 5)
    True
    """
    def f(g):
        nonlocal n
        n = g(n)
        return n
    return f

def group_by(s, fn):
    """ takinging in a sequence s and a function fn and returns a dictionary.
    The values of the dictionary are lists of elements from s. Each element e in a list
    should be constructed such that fn(e) is the same for all elements in that list. The
     key for each value should be fn(e). For each element e in s, check the value that
    calling fn(e) returns, and add e to the corresponding group.

    >>> group_by([12, 23, 14, 45], lambda p: p // 10)
    {1: [12, 14], 2: [23], 4: [45]}
    >>> group_by(range(-3, 4), lambda x: x * x)
    {9: [-3, 3], 4: [-2, 2], 1: [-1, 1], 0: [0]}
    """
    grouped = {}
    for e in s:
        key = fn(e)
        grouped[key] = [i for i in s if fn(i) == key]
    return grouped

def group_by_sol(s, fn):
    """ takinging in a sequence s and a function fn and returns a dictionary.
    The values of the dictionary are lists of elements from s. Each element e in a list
    should be constructed such that fn(e) is the same for all elements in that list. The
     key for each value should be fn(e). For each element e in s, check the value that
    calling fn(e) returns, and add e to the corresponding group.

    >>> group_by_sol([12, 23, 14, 45], lambda p: p // 10)
    {1: [12, 14], 2: [23], 4: [45]}
    >>> group_by_sol(range(-3, 4), lambda x: x * x)
    {9: [-3, 3], 4: [-2, 2], 1: [-1, 1], 0: [0]}
    """
    grouped = {}
    for e in s:
        key = fn(e)
        if key not in grouped:
            grouped[key] = [e]
        else:
            grouped[key].append(e)
    return grouped

def add_this_many(x, el, s):
    """ Adds el to the end of s the number of times x occurs
    in s.
    >>> s = [1, 2, 4, 2, 1]
    >>> add_this_many(1, 5, s)
    >>> s
    [1, 2, 4, 2, 1, 5, 5]
    >>> add_this_many(2, 2, s)
    >>> s
    [1, 2, 4, 2, 1, 5, 5, 2, 2]
    """
    for i in range(len(s)):
        if s[i] == x:
            s.append(el)
    return


def add_this_many_2(x, el, s):
    """ Adds el to the end of s the number of times x occurs
    in s.
    >>> s = [1, 2, 4, 2, 1]
    >>> add_this_many_2(1, 5, s)
    >>> s
    [1, 2, 4, 2, 1, 5, 5]
    >>> add_this_many_2(2, 2, s)
    >>> s
    [1, 2, 4, 2, 1, 5, 5, 2, 2]
    """
    x_counts = s.count(x)
    for i in range(x_counts):
        s.append(el)
    return

def filter(iterable, fn):
    """
    >>> is_even = lambda x: x % 2 == 0
    >>> list(filter(range(5), is_even)) # a list of the values yielded from the call to filter
    [0, 2, 4]
    >>> all_odd = (2*y-1 for y in range (5))
    >>> list(filter(all_odd, is_even))
    []
    """
    for el in iterable:
        if fn(el):
            yield el

def merge(a, b):
    """  taking in two innite generators a
    and b that are in increasing order without duplicates and returns a generator that
    has all the elements of both generators, in increasing order, without duplicates
    
    >>> a = sequence(2, 3) # 2, 5, 8, 11, 14, ...
    >>> b = sequence(3, 2) # 3, 5, 7, 9, 11, 13, 15, ...
    >>> result = merge(a, b) # 2, 3, 5, 7, 8, 9, 11, 13, 14, 15
    >>> [next(result) for _ in range(10)]
    [2, 3, 5, 7, 8, 9, 11, 13, 14, 15]
    """
    next_a = next(a)
    next_b = next(b)
    while True:
        if next_a < next_b:
            yield next_a
            next_a = next(a)
        elif next_a == next_b:
            yield next_a
            next_a, next_b = next(a), next(b)
        else:
            yield next_b
            next_b = next(b)

def sequence(start, step):
    while True:
        yield start
        start += step 

