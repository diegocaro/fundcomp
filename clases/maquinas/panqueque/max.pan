# OPS     pseudocodigo          stack
READ      # lee a               [a ]
READ      # lee b               [a, b]
OVER      # apila a             [a, b, a]
OVER      # apila b             [a, b, a, b]
GT        # a < b               [a, b, a < b]
JMPZ fin  # salta a fin si T=0  [a, b]
POP       # desapila            [a ]
fin:      # 
SEND      $ imprime             [ ]
