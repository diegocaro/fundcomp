# Este programa calcula el máximo entre dos numeros
# el resultado lo deja en el stack, pero no imprime.
# 
# Para ver el resultado ejecuta panqueque con la opción -v
#    python3 panqueque.py -v minv2.pan
#
# OPS         pseudocodigo      stack
PUSH 9     # a = 9             [a, ]
PUSH 15     # b = 15            [a, b ]
OVER        #                   [a, b, a ]
OVER        #                   [a, b, a, b ]
LT          # if a < b          [a, b, a < b?]
JMPZ end    #                   [a, b]
POP         #                   [a ]
end:        #                   [a ]
