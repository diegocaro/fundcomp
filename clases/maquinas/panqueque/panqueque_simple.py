from math import exp

def push(s,a): s.append(a)
def pop(s): return s.pop()

def main(f):
    s = list()
    for i, line in enumerate(f):
        # decoding
        inst = line[:line.find('#')].strip().split()
        # skip if line is a comment
        if len(inst) == 0: continue
        op, *a = inst
        # executing     
        if op == 'PUSH':
            if len(a) == 1: a = float(*a); push(s, a);
            else: raise Exception('missing value for PUSH')
        elif op == 'POP':  a = pop(s); 
        elif op == 'EXP':  a = pop(s); c = exp(a); push(s, c);
        elif op == 'ADD':  a = pop(s); b = pop(s); c = b+a; push(s, c);
        elif op == 'MULT': a = pop(s); b = pop(s); c = b*a; push(s, c);
        elif op == 'SUB':  a = pop(s); b = pop(s); c = b-a; push(s, c);
        elif op == 'DIV':  a = pop(s); b = pop(s); c = b/a; push(s, c);
        elif op == 'MOD':  a = pop(s); b = pop(s); c = b%a; push(s, c);
        elif op == 'DUP':  a = pop(s); push(a); push(a);
        elif op == 'OVER': a,b = pop(s), pop(s); push(b); push(a); push(b)
        elif op == 'SWAP': a,b = pop(s), pop(s); push(a); push(b)
        elif op == 'READ': a = float(input()); push(s, a)
        elif op == 'SEND': print(pop(s));
        else: raise Exception('instruction malformed, aborting')
        
if __name__ == "__main__":
    import sys
    infile = open(sys.argv[1], 'r')         
    main(infile)