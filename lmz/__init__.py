from itertools import zip_longest

def Map(*x,**y):
    return list(map(*x,**y))

def Zip(*x,**y):
    return list(zip(*x,**y))

def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)

def Transpose(x): 
    return list(zip(*x))
