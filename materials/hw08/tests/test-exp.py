test = {
  'name': 'test-exp',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (= 8 (exp 2 3))
          af2fd7905919be94e4d509e8239d5fd1
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (= 1 (exp 9.137 0))
          af2fd7905919be94e4d509e8239d5fd1
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (= 1024 (exp 4 5))
          af2fd7905919be94e4d509e8239d5fd1
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (= 6.25 (exp 2.5 2))
          af2fd7905919be94e4d509e8239d5fd1
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (= 16 (remainder (exp 2 (exp 2 10)) 100)))
          af2fd7905919be94e4d509e8239d5fd1
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'hw08)
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
