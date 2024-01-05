test = {
  'name': 'Question 1: Control',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> def xk(c, d):
          ...     if c == 4:
          ...         return 6
          ...     elif d >= 4:
          ...         return 6 + 7 + c
          ...     else:
          ...         return 25
          >>> xk(10, 10)
          e21f9317d59223c27bfded4c28b50623
          # locked
          >>> xk(10, 6)
          e21f9317d59223c27bfded4c28b50623
          # locked
          >>> xk(4, 6)
          30c9c01d682c1c073899ac51c9dcd745
          # locked
          >>> xk(0, 0)
          90ce04e3fa2b06626929a5bd8e93ab63
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> def how_big(x):
          ...     if x > 10:
          ...         print('huge')
          ...     elif x > 5:
          ...         return 'big'
          ...     elif x > 0:
          ...         print('small')
          ...     else:
          ...         print("nothin'")
          >>> how_big(7)
          'big'
          # locked
          >>> how_big(12)
          huge
          # locked
          >>> how_big(1)
          small
          # locked
          >>> how_big(-1)
          nothin'
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> n = 3
          >>> while n >= 0:
          ...     n -= 1
          ...     print(n)
          2
          1
          0
          -1
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> positive = 28
          >>> while positive:
          ...     print("positive?")
          ...     positive -= 3
          Forever
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> positive = -9
          >>> negative = -12
          >>> while negative:
          ...     if positive:
          ...         print(negative)
          ...     positive += 3
          ...     negative += 3
          518ad794713accd9681e060cd074d363
          173616075e1d1d387156f5d6c9eed83a
          1ec53e9bdd9c056a89d72e3230bc8cf2
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
