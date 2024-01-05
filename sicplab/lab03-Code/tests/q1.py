test = {
  'name': 'Question 1: Tricky Functions',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> def f(x):
          ...     return x * x
          >>> g = lambda x: f(x + 1)
          >>> g
          Function
          # locked
          >>> g(1)
          4
          # locked
          >>> print(g(2))
          9         
          # locked
          >>> f = lambda x: f(x + 1)
          >>> f(1)    # When is the return expression of a lambda expression executed?
          Forever
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> def f1(n):
          ...     def f2(x):
          ...         if x == 0:
          ...             return 'cake'
          ...         else:
          ...             print('The cake is a lie.')
          ...             n -= x
          ...             return f2(n)
          ...     return f2
          >>> f1(2)
          Function
          >>> f1(2)(2)
          The cake is a lie.
          cake
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
