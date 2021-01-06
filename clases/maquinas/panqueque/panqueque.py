# Panqueque: A simple simulator of a Stack Machine
#
# Adapted from the Stack Machine proposed by Nakano et al. (2008)
#
# Code based on the adaptation of the PL0 Machine (Wirth, 1976) by Anthony 
#   Aaby (1995)
#
# Autor: Diego Caro
#
# References:
#
#   Nakano, K.; Ito, Y., Processor, Assembler, and Compiler Design Education
#     Using an FPGA, Parallel and Distributed Systems, 2008. ICPADS '08. 14th 
#     IEEE International Conference on; 8-10 Dec. 2008 pages: 723 - 728 (Nakano,
#     K.; Ito, Y.; Dept. of Inf. Eng., Hiroshima Univ., Higashi-Hiroshima, Japan)
#
#   Nakano, K.; Kawakami, K.; Shigemoto, K.; Kamada, Y.; Ito, Y. A Tiny
#     Processing System for Education and Small Embedded Systems on the FPGAs,
#     Embedded and Ubiquitous Computing, 2008. EUC '08. IEEE/IFIP International
#     Conference, Dec. 2008 pages: 472 - 479 
# 
#    Niklaus Wirth, Algorithms + Data Structures = Programs Prentice-Hall,
#      Englewood Cliffs, N.J., 1976.
#
#    Anthony Aaby, Compiler Construction using Flex and Bison (draft year2005).
#    Available at https://web.archive.org/web/20080421194011/http://cs.wwc.edu/~aabyan/464/Book/StackMachine.html

import sys
import re
from math import exp

class Panqueque:
    def __init__(self, filename):
        # main stack
        self.stack = [0]*32
        self.code = [0]*32
        self.label = dict()
        self.mem = [0]*32
        self.top = 0
        self.pc = 0

        #regexp = "^([A-Z]{3,5})[ \t]*([\-0-9]*)";
        regexp = "^[ \t]*((?P<label>[A-Za-z]+):|(?P<op>[A-Z]{2,5}))[ \t]*(?P<arg>[\-0-9A-Za-z]*)"
        pattern = re.compile(regexp)
        
        file = open(filename, 'r')

        j = 0
        for i,line in enumerate(file):
            matcher = pattern.match(line)
            if matcher is not None:
                op = matcher.group('op') #matcher[1] 
                arg = matcher.group('arg') #matcher[4]
                label = matcher.group('label')
                
                if label:
                    self.label[label] = j
                    continue
                    
                self.code[j] = (op, arg, i) 
                #print(self.code[j])
                j += 1
        
    def dump(self):
        print()
        print(self.stack[1:self.top+1])
        print()

    def run(self, verbose=False):
        pc = self.pc
        code = self.code
        stack = self.stack
        top = self.top
        mem = self.mem
        label = self.label
        
        while True:
            (op, arg, i) = code[pc]
            pc += 1
            
            # executing     
            if op == 'PUSH':
                if len(arg) > 0: top += 1; stack[top] = int(arg); 
                else: print('missing value for PUSH, aborting'); break
            elif op == 'POP':  mem[int(arg)] = stack[top]; top -= 1;
            elif op == 'LOAD': top += 1; stack[top] = mem[int(arg)]; 
            elif op == 'EXP':  stack[top] = exp(stack[top]); 
            elif op == 'ADD':  stack[top-1] = stack[top-1] + stack[top]; top -= 1; 
            elif op == 'MULT': stack[top-1] = stack[top-1] * stack[top]; top -= 1; 
            elif op == 'SUB':  stack[top-1] = stack[top-1] - stack[top]; top -= 1;
            elif op == 'DIV':  stack[top-1] = stack[top-1] / stack[top]; top -= 1;
            elif op == 'DIVI':  stack[top-1] = stack[top-1] // stack[top]; top -= 1;
            elif op == 'MOD':  stack[top-1] = stack[top-1] % stack[top]; top -= 1;
            elif op == 'POW':  stack[top-1] = stack[top-1] ** stack[top]; top -= 1;
            elif op == 'EQ':   stack[top-1] = int(stack[top-1] == stack[top]); top -= 1;
            elif op == 'GT':   stack[top-1] = int(stack[top-1] > stack[top]); top -= 1;
            elif op == 'LT':   stack[top-1] = int(stack[top-1] < stack[top]); top -= 1;
            elif op == 'READ': top += 1; stack[top] = int(input());
            elif op == 'WRITE': print(stack[top]); top -= 1;
            elif op == 'JUMP': 
                if arg not in label: print('label not found, aborting'); break
                pc = label[arg]; 
            elif op == 'JUMPZ':
                if arg not in label: print('label not found, aborting'); break
                if stack[top] == 0: pc = label[arg];
                top -= 1;
            elif op == 'HALT': break
#            elif op == 'SQRT': stack[top] = sqrt(stack[top]);
#            elif op == 'BAND': stack[top-1] = stack[top-1] & stack[top]; top -= 1; # bitwise and
#            elif op == 'BXOR': stack[top-1] = stack[top-1] ^ stack[top]; top -= 1; # bitwise xor
#            elif op == 'SHFL': stack[top-1] = stack[top-1] << stack[top]; top -= 1; # shift left
#            elif op == 'SHFR': stack[top-1] = stack[top-1] >> stack[top]; top -= 1; # shift right            
            else:
                print('instruction malformed, aborting'); break

            if top < 0: print('stack underflow, aborting'); break
                
            # print(i, op, arg, top, stack[1:top+1], sep='\t')
            
            pc = pc & 0xFF;            # don't let pc overflow an 8-bit integer

        self.pc = pc # save last pc to attribute            
        self.top = top
        
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
        print("PANQQ:   invalid command-line options", file=sys.stderr)
        print("usage: panqq.py [--verbose] filename.pan [pc]", file=sys.stderr)
        sys.exit(-1)

    pan = Panqueque(filename)
    pan.run(isVerbose)

    if isVerbose:
        print()
        print('---------------------------------------')
        print('Stack Dump of Panqueque After Executing')
        print('---------------------------------------')
        pan.dump()