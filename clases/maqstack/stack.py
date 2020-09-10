# Simulación máquina de stack
# Código basado en implementación de Alejandro Cisterna Villalobos
# Autor: Diego Caro

import sys
from math import sqrt, exp

INS = ['PUSH','POP','ADD', 'PROD', 'DIV', 'MOD','POW', 'EXP', 'SQRT']
ADD = lambda a,b: a+b
PROD = lambda a,b: a*b
DIV = lambda a,b: a/b
MOD = lambda a,b: a%b
POW = lambda a,b: a^b
EXP = lambda a: exp(a)
SQRT = lambda a: sqrt(a)


def execute(p):
    s = list()
    for i, op in enumerate(p):
        print(i, op)
        if isinstance(op,list) and len(op)==2 and op[0] == 'PUSH':
            s.append(op[1])
        elif op == 'POP':
            a = s.pop()
            print('POP:', a)
        elif op == 'RAI':
            a = s.pop()
            s.append(RAI(a))
        elif op == 'EXP':
            a = s.pop()
            s.append(EXP(a))
        elif op in INS:
            a = s.pop()
            b = s.pop()
            
            f = globals()[op]
            c = f(a,b)
            print('\tEXECUTE: ', op, a, b, '=', c)
            s.append(c)
        else:
            assert op in INS
    # post condition
    assert len(s) == 1
    
    return s[0]

def read(f):
    program = list()
    nlines = 0
    for line in sys.stdin:
        ops = line.strip().split()
        if ops[0] == 'PUSH':
            if len(ops) == 2:
                ops[1] = int(ops[1])
                program.append(ops)
            else:
                assert 'missing value for PUSH'
        elif len(ops) == 1:
            program.append(ops[0])
    
    # post condition ???

    return program
 
program = read(sys.stdin)
ans = execute(program)
print(ans)