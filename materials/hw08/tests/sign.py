test = {
  'name': 'sign',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (sign -42)
          def5a8c3e39d76dfbcb66189bf0d3593
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (sign 0)
          5ca79ce4fb57688138ae494e7845eb74
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (sign 42)
          38dac9033a8f5e8edb2dbe6428e02d1d
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
