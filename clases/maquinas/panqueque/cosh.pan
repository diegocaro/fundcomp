# Implementa la función coseno hiperbólico
#   cosh(x) = (exp(x) + exp(-x)) / 2
#   cosh(x) = -x exp x exp add 2 /
# donde x = 2
PUSH -2
EXP
PUSH 2
EXP
ADD
PUSH 2
DIV
WRITE
HALT