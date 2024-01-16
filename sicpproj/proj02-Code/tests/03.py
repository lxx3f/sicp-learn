test = {
  'name': 'Problem 3',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> accuracy("12345", "12345") # This should return 100.0 (not the integer 100!)
          14be02400b49f1fdcf6a7eb38454eddb
          # locked
          >>> accuracy("a b c", "a b c")
          14be02400b49f1fdcf6a7eb38454eddb
          # locked
          >>> accuracy("a  b  c  d", "b  a  c  d")
          b82372325ac59890d7e195d5a0bb65bb
          # locked
          >>> accuracy("a b", "c d e")
          a55ff5373a53b92a47b83c5732dd9679
          # locked
          >>> accuracy("Cat", "cat") # the function is case-sensitive
          a55ff5373a53b92a47b83c5732dd9679
          # locked
          >>> accuracy("a b c d", "a d")
          c708e2a1731add8a43ca4511ae848940
          # locked
          >>> accuracy("abc", " ")
          a55ff5373a53b92a47b83c5732dd9679
          # locked
          >>> accuracy("a b \tc" , "a b c") # Tabs don't count as words
          14be02400b49f1fdcf6a7eb38454eddb
          # locked
          >>> accuracy("abc", "")
          a55ff5373a53b92a47b83c5732dd9679
          # locked
          >>> accuracy("", "abc")
          a55ff5373a53b92a47b83c5732dd9679
          # locked
          >>> accuracy("a b c d", "b c d")
          a55ff5373a53b92a47b83c5732dd9679
          # locked
          >>> accuracy("cats.", "cats") # punctuation counts
          a55ff5373a53b92a47b83c5732dd9679
          # locked
          >>> accuracy("", "") # Returns 100.0
          14be02400b49f1fdcf6a7eb38454eddb
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> accuracy('Cute Dog!', 'Cute Dog.')
          50.0
          >>> accuracy('A Cute Dog!', 'Cute Dog.')
          0.0
          >>> accuracy('cute Dog.', 'Cute Dog.')
          50.0
          >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
          50.0
          >>> accuracy('Cute', 'Cute Dog.')
          100.0
          >>> accuracy('', 'Cute Dog.')
          0.0
          >>> accuracy('', '')
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> source_text = "Abstraction, in general, is a fundamental concept to computer science and software development. The process of abstraction can also be referred to as modeling and is closely related to the concepts of theory and design. Models can also be considered types of abstractions per their generalization of aspects of reality. Abstraction in computer science is also closely related to abstraction in mathematics due to their common focus on building abstractions as objects, but is also related to other notions of abstraction used in other fields such as art."
          >>> typed_string1 = "Abstraction, in general, is a fundamental concept to computer science and software development. The process of abstraction can also be referred to as modeling and is closely related to the concepts of theory and design. Models can also be considered types of abstractions per their generalization of aspects of reality. Abstraction in computer science is also closely related to abstraction in mathematics due to their common focus on building abstractions as objects, but is also related to other notions of abstraction used in other fields such as art."
          >>> typed_string2 = "Abstraction, in general, is a fundamentl concept to computer science and software development. The process of abstraction can also be referred to as modeling and is closely related to the concepts of theory and design. Models can also be considered types of abstractions per their generalization of aspects of reality. Abstraction in computer science is also closely related to abstraction in mathematics due to their common focus on building abstractions as objects, but is also related to other notions of abstraction usd in other fields such as art."
          >>> typed_string3 = "Abstraction,"
          >>> typed_string4 = "Abstraction, in general, is a fundamental concept to computer science and software development. The process of abstraction can also be referred to as modeling and is closely related to the concepts of theory and design. Models can also be considered types of abstractions per their generalization of aspects of reality. Abstraction in computer science is also closely related to abstraction in mathematics due to their common focus on building abstractions as objects, but is also related to other notions of abstraction used in other fields such as art. extra"
          >>> typed_string5 = "Abstraction, in general, is a fundamental concept to computer science and software development. The process of abstraction can also be referred to as modeling and is closely related to the concepts of theory and design. Models can also be considered types of abstractions per their generalization of aspects of reality. Abstraction in computer science is also closely related to abstraction in mathematics due to their common focus on building abstractions as objects, but is also related to other notions of abstraction used in other fields such as art. Abstraction, in general, is a fundamental concept to computer science and software development. The process of abstraction can also be referred to as modeling and is closely related to the concepts of theory and design. Models can also be considered types of abstractions per their generalization of aspects of reality. Abstraction in computer science is also closely related to abstraction in mathematics due to their common focus on building abstractions as objects, but is also related to other notions of abstraction used in other fields such as art. art"
          >>> typed_string6 = "abstraction"
          >>> round(accuracy(typed_string2, source_text), 1)
          97.7
          >>> round(accuracy(typed_string3, source_text), 1)
          100.0
          >>> round(accuracy(typed_string4, source_text), 1)
          98.9
          >>> round(accuracy(typed_string5, source_text), 1)
          49.7
          >>> round(accuracy(typed_string6, source_text), 1)
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('modern[-izer marque_ .roi$t befr+iz. psychologi"c baptizee_', 'modern[-izer marque_ .roi$t befr+iz. psychologi"c baptizee_ u-nflu"ent f]reckleproof'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('phrymaceous bridgema:ki<ng non*support|er (feasible respectability_ mong{relize ul<la}ge sinistrogyration treasur"es(', 'phrymaceous bridgema:ki<ng non*support|er (feasible respectability_'), 2)
          55.56
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('ammonionitr.ate s>ulpholysis a&dmirative cirso]tomy itin+\\eration preoffensively', 'ammonionitr.ate s>ulpholysis a&dmirative cirso]tomy itin+\\eration preoffensively acardiac +psychophysio;logist nicknameable'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('handgun hydrometra)^ anticentralization unmicrob/#ic paradisal+ vulval dr.oo[py', 'handgun hydrometra)^ anticentralization unmicrob/#ic paradisal+'), 2)
          71.43
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('cunge(boi mistressdom sir\\l<oin mol^}eproof ala@creatin$ine', 'cunge(boi mistressdom sir\\l<oin mol^}eproof ala@creatin$ine'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from cats import accuracy
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
