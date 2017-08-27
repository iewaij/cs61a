test = {
  'name': 'test-filter',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (filter even? '(0 1 1 2 3 5 8))
          f609448368363760ee0a753024d2b0eb
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (filter even? '(2 4 6 8 10))
          88e2ee9cdb7d954cf8475a907d51eaaf
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (filter even? '(1 3 5))
          7e44d32911eb855f7a970358ab156a57
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (filter even? (longlink 8))
          0328d18fb221cffd9e552e82b5317962
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (filter even? (longlink 15))
          7e44d32911eb855f7a970358ab156a57
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'hw08)
      scm> (define (even? x)
        (= (modulo x 2) 0))
      scm> (define (longlink num)
              (define (helper count num result)
                  (if (= count 0)
                    result
                    (helper (- count 1) num (cons num result))
                  )
              )
              (helper num num '())
            )
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
