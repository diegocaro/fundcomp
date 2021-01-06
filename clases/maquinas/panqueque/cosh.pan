# Implementa la función coseno hiperbólico
#   cosh(x) = (exp(x) + exp(-x)) / 2
#   cosh(x) = -x exp x exp add 2 /
# donde x = 3
PUSH 3
PUSH -1
MULT
EXP
PUSH 3
EXP
ADD
PUSH 2
DIV
WRITE
HALT