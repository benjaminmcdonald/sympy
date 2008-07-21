
def all(iterable):
    """Return True if all elements are set to True. This
       function does not support predicates explicitely,
       but this behaviour can be simulated easily using
       list comprehension.

       >>> all( [True, True, True] )
       True
       >>> all( [True, False, True] )
       False
       >>> all( [ x % 2 == 0 for x in [2, 6, 8] ] )
       True
       >>> all( [ x % 2 == 0 for x in [2, 6, 7] ] )
       False

       NOTE: Starting from Python 2.5 this a built-in.
    """
    for item in iterable:
        if not item:
            return False
    return True

def any(iterable):
    """Return True if at least one element is set to True.
       This function does not support predicates explicitely,
       but this behaviour can be simulated easily using
       list comprehension.

       >>> any( [False, False, False] )
       False
       >>> any( [False, True, False] )
       True
       >>> any( [ x % 2 == 1 for x in [2, 6, 8] ] )
       False
       >>> any( [ x % 2 == 1 for x in [2, 6, 7] ] )
       True

       NOTE: Starting from Python 2.5 this a built-in.
    """
    for item in iterable:
        if item:
            return True
    return False

def make_list(expr, kind):
    """Returns a list of elements taken from specified expresion
       when it is of sequence type (Add or Mul) or singleton list
       otherwise (Rational, Pow etc.).

       >>> from sympy import *
       >>> x, y = map(Symbol, 'xy')

       >>> make_list(x*y, Mul)
       [x, y]
       >>> make_list(x*y, Add)
       [x*y]
       >>> set(make_list(x*y + y, Add)) == set([y, x*y])
       True

    """
    if isinstance(expr, kind):
        return list(expr.args[:])
    else:
        return [expr]

def flatten(iterable):
    """Recursively denest iterable containers.

       >>> flatten([1, 2, 3])
       [1, 2, 3]
       >>> flatten([1, 2, [3]])
       [1, 2, 3]
       >>> flatten([1, [2, 3], [4, 5]])
       [1, 2, 3, 4, 5]
    """
    result = []

    for item in iterable:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)

    return result

def postorder_traversal(node):
    """ Do a postorder traversal of a tree.

    This generator recursively yields nodes that it has visited in a postorder
    fashion. That is, it descends through the tree depth-first to yield all of
    a node's children's postorder traversal before yielding the node itself.

    Parameters
    ----------
    node : sympy expression
        The expression to traverse.

    Yields
    ------
    subtree : sympy expression
        All of the subtrees in the tree.

    Examples
    --------
    >>> from sympy import symbols
    >>> from sympy.utilities.iterables import postorder_traversal
    >>> x,y,z = symbols('xyz')
    >>> set(postorder_traversal((x+y)*z)) == set([z, y, x, x + y, z*(x + y)])
    True
    """
    for arg in node.args:
        for subtree in postorder_traversal(arg):
            yield subtree
    yield node

def preorder_traversal(node):
    """ Do a preorder traversal of a tree.

    This generator recursively yields nodes that it has visited in a preorder
    fashion. That is, it yields the current node then descends through the tree
    breadth-first to yield all of a node's children's preorder traversal.

    Parameters
    ----------
    node : sympy expression
        The expression to traverse.

    Yields
    ------
    subtree : sympy expression
        All of the subtrees in the tree.

    Examples
    --------
    >>> from sympy import symbols
    >>> from sympy.utilities.iterables import preorder_traversal
    >>> x,y,z = symbols('xyz')
    >>> set(preorder_traversal((x+y)*z)) == set([z, x + y, z*(x + y), x, y])
    True
    """
    yield node
    for arg in node.args:
        for subtree in preorder_traversal(arg):
            yield subtree

