# Este programa calcula el máximo entre dos numeros
# el resultado lo deja en el stack, pero no imprime.
# 
# Para ver el resultado ejecuta panqueque con la opción -v
#    python3 panqueque.py -v minv2.pan
#
PUSH 5  # agrega 5 al stack
PUSH 9  # agrega 9 al stack
OVER
OVER
LT
JMPZ end
SWAP
end:
SWAP
POP
