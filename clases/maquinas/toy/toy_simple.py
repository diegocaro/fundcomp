# Based on Computer Science An Interdisciplinary Approach Book
# https:#introcs.cs.princeton.edu/java/64simulator/TOY.java.html
# https:#introcs.cs.princeton.edu/java/lectures/keynote/CS.18.MachineII.pdf
# https://introcs.cs.princeton.edu/java/62toy/cheatsheet.txt
# Autor: Diego Caro

def main(f):
    pc = 0x10 # contador de programa
    R = [0] * 16 # registros
    M = [0] * 256 # memoria principal
    
    for i in range(0x10, 0xFF): # leer memoria
        M[i] = hex(f.readline().strip()) & 0xFF
        l = next(l)
    
    while True:
        ir = M[pc]  # fetch
        pc += 1     # increment
        
        op   = (ir >> 12) &  0xF;   # get opcode (bits 12-15)
        d    = (ir >>  8) &  0xF;   # get dest   (bits 08-11)
        s    = (ir >>  4) &  0xF;   # get s      (bits 04-07)
        t    = ir         &  0xF;   # get t      (bits 00-03)
        addr = ir         & 0xFF;   # get addr   (bits 00-07)
        
        if op == 0: break                             # halt
        elif op ==  1: R[d] = R[s] +  R[t];           # add
        elif op ==  2: R[d] = R[s] -  R[t];           # subtract
        elif op ==  3: R[d] = R[s] &  R[t];           # bitwise and
        elif op ==  4: R[d] = R[s] ^  R[t];           # bitwise xor
        elif op ==  5: R[d] = R[s] << R[t];           # shift left
        elif op ==  6: R[d] = (short) R[s] >> R[t];   # shift right
        elif op ==  7: R[d] = addr;                   # load address
        elif op ==  8: R[d] = mem[addr];              # load
        elif op ==  9: mem[addr] = R[d];              # store
        elif op == 10: R[d] = mem[R[t] & 255];        # load indirect
        elif op == 11: mem[R[t] & 255] = R[d];        # store indirect
        elif op == 12: if (R[d] == 0) pc = addr;      # branch if zero
        elif op == 13: if (R[d] >  0) pc = addr;      # branch if positive
        elif op == 14: pc = R[d];                     # jump indirect
        elif op == 15: R[d] = pc; pc = addr;          # jump and link
            
#if __name__ == "__main__":
#    import sys
#    infile = sys.stdin
#    if len(sys.argv) > 1 and sys.argv[1] != '-':
#        infile = open(sys.argv[1], 'r')        
#    main(infile)
