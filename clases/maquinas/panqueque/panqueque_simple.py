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
        elif op == 'SUB':  a = pop(s); b = pop(s); c = b-a; push(s, c);
        elif op == 'DIV':  a = pop(s); b = pop(s); c = b/a; push(s, c);
        elif op == 'MOD':  a = pop(s); b = pop(s); c = b%a; push(s, c);
        elif op == 'POW':  a = pop(s); b = pop(s); c = b^a; push(s, c);
        else:
            raise Exception('instruction malformed, aborting')
        print(i, op, s)
        
if __name__ == "__main__":
    import sys
    infile = open(sys.argv[1], 'r')         
    main(infile)