#!/usr/bin/env python3

# ************************************************************************/
#   Execution: python3 toy.py [--verbose] filename.toy 
# 
#   We use variables of type int to store the TOY registers, main
#   memory, and program counter even though in TOY these quantities
#   are 16 and 8 bit integers. Python does not have an 8-bit unsigned
#   type. The type short is not available in Python. Instead, we are
#   careful to treat all of the variable as if they were the appropriate
#   type so that the behavior truly models the TOY machine.
# 
#   % more multiply.toy
#   10: 8AFF   read R[A]
#   11: 8BFF   read R[B]
#   12: 7C00   R[C] <- 0000
#   13: 7101   R[1] <- 0001
#   14: CA18   if (R[A] == 0) goto 18
#   15: 1CCB   R[C] <- R[C] + R[B]
#   16: 2AA1   R[A] <- R[A] - R[1]
#   17: C014   goto 14
#   18: 9CFF   write R[C]
#   19: 0000   halt                        
# 
#   % python3 toy.py multiply.toy
#   0002
#   0004
#   0008
# 
#   % python3 toy.py --verbose multiply.toy
#   [core dump]
#   0002
#   0004
#   0008
#   [core dump]
# 
# ************************************************************************/
# Author: Diego Caro <diego.caro.a at usach.cl>

# Based on Computer Science An Interdisciplinary Approach Book
#   https:#introcs.cs.princeton.edu/java/64simulator/TOY.java.html
#   https:#introcs.cs.princeton.edu/java/lectures/keynote/CS.18.MachineII.pdf
#   https:#introcs.cs.princeton.edu/java/62toy/cheatsheet.txt


import re
import numpy as np
# return a 4-digit hex string corresponding to 16-bit integer n    
def toHex(n):
    return '{0:04X}'.format(n & 0xFFFF)

# return a 16-bit integer corresponding to the 4-digit hex string s
def fromHex(s):
    return int(s, base=16) & 0xFFFF

# write to an array of hex integers, 8 per line to standard output
def show(a):
    for i in range(len(a)):
        print(toHex(a[i]) + " ", end='')
        if i % 8 == 7: print()

# return a short integer following the two complement rule
def toShort(n):
    if n > 0x0FFF:
        n = n - 0xFFFF - 1
    return n

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
            if op == 0x0: break

            # stdin 
            if ((addr == 255 and op == 8) or (reg[t] == 255 and op == 10)):
                mem[255] = fromHex(input());

            # Execute
            if   op == 0x1: reg[d] = reg[s] +  reg[t]           # add
            elif op == 0x2: reg[d] = reg[s] -  reg[t]           # subtract
            elif op == 0x3: reg[d] = reg[s] &  reg[t]           # bitwise and
            elif op == 0x4: reg[d] = reg[s] ^  reg[t]           # bitwise xor
            elif op == 0x5: reg[d] = reg[s] << reg[t]           # shift left
            elif op == 0x6: reg[d] = toShort(reg[s] >> reg[t])  # shift right
            elif op == 0x7: reg[d] = addr                       # load address
            elif op == 0x8: reg[d] = mem[addr]                  # load
            elif op == 0x9: mem[addr] = reg[d]                  # store
            elif op == 0xA: reg[d] = mem[reg[t] & 0xFF]         # load indirect
            elif op == 0xB: mem[reg[t] & 0xFF] = reg[d]         # store indirect
            elif op == 0xC:                                     # branch if zero 
                if toShort(reg[d]) == 0: pc = addr        
            elif op == 0xD:                                     # branch if positive
                if toShort(reg[d]) >  0: pc = addr         
            elif op == 0xE: pc = reg[d]                         # jump indirect
            elif op == 0xF: reg[d] = pc; pc = addr              # jump and link


            # stdout
            if ((addr == 0xFF and op == 0x9) or (reg[t] == 0xFF and op == 0xB)):
                print(toHex(mem[0xFF]));

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

    toy = Toy(filename, pc)
    
    
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
    