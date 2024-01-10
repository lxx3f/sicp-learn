test = {
  'name': 'Problem 7',
  'points': 400,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> is_always_roll(always_roll_5)
          baebe1f6b92b3967d0d783179087be29
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> is_always_roll(always_roll(3))
          baebe1f6b92b3967d0d783179087be29
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> is_always_roll(catch_up)
          c8ca0faf02b8729b7fd27037278ac4ba
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
