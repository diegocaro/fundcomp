# Simulación máquina de stack
# Código basado en implementación de Alejandro Cisterna Villalobos
# y en http://ebook.pldworld.com/-huihoo-/book/compiler-construction-using-flex-and-bison/StackMachine.html
# Autor: Diego Caro

import sys
from math import sqrt, exp

def push(s,a): s.append(a)
def pop(s): return s.pop()

def execute(p):
    s = list()
    it = enumerate(p)
    for i, op in it:
        if op == 'PUSH': _, a = next(it); push(s, a);         
        elif op == 'POP':  a = pop(s); 
        elif op == 'SQRT': a = pop(s); c = sqrt(a); push(s, c);
        elif op == 'EXP':  a = pop(s); c = exp(a); push(s, c);
        elif op == 'ADD':  a = pop(s); b = pop(s); c = b+a; push(s, c);
        elif op == 'MULT': a = pop(s); b = pop(s); c = b*a; push(s, c);
        elif op == 'DIV':  a = pop(s); b = pop(s); c = b/a; push(s, c);
        elif op == 'MOD':  a = pop(s); b = pop(s); c = b%a; push(s, c);
        elif op == 'POW':  a = pop(s); b = pop(s); c = b^a; push(s, c);
        else:
            raise Exception('instruction malformed, aborting')
        print(i, op, s)
    return s

def read(f):
    program = list()
    for line in sys.stdin:
        ops = line.strip().split()
        if ops[0] == 'PUSH':
            if len(ops) == 2:
                ops[1] = int(ops[1])
            else:
                raise Exception('missing value for PUSH')
        program.extend(ops)    
    # post condition ???
    return program
 
program = read(sys.stdin)
ans = execute(program)
print('Ans:',*ans)