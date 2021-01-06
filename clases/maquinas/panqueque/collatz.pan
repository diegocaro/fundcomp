READ    # PUSH integer from keyboard
POP 0   # mem[0] = top, guardamos n en la posicion 0 de la memoria

collatz:
LOAD 0  # top = mem[0]  
PUSH 1
GT          # n < 1 ?
JUMPZ fin
LOAD 0
WRITE
LOAD 0
PUSH 2
MOD
PUSH 0
EQ
JUMPZ par

impar:
LOAD 0
PUSH 2
DIVI
POP 0
JUMP collatz

par:
LOAD 0
PUSH 3
MULT
PUSH 1
ADD
POP 0 
JUMP collatz   # mem[0] = top

fin:
LOAD 0
WRITE
HALT