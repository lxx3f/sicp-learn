test = {
  'name': 'Problem 1',
  'points': 300,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> roll_dice(2, make_test_dice(4, 6, 1))
          eec979b1214e3645f3f9a2f6565eae70
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> roll_dice(3, make_test_dice(4, 6, 1))
          27d7ea0c1ef247eb4d13969601b324fd
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> roll_dice(4, make_test_dice(2, 2, 3))
          12fb4058d6c28b6ccc056b1156595353
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> a = roll_dice(4, make_test_dice(1, 2, 3))
          >>> a # check that the value is being returned, not printed
          27d7ea0c1ef247eb4d13969601b324fd
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> counted_dice = make_test_dice(4, 1, 2, 6)
          >>> roll_dice(3, counted_dice)
          27d7ea0c1ef247eb4d13969601b324fd
          # locked
          >>> # Make sure you call dice exactly num_rolls times!
          >>> # If you call it fewer or more than that, it won't be at the right spot in the cycle for the next roll
          >>> # Note that a return statement within a loop ends the loop
          >>> roll_dice(1, counted_dice)
          0e4902a64fc8eda3bff6f836a1e0cdca
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> roll_dice(9, make_test_dice(6))
          5ef471a5d3a7a0922b7b2ce610fcb1cc
          # locked
          >>> roll_dice(7, make_test_dice(2, 2, 2, 2, 2, 2, 1))
          27d7ea0c1ef247eb4d13969601b324fd
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
