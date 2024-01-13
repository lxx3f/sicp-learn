test = {
  'name': 'Question 1: Lists',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> s = [7//3, 5, [4, 0, 1], 2]
          >>> s[0]
          2
          # locked
          >>> s[2]
          [4,0,1]
          # locked
          >>> s[-1]
          2
          # locked
          >>> len(s)
          4
          # locked
          >>> 4 in s
          False
          # locked
          >>> 4 in s[2]
          True
          # locked
          >>> s + [3 + 2, 9]
          [2,5,[4,0,1],2,5,9]
          # locked
          >>> s[2] * 2
          [4,0,1,4,0,1]
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> x = [1, 2, 3, 4]
          >>> x[1:3]
          [2,3]
          # locked
          >>> x[:2]
          [1,2]
          # locked
          >>> x[1:]
          [2,3,4]
          # locked
          >>> x[-2:3]
          [3]
          # locked
          >>> x[-2:4]
          [3,4]
          # locked
          >>> x[0:4:2]
          [1,3]
          # locked
          >>> x[::-1]
          [4,3,2,1]
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
