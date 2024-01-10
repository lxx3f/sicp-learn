test = {
  'name': 'Problem 4',
  'points': 100,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> swine_swap(9)
          baebe1f6b92b3967d0d783179087be29
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> swine_swap(1)
          baebe1f6b92b3967d0d783179087be29
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> swine_swap(2)
          c8ca0faf02b8729b7fd27037278ac4ba
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> swine_swap(121)
          baebe1f6b92b3967d0d783179087be29
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
