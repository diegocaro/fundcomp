# Simulación máquina de stack
# Código basado en implementación de Alejandro Cisterna Villalobos
# y en http://ebook.pldworld.com/-huihoo-/book/compiler-construction-using-flex-and-bison/StackMachine.html
# Autor: Diego Caro

import sys
import re
from math import sqrt, exp

def push(s,a): s.append(a)
def pop(s): return s.pop()

# main stack
s = list()

def run(f, verbose=False):
    global s
    
    regexp = "^([A-Za-z]{3,4})[ \t]*([\-0-9]*)";
    pattern = re.compile(regexp)
    
    for i,line in enumerate(f):
        matcher = pattern.match(line)

        # skip empty line
        if matcher is None: continue

        # decoding
        op = matcher[1]
        a = matcher[2]
        
        if verbose: print(i, op, a, end=' ')

        # executing     
        if op == 'PUSH':
            if len(a) > 0: a = int(a); push(s, a);
            else: raise Exception('missing value for PUSH')
        elif op == 'POP':  a = pop(s); 
        elif op == 'SQRT': a = pop(s); c = sqrt(a); push(s, c);
        elif op == 'EXP':  a = pop(s); c = exp(a); push(s, c);
        elif op == 'ADD':  a = pop(s); b = pop(s); c = b+a; push(s, c);
        elif op == 'MULT': a = pop(s); b = pop(s); c = b*a; push(s, c);
        elif op == 'SUB':  a = pop(s); b = pop(s); c = b-a; push(s, c);
        elif op == 'DIV':  a = pop(s); b = pop(s); c = b/a; push(s, c);
        elif op == 'MOD':  a = pop(s); b = pop(s); c = b%a; push(s, c);
        elif op == 'POW':  a = pop(s); b = pop(s); c = b^a; push(s, c);
        else:
            raise Exception('instruction malformed, aborting')
        if verbose: print(s)

if __name__ == "__main__":
    import sys

    # -v or --verbose is an optional first command-line argument
    isVerbose = False
    if len(sys.argv) > 1 and sys.argv[1] in ('-v','--verbose'):
        isVerbose = True

    # the filename is the next command-line argument
    filename = None
    if not isVerbose and len(sys.argv) > 1: filename = sys.argv[1]
    if     isVerbose and len(sys.argv) > 2: filename = sys.argv[2]
    
    # no command-line arguments
    if (len(sys.argv) == 1):
        print("STACK:   invalid command-line options", file=sys.stderr)
        print("usage: stack.py [--verbose] filename.in", file=sys.stderr)
        sys.exit(-1)
    
    program = open(filename, 'r')
    run(program, isVerbose)
    program.close()
    
    if len(s) > 1:
        print("Error, stack has more than one element", file=sys.stderr)
        print('Stack:', s, file=sys.stderr)
        sys.exit(-1)
        
    last = pop(s)
    print(last)