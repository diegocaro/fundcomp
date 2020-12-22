# Simulación máquina de stack
# Código basado en implementación de Alejandro Cisterna Villalobos
# y en http://ebook.pldworld.com/-huihoo-/book/compiler-construction-using-flex-and-bison/StackMachine.html
# Autor: Diego Caro

from math import sqrt, exp

def push(s,a): s.append(a)
def pop(s): return s.pop()

def main(f):
    s = list()
    for i,line in enumerate(f):
        # decoding
        op, *a = line.strip().split()
        # executing     
        if op == 'PUSH':
            if len(a) == 1: a = int(*a); push(s, a);
            else: raise Exception('missing value for PUSH')
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
        
#if __name__ == "__main__":
#import sys
#    infile = sys.stdin
#    if len(sys.argv) > 1 and sys.argv[1] != '-':
#        infile = open(sys.argv[1], 'r')
#         
#    main(infile)
