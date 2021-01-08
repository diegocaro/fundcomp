from math import exp
def push(s,a): s.append(a)
def pop(s): return s.pop()
def main(f):
    code = list() # code
    lbl = dict() # labels
    for line in f: # decoding, and skip comments
        line = line[:line.find('#')].strip()
        label = line[:line.find(':')+1].strip()
        if len(label) > 0: lbl[label[:-1]] = len(code); continue
        if len(line) > 0: code.append(line.split())
    pc = 0
    s = list() # stack
    while True: # executing loop
        op, *arg = code[pc]
        pc += 1   
        if op == 'PUSH':   arg = float(*arg); push(s, arg);
        elif op == 'POP':  pop(s); 
        elif op == 'EXP':  push(s, exp(pop(s)));
        elif op == 'ADD':  push(s, pop(s) + pop(s));
        elif op == 'MULT': push(s, pop(s) * pop(s));
        elif op == 'SUB':  push(s, pop(s) - pop(s));
        elif op == 'DIV':  a = pop(s); push(s, pop(s) / a);
        elif op == 'MOD':  push(s, pop(s) % pop(s));
        elif op == 'DUP':  a = pop(s); push(s,a); push(s,a);
        elif op == 'OVER': a,b = pop(s), pop(s); push(s,b); push(s,a); push(s,b)
        elif op == 'SWAP': a,b = pop(s), pop(s); push(s,a); push(s,b)
        elif op == 'EQ':   push(s, int(pop(s) == pop(s)))
        elif op == 'LT':   a=pop(s); push(s, int(pop(s) < a))
        elif op == 'READ': a = float(input()); push(s, a)
        elif op == 'SEND': print(pop(s));
        elif op == 'JUMP': pc = lbl[arg[0]]; 
        elif op == 'JMPZ':
            if pop(s) == 0: pc = lbl[arg[0]];
        else: print(op); raise Exception('instruction malformed, aborting')
        if pc >= len(code): break
if __name__ == "__main__":
    import sys
    infile = open(sys.argv[1], 'r')         
    main(infile)