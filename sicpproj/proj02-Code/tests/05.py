test = {
  'name': 'Problem 5',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> abs_diff = lambda w1, w2, limit: abs(len(w2) - len(w1))
          >>> autocorrect("cul", ["culture", "cult", "cultivate"], abs_diff, 10)
          3b903e3a019da04728527fa8ebce576a
          # locked
          >>> autocorrect("cul", ["culture", "cult", "cultivate"], abs_diff, 0)
          1a362506e22c8e03e22f57702cc77d4f
          # locked
          >>> autocorrect("wor", ["worry", "car", "part"], abs_diff, 10)
          dd4a3aed7d6df189d8af77923cf50ddf
          # locked
          >>> first_diff = lambda w1, w2, limit: 1 if w1[0] != w2[0] else 0
          >>> autocorrect("wrod", ["word", "rod"], first_diff, 1)
          70ab68f4a49142a64c29be8bfbb4ee64
          # locked
          >>> autocorrect("inside", ["idea", "inside"], first_diff, 0.5)
          7c57452cb176c89d4cd931cd68f816a3
          # locked
          >>> autocorrect("inside", ["idea", "insider"], first_diff, 0.5)
          cda0fbe31938d4af633db9d11047c25c
          # locked
          >>> autocorrect("outside", ["idea", "insider"], first_diff, 0.5)
          0a62924e9e516400ecf94e6ff95e139a
          # locked
          >>> length_ratio = lambda w1, w2, limit: len(w2) / len(w1) # An asymmetric diff function
          >>> autocorrect("aaa", ["a"], length_ratio, 2) # typed_word ("aaa") is passed in as the first argument to a diff function
          b844008180870cc36972f88e9fa6adb7
          # locked
          >>> autocorrect("cats", ["panthers", "lions"], length_ratio, 2)
          90fa40a100fb41e3b0662ac3420d5adb
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> ten_diff = lambda w1, w2, limit: 10 # Always returns 10
          >>> autocorrect("hwllo", ["butter", "hello", "potato"], ten_diff, 20)
          'butter'
          >>> first_diff = lambda w1, w2, limit: (1 if w1[0] != w2[0] else 0) # Checks for matching first char
          >>> autocorrect("tosting", ["testing", "asking", "fasting"], first_diff, 10)
          'testing'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> matching_diff = lambda w1, w2, limit: sum([w1[i] != w2[i] for i in range(min(len(w1), len(w2)))]) # Num matching chars
          >>> autocorrect("tosting", ["testing", "asking", "fasting"], matching_diff, 10)
          'testing'
          >>> autocorrect("tsting", ["testing", "rowing"], matching_diff, 10)
          'rowing'
          >>> autocorrect("bwe", ["awe", "bye"], matching_diff, 10)
          'awe'
          >>> autocorrect("bwe", ["bye", "awe"], matching_diff, 10)
          'bye'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> words_list = sorted(lines_from_file('data/words.txt')[:10000])
          >>> autocorrect("testng", words_list, lambda w1, w2, limit: 1, 10)
          'a'
          >>> autocorrect("testing", words_list, lambda w1, w2, limit: 1, 10)
          'testing'
          >>> autocorrect("gesting", words_list, lambda w1, w2, limit: sum([w1[i] != w2[i] for i in range(min(len(w1), len(w2)))]) + abs(len(w1) - len(w2)), 10)
          'getting'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('stilter', ['modernizer', 'posticum', 'undiscernible', 'heterotrophic', 'waller', 'marque', 'dephosphorization'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 1)
          'posticum'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('bridgemaking', ['seeds', 'bridgemaking', 'endemiological', 'cobaltinitrite'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
          'bridgemaking'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('excursively', ['cirsotomy', 'terminableness', 'margaritaceous', 'gawkiness', 'ascon', 'floccose'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 1)
          'excursively'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('hypertense', ['hyperbrachycranial'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 2)
          'hypertense'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from cats import autocorrect, lines_from_file
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
