test = {
  'name': 'Problem 8',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> typed = ['I', 'have', 'begun']
          >>> prompt = ['I', 'have', 'begun', 'to', 'type']
          >>> print_progress({'id': 1, 'progress': 0.6})
          2c3230b0d982b178e3f494375626a6aa
          # locked
          >>> report_progress(typed, prompt, 1, print_progress) # print_progress is called on the report
          2c3230b0d982b178e3f494375626a6aa
          8a6aacacfd7f4fb22948a7fae031cea7
          # locked
          >>> report_progress(['I', 'begun'], prompt, 2, print_progress)
          091f53f4aadf3c74d31509e5b783b470
          6fdd50e116438cd8ef30e5c75628b8a4
          # locked
          >>> report_progress(['I', 'hve', 'begun', 'to', 'type'], prompt, 3, print_progress)
          5424ffa15cef19306c513fd38a904386
          6fdd50e116438cd8ef30e5c75628b8a4
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> print_progress = lambda d: print('ID:', d['id'], 'Progress:', d['progress'])
          >>> # The above function displays progress in the format ID: __, Progress: __
          >>> print_progress({'id': 1, 'progress': 0.6})
          ID: 1 Progress: 0.6
          >>> typed = ['how', 'are', 'you']
          >>> prompt = ['how', 'are', 'you', 'doing', 'today']
          >>> report_progress(typed, prompt, 2, print_progress)
          ID: 2 Progress: 0.6
          0.6
          >>> report_progress(['how', 'aree'], prompt, 3, print_progress)
          ID: 3 Progress: 0.2
          0.2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['smopple'], 22, print_progress)
          ID: 22 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['equalizing', 'phrymaceous', 'jFluidimeter'], ['equalizing', 'phrymaceous', 'fluidimeter', 'seeds'], 48, print_progress)
          ID: 48 Progress: 0.5
          0.5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['seeingly'], 13, print_progress)
          ID: 13 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['iprObaT\\ively', 'unabatedly', 'reundergo'], ['probatively', 'unabatedly', 'reundergo', 'unweld', 'handgun', 'hydrometra', 'recessionary'], 35, print_progress)
          ID: 35 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['elysia'], 90, print_progress)
          ID: 90 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['entomical'], 52, print_progress)
          ID: 52 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['choirwise', 'uncircumstantial', 'glassine', 'supplies', 'underivedly', 'henter', 'undeserving'], 47, print_progress)
          ID: 47 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from cats import report_progress
      >>> print_progress = lambda d: print('ID:', d['id'], 'Progress:', d['progress'])
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
