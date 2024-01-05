from operator import add, mul, sub

square = lambda x: x * x
identity = lambda x: x
triple = lambda x: 3 * x
increment = lambda x: x + 1

def accumulate(combiner, base, n, f):
    for i in range(1,n+1):
        base = combiner(base,f(i))
    return base


# print(accumulate(add, 0, 5, identity)) 
# print(accumulate(add, 11, 5, identity))
# print(accumulate(add, 11, 0, identity))
# print(accumulate(add, 11, 3, square))
# print(accumulate(mul, 2, 3, square)) 
# print(accumulate(lambda x, y: x + y + 1, 2, 3, square))
# print(accumulate(lambda x, y: (x + y) % 17, 19, 20, square))


def summation_using_accumulate(n, f):
    """Returns the sum of f(1) + ... + f(n). The implementation
    uses accumulate.

    >>> summation_using_accumulate(5, square)
    55
    >>> summation_using_accumulate(5, triple)
    45
    >>> from construct_check import check
    >>> # ban iteration and recursion
    >>> check('hw02.py', 'summation_using_accumulate',
    ...       ['Recursion', 'For', 'While'])
    True
    """
    "*** YOUR CODE HERE ***"
    return accumulate(lambda a,b:a+b,0,n,f)

# print(summation_using_accumulate(5, square))
# print(summation_using_accumulate(5, triple))


def product_using_accumulate(n, f):
    """An implementation of product using accumulate.

    >>> product_using_accumulate(4, square)
    576
    >>> product_using_accumulate(6, triple)
    524880
    >>> from construct_check import check
    >>> # ban iteration and recursion
    >>> check('hw02.py', 'product_using_accumulate',
    ...       ['Recursion', 'For', 'While'])
    True
    """
    "*** YOUR CODE HERE ***"
    return accumulate(lambda a,b:a*b,1,n,f)

# print(product_using_accumulate(4, square))
# print(product_using_accumulate(6, triple))

def missions(f):
    """DO NOT EDIT THIS FUNCTION"""
    def mission1(f):
        if f(0) == 0 and f(1) == 2:
            print('MISSION 1 SOLVED')
            return lambda g: mission2(g(f))
        else:
            print('MISSION 1 FAILED')

    def mission2(f):
        if f(0) == 0 and f(1) == 2:
            print('MISSION 2 SOLVED')
            return mission3(0, 0)
        else:
            print('MISSION 2 FAILED')

    def mission3(f, g):
        def mission3_inner(f):
            if f == g:
                return mission3(f, g + 1)

        if g == 5:
            print('MISSION 3 SOLVED')
            return 'The cake is a lie.'
        else:
            return mission3_inner

    return mission1(f)

def get_the_cake(missions):
    """
    Write a higher order function so that it calls three
    mission functions in turn and return the hidden cake.
    You are not allowed to return variable cake or print
    the messages directly. A correct solution contains
    only one expression.

    By the way, do you know that "The cake is a lie" is 
    a catchphrase from the 2007 video game Portal? Visit
    https://en.wikipedia.org/wiki/The_cake_is_a_lie
    if you have never played Portal before!

    >>> the_cake = get_the_cake(missions)
    MISSION 1 SOLVED
    MISSION 2 SOLVED
    MISSION 3 SOLVED
    >>> the_cake
    'The cake is a lie.'
    >>> # check that your answer consists of nothing but an
    >>> # expression (this docstring) and a return statement
    >>> import inspect, ast
    >>> [type(x).__name__ for x in ast.parse(inspect.getsource(get_the_cake)).body[0].body]
    ['Expr', 'Return']
    """
    return missions(lambda x:2*x)(lambda f:f)(0)(1)(2)(3)(4)

# the_cake = get_the_cake(missions)
# print(the_cake)


def protected_secret(password, secret, num_attempts):
    """
    Returns a function which takes in a password and prints the SECRET if the password entered matches
    the PASSWORD given to protected_secret. Otherwise it prints "INCORRECT PASSWORD". After NUM_ATTEMPTS
    incorrect passwords are entered, the secret is locked and the function should print "SECRET LOCKED".

    >>> my_secret = protected_secret("correcthorsebatterystaple", "I love NJU", 2)
    >>> my_secret = my_secret("hax0r_1") # 2 attempts left
    INCORRECT PASSWORD
    >>> my_secret = my_secret("correcthorsebatterystaple")
    I love NJU
    >>> my_secret = my_secret("hax0r_2") # 1 attempt left
    INCORRECT PASSWORD
    >>> my_secret = my_secret("hax0r_3") # No attempts left
    SECRET LOCKED
    >>> my_secret = my_secret("correcthorsebatterystaple")
    SECRET LOCKED
    """
    def get_secret(password_attempt):
        "*** YOUR CODE HERE ***"
        if num_attempts == 0:
            print('SECRET LOCKED')
            return protected_secret(password,secret,num_attempts)
        elif password_attempt == password:
            print(secret)
            return protected_secret(password,secret,num_attempts)
        else:
            print('INCORRECT PASSWORD')
            return protected_secret(password,secret,num_attempts-1)
    
    return get_secret

my_secrete = protected_secret("correcthorsebatterystaple", "I love NJU", 2)
my_secrete = my_secrete("hax0r_1")
my_secrete = my_secrete("correcthorsebatterystaple")
my_secrete = my_secrete("hax0r_2")
my_secrete = my_secrete("hax0r_3")










