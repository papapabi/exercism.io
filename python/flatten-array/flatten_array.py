import collections

def flatten(xs):
    """Returns a single flattened list with all values retained except None.

    param: xs (sequence): an arbitrarily nested sequence. 
    returns: a flattened list.
    """
    if not xs:
        return []
    if (isinstance(xs[0], collections.Iterable) and 
        not isinstance(xs[0], (str, bytes))):
            return flatten(xs[0]) + flatten(xs[1:])
    else:
        if xs[0] is None:
            return []
        else:
            return xs[:1] + flatten(xs[1:])
