# OPS          pseudocodigo     stack
PUSH 5       # n = 3            [n ]    
DUP          # i = n            [n, i]
factorial:   # 
PUSH 1       #                  [n, i, 1]
OVER         #                  [n, i, 1, i]
LT           # while 1 < i:     [n, i, 1 < i]
JMPZ fin     #                  [n, i ]
PUSH 1       #                  [n, i, 1 ]
SUB          #    i=i-1         [n, i-1 ]
SWAP                            [i-1, n]
OVER         #                  [i-1, n, i-1]
MULT         #    n=n*i         [i-1, (i-1)*n ]
SWAP         #                  [(i-1)*n, i-1]
JUMP factorial
fin:         #
POP          #                  [6 ]            
SEND         #                  []