test = {
  'name': 'Problem 6',
  'points': 100,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> always_roll(3)(10, 20)
          acb7ae51e29364a82ec8f43b4d92dd9d
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> always_roll(0)(99, 99)
          0b19e2d0e0e3a7972243801cf8e912eb
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hog import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
