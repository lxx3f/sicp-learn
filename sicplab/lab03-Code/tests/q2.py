test = {
  'name': 'Question 2: Squared Virahanka Fibonacci',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> def virfib_sq(n):
          ...     print(n)
          ...     if n <= 1:
          ...         return n
          ...     return (virfib_sq(n - 1) + virfib_sq(n - 2)) ** 2
          >>> virfib_sq
          Function
          # locked
          >>> r0 = virfib_sq(0)
          0
          # locked
          >>> virfib_sq(1)
          1
          1
          # locked
          >>> r1 = virfib_sq(1)
          1
          # locked
          >>> r2 = virfib_sq(2)
          2
          1
          0
          # locked
          >>> r3 = virfib_sq(3)
          3
          2
          1
          0
          1
          # locked
          >>> r3
          4
          # locked
          >>> (r1 + r2) ** 2
          4
          # locked
          >>> r4 = virfib_sq(4)
          4
          3
          2
          1
          0
          1
          2
          1
          0
          # locked
          >>> r4
          25
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
