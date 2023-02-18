(define (cadr lst) (car (cdr lst)))
(define (caddr lst) (car (cdr (cdr lst))))
(define (infix e) 
  (if (not (list? e))
    e
    `(,(cadr e) ,(infix (car e)) ,(infix (caddr e)))
  )
)