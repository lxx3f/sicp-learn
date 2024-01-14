""" Homework 4: Data Abstraction and Trees"""

from ADT import tree, label, branches, is_leaf, print_tree

def test(x,y):
    if x == y:
        pass
    else:
        print('error')

#####################
# Required Problems #
#####################

# Problem 1
def couple(lst1, lst2):
    """Return a list that contains lists with i-th elements of two sequences
    coupled together.
    >>> lst1 = [1, 2, 3]
    >>> lst2 = [4, 5, 6]
    >>> couple(lst1, lst2)
    [[1, 4], [2, 5], [3, 6]]
    >>> lst3 = ['c', 6]
    >>> lst4 = ['s', '1']
    >>> couple(lst3, lst4)
    [['c', 's'], [6, '1']]
    """
    assert len(lst1) == len(lst2)
    "*** YOUR CODE HERE ***"
    return [[lst1[i],lst2[i]] for i in range(len(lst1))]

lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
couple(lst1, lst2),[[1, 4], [2, 5], [3, 6]]
lst3 = ['c', 6]
lst4 = ['s', '1']
couple(lst3, lst4),[['c', 's'], [6, '1']]



# Problem 2
# The constructor and selectors of the arm
def mobile(left, right):
    """Construct a mobile from a left arm and a right arm."""
    assert is_arm(left), "left must be a arm"
    assert is_arm(right), "right must be a arm"
    return ['mobile', left, right]


def is_mobile(m):
    """Return whether m is a mobile."""
    return type(m) == list and len(m) == 3 and m[0] == 'mobile'


def left(m):
    """Select the left arm of a mobile."""
    assert is_mobile(m), "must call left on a mobile"
    return m[1]


def right(m):
    """Select the right arm of a mobile."""
    assert is_mobile(m), "must call right on a mobile"
    return m[2]


def arm(length, mobile_or_planet):
    """Construct a arm: a length of rod with a mobile or planet at the end."""
    assert is_mobile(mobile_or_planet) or is_planet(mobile_or_planet)
    return ['arm', length, mobile_or_planet]


def is_arm(s):
    """Return whether s is a arm."""
    return type(s) == list and len(s) == 3 and s[0] == 'arm'


def length(s):
    """Select the length of a arm."""
    assert is_arm(s), "must call length on a arm"
    return s[1]


def end(s):
    """Select the mobile or planet hanging at the end of a arm."""
    assert is_arm(s), "must call end on a arm"
    return s[2]


# Problem 2.1
def planet(size):
    """Construct a planet of some size.

    >>> planet(5)
    ['planet', 5]
    """
    assert size > 0
    "*** YOUR CODE HERE ***"
    return ['planet',size]

test(planet(5),['planet',5])

def size(w):
    """Select the size of a planet.

    >>> p = planet(5)
    >>> size(p)
    5
    """
    assert is_planet(w), 'must call size on a planet'
    "*** YOUR CODE HERE ***"
    return w[1]

def is_planet(w):
    """Whether w is a planet."""
    return type(w) == list and len(w) == 2 and w[0] == 'planet'

test(size(planet(5)),5)

# examples and usage
def examples():
    t = mobile(arm(1, planet(2)),
               arm(2, planet(1)))
    u = mobile(arm(5, planet(1)),
               arm(1, mobile(arm(2, planet(3)),
                             arm(3, planet(2)))))
    v = mobile(arm(4, t), arm(2, u))
    return (t, u, v)


def total_weight(m):
    """Return the total weight of m, a planet or mobile.

    >>> t, u, v = examples()
    >>> total_weight(t)
    3
    >>> total_weight(u)
    6
    >>> total_weight(v)
    9
    """
    "*** YOUR CODE HERE ***"
    if is_mobile(m):
        return total_weight(left(m)) + total_weight(right(m))
    elif is_arm(m):
        return total_weight(end(m))
    elif is_planet(m): 
        return size(m) 

t, u, v = examples()
test(total_weight(t),3)
test(total_weight(u),6)
test(total_weight(v),9)       

# Problem 2.2
def balanced(m):
    """Return whether m is balanced.

    >>> t, u, v = examples()
    >>> balanced(t)
    True
    >>> balanced(v)
    True
    >>> w = mobile(arm(3, t), arm(2, u))
    >>> balanced(w)
    False
    >>> balanced(mobile(arm(1, v), arm(1, w)))
    False
    >>> balanced(mobile(arm(1, w), arm(1, v)))
    False
    """
    assert is_mobile(m)
    "*** YOUR CODE HERE ***"
    res = True
    arm1,arm2 = left(m),right(m)
    if total_weight(end(arm1)) * length(arm1) == total_weight(end(arm2)) * length(arm2):
        if is_mobile(end(arm1)):
            res = balanced(end(arm1))
        if is_mobile(end(arm2)) and res:
            res = balanced(end(arm2))
    else:
        res = False
    return res

test(balanced(t),True)
test(balanced(v),True)
w = mobile(arm(3, t), arm(2, u))
test(balanced(w),False)
test(balanced(mobile(arm(1, v), arm(1, w))),False)
test(balanced(mobile(arm(1, w), arm(1, v))),False)

# Problem 2.3
def totals_tree(m):
    """Return a tree representing the mobile/planet with its total weight at the root.

    >>> t, u, v = examples()
    >>> print_tree(totals_tree(t))
    3
      2
      1
    >>> print_tree(totals_tree(u))
    6
      1
      5
        3
        2
    >>> print_tree(totals_tree(v))
    9
      3
        2
        1
      6
        1
        5
          3
          2
    """
    assert is_mobile(m) or is_planet(m)
    "*** YOUR CODE HERE ***"
    if is_mobile(m):
        return tree(total_weight(m),[totals_tree(end(left(m))),totals_tree(end(right(m)))])
    else:
        return tree(total_weight(m))

# print_tree(totals_tree(t))
# print_tree(totals_tree(u))
# print_tree(totals_tree(v))

# Problem 3.1
def add_trees(t1, t2):
    """
    >>> numbers = tree(1,
    ...                [tree(2,
    ...                      [tree(3),
    ...                       tree(4)]),
    ...                 tree(5,
    ...                      [tree(6,
    ...                            [tree(7)]),
    ...                       tree(8)])])
    >>> print_tree(add_trees(numbers, numbers))
    2
      4
        6
        8
      10
        12
          14
        16
    >>> print_tree(add_trees(tree(2), tree(3, [tree(4), tree(5)])))
    5
      4
      5
    >>> print_tree(add_trees(tree(2, [tree(3)]), tree(2, [tree(3), tree(4)])))
    4
      6
      4
    >>> print_tree(add_trees(tree(2, [tree(3, [tree(4), tree(5)])]), \
    tree(2, [tree(3, [tree(4)]), tree(5)])))
    4
      6
        8
        5
      5
    """
    "*** YOUR CODE HERE ***"
    res_label = label(t1) + label(t2)
    res_branch = []
    i = 0
    while i < len(branches(t1)) and i < len(branches(t2)):
        res_branch.append(add_trees(branches(t1)[i],branches(t2)[i]))
        i += 1
    res_branch += branches(t1)[i:]
    res_branch += branches(t2)[i:]
    return tree(res_label,res_branch)

numbers = tree(1,[tree(2,[tree(3),tree(4)]),tree(5,[tree(6,[tree(7)]),tree(8)])])
# print_tree(add_trees(numbers, numbers))
# print_tree(add_trees(tree(2), tree(3, [tree(4), tree(5)])))
# print_tree(add_trees(tree(2, [tree(3)]), tree(2, [tree(3), tree(4)])))
# print_tree(add_trees(tree(2, [tree(3, [tree(4), tree(5)])]),tree(2, [tree(3, [tree(4)]), tree(5)])))

# Problem 3.2
def bigpath(t, n):
    """Return the number of paths in t that have a sum larger or equal to n.

    >>> t = tree(1, [tree(2), tree(3, [tree(4), tree(5)])])
    >>> bigpath(t, 3)
    4
    >>> bigpath(t, 6)
    2
    >>> bigpath(t, 9)
    1
    """
    "*** YOUR CODE HERE ***"
    if is_leaf(t):
        return 1 if label(t) >= n else 0
    else:
        res = 0
        res += 1 if label(t) >= n else 0
        for i in range(len(branches(t))):
            res += bigpath(branches(t)[i],n-label(t))
        return res

t = tree(1, [tree(2), tree(3, [tree(4), tree(5)])])
test(bigpath(t,3),4)
test(bigpath(t,6),2)
test(bigpath(t,9),1)

# Problem 3.3
def bigger_path(t, n):
    """Return the number of paths in t that have a sum larger or equal to n.

    >>> t = tree(1, [tree(2), tree(3, [tree(4), tree(5)])])
    >>> bigger_path(t, 3)
    9
    >>> bigger_path(t, 6)
    4
    >>> bigger_path(t, 9)
    1
    """
    "*** YOUR CODE HERE ***"
    res = 0
    res += bigpath(t,n)
    if is_leaf(t):
        pass
    else:
        for i in range(len(branches(t))):
            res += bigger_path(branches(t)[i],n)
    return res

test(bigger_path(t,3),9)
test(bigger_path(t,6),4)
test(bigger_path(t,9),1)


# Problem 3.4
def has_path(t, word):
    """Return whether there is a path in a tree where the entries along the path
    spell out a particular word.

    >>> greetings = tree('h', [tree('i'),
    ...                        tree('e', [tree('l', [tree('l', [tree('o')])]),
    ...                                   tree('y')])])
    >>> print_tree(greetings)
    h
      i
      e
        l
          l
            o
        y
    >>> has_path(greetings, 'h')
    True
    >>> has_path(greetings, 'i')
    False
    >>> has_path(greetings, 'hi')
    True
    >>> has_path(greetings, 'hello')
    True
    >>> has_path(greetings, 'hey')
    True
    >>> has_path(greetings, 'bye')
    False
    """
    assert len(word) > 0, 'no path for empty word.'
    "*** YOUR CODE HERE ***"
    if label(t) == word[0]:
        if len(word) == 1:
            return True
        else:
            for i in range(len(branches(t))):
                if has_path(branches(t)[i],word[1:]):
                    return True
            return False
    else:
        return False

greetings = tree('h', [tree('i'),tree('e', [tree('l', [tree('l', [tree('o')])]),tree('y')])])
# print_tree(greetings)
test(has_path(greetings, 'h'),True)
test(has_path(greetings, 'i'),False)
test(has_path(greetings, 'hi'),True)
test(has_path(greetings, 'hello'),True)
test(has_path(greetings, 'hey'),True)
test(has_path(greetings, 'bye'),False)

##########################
# Just for fun Questions #
##########################

# Problem 4
def fold_tree(t, base_func, merge_func):
    """Fold tree into a value according to base_func and merge_func"""
    "*** YOUR CODE HERE ***"
    return merge_func(base_func(t),[fold_tree(b,base_func,merge_func) for b in branches(t)])

def count_leaves(t):
    """Count the leaves of a tree.

    >>> t = tree(1, [tree(2), tree(3, [tree(4), tree(5)])])
    >>> count_leaves(t)
    3
    """
    return fold_tree(t, lambda t: 1 if is_leaf(t) else 0, lambda x,bs: x + sum(bs))

test(count_leaves(t),3)

def label_sum(t):
    """Sum up the labels of all nodes in a tree.

    >>> t = tree(1, [tree(2), tree(3, [tree(4), tree(5)])])
    >>> label_sum(t)
    15
    """
    return fold_tree(t, label, lambda x,bs: x + sum(bs))

test(label_sum(t),15)

def preorder(t):
    """Return a list of the entries in this tree in the order that they
    would be visited by a preorder traversal.

    >>> t = tree(1, [tree(2), tree(3, [tree(4), tree(5)])])
    >>> preorder(t)
    [1, 2, 3, 4, 5]
    """
    return fold_tree(t, lambda t:[label(t)],lambda x,bs:x + [b for y in bs for b in y])

test(preorder(t),[1,2,3,4,5])

