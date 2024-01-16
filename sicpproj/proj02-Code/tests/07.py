test = {
  'name': 'Problem 7',
  'points': 3,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> big_limit = 10
          >>> minimum_mewtations("wind", "wind", big_limit)
          168e201af4950d5f73b97b178697ad92
          # locked
          >>> minimum_mewtations("wird", "wiry", big_limit)
          232ad58b0f81f037ca6eb6a8f27a11b5
          # locked
          >>> minimum_mewtations("wird", "bird", big_limit)
          232ad58b0f81f037ca6eb6a8f27a11b5
          # locked
          >>> minimum_mewtations("wird", "wir", big_limit)
          232ad58b0f81f037ca6eb6a8f27a11b5
          # locked
          >>> minimum_mewtations("wird", "bwird", big_limit)
          232ad58b0f81f037ca6eb6a8f27a11b5
          # locked
          >>> minimum_mewtations("speling", "spelling", big_limit)
          232ad58b0f81f037ca6eb6a8f27a11b5
          # locked
          >>> minimum_mewtations("used", "use", big_limit)
          232ad58b0f81f037ca6eb6a8f27a11b5
          # locked
          >>> minimum_mewtations("hash", "ash", big_limit)
          232ad58b0f81f037ca6eb6a8f27a11b5
          # locked
          >>> minimum_mewtations("ash", "hash", big_limit)
          232ad58b0f81f037ca6eb6a8f27a11b5
          # locked
          >>> minimum_mewtations("roses", "arose", big_limit)     # roses -> aroses -> arose
          fae562ba87ca875594496dfd22cc638d
          # locked
          >>> minimum_mewtations("tesng", "testing", big_limit)   # tesng -> testng -> testing
          fae562ba87ca875594496dfd22cc638d
          # locked
          >>> minimum_mewtations("rlogcul", "logical", big_limit) # rlogcul -> logcul -> logicul -> logical
          e7749498d0ccda838a1931ea58535532
          # locked
          >>> minimum_mewtations("", "", big_limit) # nothing to nothing needs no edits
          168e201af4950d5f73b97b178697ad92
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> big_limit = 10
          >>> minimum_mewtations("cats", "scat", big_limit)
          2
          >>> minimum_mewtations("purng", "purring", big_limit)
          2
          >>> minimum_mewtations("ckiteus", "kittens", big_limit)
          3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> small_limit = 0
          >>> minimum_mewtations("cats", "cats", small_limit)
          0
          >>> minimum_mewtations("", "", small_limit)
          0
          >>> minimum_mewtations("cats", "scat", small_limit) > small_limit
          True
          >>> minimum_mewtations("purng", "purring", small_limit) > small_limit
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> negative_limit = -1
          >>> minimum_mewtations("cats", "cats", negative_limit) > negative_limit
          True
          >>> minimum_mewtations("cats", "scat", negative_limit) > negative_limit
          True
          >>> minimum_mewtations("purng", "purring", negative_limit) > negative_limit
          True
          >>> minimum_mewtations("", "", negative_limit) > negative_limit
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> small_words_list = ["spell", "nest", "test", "pest", "best", "bird", "wired",
          ...                     "abstraction", "abstract", "wire", "peeling", "gestate",
          ...                     "west", "spelling", "bastion"]
          >>> autocorrect("speling", small_words_list, minimum_mewtations, 10)
          'spelling'
          >>> autocorrect("abstrction", small_words_list, minimum_mewtations, 10)
          'abstraction'
          >>> autocorrect("wird", small_words_list, minimum_mewtations, 10)
          'bird'
          >>> autocorrect("gest", small_words_list, minimum_mewtations, 10)
          'nest'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # ***Check that the recursion stops when the limit is reached***
          >>> import trace, io
          >>> from contextlib import redirect_stdout
          >>> with io.StringIO() as buf, redirect_stdout(buf):
          ...     trace.Trace(trace=True).runfunc(minimum_mewtations, "someawe", "awesome", 3)
          ...     output = buf.getvalue()
          >>> len([line for line in output.split('\n') if 'funcname' in line]) < 1000
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('rut', 'rzumt', k) > k for k in range(5)])
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('yo', 'yo', 100)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('slurp', 'slurpm', 100)
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('nice', 'tie', 100)
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # ***Check that the recursion stops when the limit is reached***
          >>> import trace, io
          >>> from contextlib import redirect_stdout
          >>> with io.StringIO() as buf, redirect_stdout(buf):
          ...     trace.Trace(trace=True).runfunc(minimum_mewtations, "someawe", "awesome", 3)
          ...     output = buf.getvalue()
          >>> len([line for line in output.split('\n') if 'funcname' in line]) < 1000
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from cats import minimum_mewtations, autocorrect
      >>> import tests.construct_check as test
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
