;; This program is ridiculously simple.
;; It just to demostrate a little bit of ELISP language.

(defun simple-calc(expr)
  (interactive "sEnter calculation(example 10 / 2):  ")
  (setq result (calc-eval expr))
  (print (concat "Result: " result)))

