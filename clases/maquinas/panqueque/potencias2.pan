# Calcula todas las potencias de 2
# que son menores que 1000
# --------------------------------------------
# OPS            PSEUDOCODIGO    PILA
# --------------------------------------------

PUSH 1         # a = 1           [a ]

potencia:      #
DUP            #                 [a, a ]
PUSH 1000      #                 [a, a, 1000 ]
LT             #                 [a, a < 1000? ]
JMPZ termina   # if a < 1000:     
DUP            #                 [a, a ]
SEND           #     print a     [a ]
DUP            #                 [a, a ]
ADD            #     a = a + a   [a+a ]
JUMP potencia  #

termina:     
POP            #                 [ ]
