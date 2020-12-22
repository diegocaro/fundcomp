# Based on Computer Science An Interdisciplinary Approach Book
# https:#introcs.cs.princeton.edu/java/64simulator/TOY.java.html
# https:#introcs.cs.princeton.edu/java/lectures/keynote/CS.18.MachineII.pdf
# https:#introcs.cs.princeton.edu/java/62toy/cheatsheet.txt
# Author: Diego Caro

import re

def fromHex(s):
    return int(s, base=16) & 0xFFFF
    
def toHex(n):
    #return hex(n & 0xFFFF)
    return '{0:04X}'.format(n & 0xFFFF)

# write to an array of hex integers, 8 per line to standard output
def show(a):
    for i in range(len(a)):
        print(toHex(a[i]) + " ", end='')
        if i % 8 == 7: print()

class Toy:
    def __init__(self, filename, pc = 0x10):
        file = open(filename, 'r')
        self.pc = pc
        self.reg = [0]*16
        self.mem = [0]*256
        
        # Read in memory location and instruction.         
        # A valid input line consists of 2 hex digits followed by a 
        # colon, followed by any number of spaces, followed by 4
        # hex digits. The rest of the line is ignored.
        
        regexp = "^([0-9A-Fa-f]{2}):[ \t]*([0-9A-Fa-f]{4})";
        pattern = re.compile(regexp)
        for line in file:
            matcher = pattern.match(line)
            if matcher is not None:
                addr = fromHex(matcher[1])
                inst = fromHex(matcher[2])
                self.mem[addr] = inst

    # print core dump of TOY to standard output
    def dump(self):
         print("PC:")
         print("{0:02X}".format(self.pc))
         print()
         print("Registers:")
         show(self.reg);
         print()
         print("Main memory:")
         show(self.mem)
         print()
    
    def run(self):
        # to make code shorter
        pc = self.pc              
        mem = self.mem                  # mem is a reference of self.mem
        reg = self.reg                  # reg is a reference of self.reg
        
        while True:            
            # Fetch and parse
            inst = mem[pc]            # fetch next instruction
            pc += 1
            op   = (inst >> 12) &  15;   # get opcode (bits 12-15)
            d    = (inst >>  8) &  15;   # get dest   (bits  8-11)
            s    = (inst >>  4) &  15;   # get s      (bits  4- 7)
            t    = inst         &  15;   # get t      (bits  0- 3)
            addr = inst         & 255;   # get addr   (bits  0- 7)

            # halt
            if op == 0: break

            # stdin 
            if ((addr == 255 and op == 8) or (reg[t] == 255 and op == 10)):
                mem[255] = fromHex(input());

            # Execute
            if   op ==  1: reg[d] = reg[s] +  reg[t]           # add
            elif op ==  2: reg[d] = reg[s] -  reg[t]           # subtract
            elif op ==  3: reg[d] = reg[s] &  reg[t]           # bitwise and
            elif op ==  4: reg[d] = reg[s] ^  reg[t]           # bitwise xor
            elif op ==  5: reg[d] = reg[s] << reg[t]           # shift left
            elif op ==  6: reg[d] = reg[s] >> reg[t]           # shift right
            elif op ==  7: reg[d] = addr                       # load address
            elif op ==  8: reg[d] = mem[addr]                  # load
            elif op ==  9: mem[addr] = reg[d]                  # store
            elif op == 10: reg[d] = mem[reg[t] & 255]          # load indirect
            elif op == 11: mem[reg[t] & 255] = reg[d]          # store indirect
            elif op == 12:                                     # branch if zero 
                if reg[d] == 0: pc = addr        
            elif op == 13:                                     # branch if positive
                if reg[d] >  0: pc = addr         
            elif op == 14: pc = reg[d]                         # jump indirect
            elif op == 15: reg[d] = pc; pc = addr              # jump and link


            # stdout
            if ((addr == 255 and op == 9) or (reg[t] == 255 and op == 11)):
                print(toHex(mem[255]));

            reg[0] = 0;                # ensure reg[0] is always 0
            reg[d] = reg[d] & 0xFFFF;  # don't let reg[d] overflow a 16-bit integer
            pc = pc & 0xFF;            # don't let pc overflow an 8-bit integer
        
        self.pc = pc # save last pc to attribute
            
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
    
    # the initial value of the PC is an optional last command-line argument
    pc = 0x10
    if not isVerbose and len(sys.argv) > 2: pc = fromHex(sys.argv[2])
    if     isVerbose and len(sys.argv) > 3: pc = fromHex(sys.argv[3])

    toy = Toy(filename)
    
    
    if isVerbose:
        print('Core Dump of TOY Before Executing')
        print('---------------------------------------')
        toy.dump()
        print('Terminal')
        print('---------------------------------------')
        
    toy.run()
    
    if isVerbose:
        print('Core Dump of TOY After Executing')
        print('---------------------------------------')
        toy.dump()
    