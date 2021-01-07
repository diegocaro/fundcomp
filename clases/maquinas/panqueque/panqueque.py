# Panqueque: A simple simulator of a Canonical Stack Machine
#
# Author: Diego Caro
# Notes: This is implementation is a work-in-progress, as it still need
#        a return stack and its operations to be a fully Turing Complete
#        machine. Hopefully it will be ready during 2021.
#
# This is an adaptation of the Canonical Stack Machine presented by Koopman 
# (1989, chapter 3), and the Forth programming language by Moore (1974).
#
# Heavily inspired by the work of Nakano et al. (2008), the PL0 Machine by
# and the S-machine, an adaptation of the PL0 Machine (Wirth, 1976) by Anthony 
# Aaby (1995).
#
# If you want to implement a real hardware Stack Machine I suggest you to check
# the FPGA design by Nanako et al. (2008).
# 
# References:
#   Koopman, P. Stack Computers: the new wave, Ellis Horwood, 1989.
#      Available at https://users.ece.cmu.edu/~koopman/stack_computers/index.html
#
#   Moore, C. H. (1974). FORTH: a new way to program a mini computer. 
#      Astronomy and Astrophysics Supplement Series, 15, 497.
#      Available at http://articles.adsabs.harvard.edu/pdf/1974A%26AS...15..497M
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
#    Niklaus Wirth, Algorithms + Data Structures = Programs, Prentice-Hall,
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
        self.data_stack = [0]*256
        self.code = [0]*256
        self.size_code = 0
        self.label = dict()
        self.top = 0
        self.pc = 0

        regexp = "^[ \t]*((?P<label>[A-Za-z]+):|(?P<op>[A-Z]{2,4}))[ \t]*(?P<arg>[\-\.0-9A-Za-z]*)"
        pattern = re.compile(regexp)
        
        file = open(filename, 'r')

        j = 0
        for i,line in enumerate(file):
            matcher = pattern.match(line)
            if matcher is not None:
                op = matcher.group('op') 
                arg = matcher.group('arg') 
                label = matcher.group('label')        
                if label:
                    self.label[label] = j
                    continue
                    
                self.code[j] = (op, arg, i) 
                #print(self.code[j])
                j += 1
        self.size_code = j
        
    def dump(self):
        print()
        print(self.data_stack[1:self.top+1])
        print()

    def run(self, verbose=False):
        pc = self.pc
        code = self.code
        stack = self.data_stack
        top = self.top
        label = self.label
        
        while True:
            (op, arg, i) = code[pc]
            pc += 1
            
            # executing
            if op == 'PUSH':
                if len(arg) > 0: top += 1; stack[top] = int(arg); 
                else: print('missing value for PUSH, aborting'); break
            elif op == 'POP':  top -= 1;
            elif op == 'EXP':  stack[top] = exp(stack[top]); 
            elif op == 'ADD':  stack[top-1] = stack[top-1] + stack[top]; top -= 1; 
            elif op == 'MULT': stack[top-1] = stack[top-1] * stack[top]; top -= 1; 
            elif op == 'SUB':  stack[top-1] = stack[top-1] - stack[top]; top -= 1;
            elif op == 'DIV':  stack[top-1] = stack[top-1] / stack[top]; top -= 1;
            elif op == 'MOD':  stack[top-1] = stack[top-1] % stack[top]; top -= 1;
            # More stack ops
            elif op == 'DUP':  top += 1; stack[top] = stack[top-1]
            elif op == 'OVER': top += 1; stack[top] = stack[top-2]
            elif op == 'SWAP': tmp = stack[top]; stack[top] = stack[top-1]; stack[top-1] = tmp
            # condition ops
            elif op == 'EQ':   stack[top-1] = int(stack[top-1] == stack[top]); top -= 1;
            elif op == 'GT':   stack[top-1] = int(stack[top-1] > stack[top]); top -= 1;
            # branch ops
            elif op == 'JUMP': 
                if arg not in label: print('label not found, aborting'); break
                pc = label[arg]; 
            elif op == 'JMPZ':
                if arg not in label: print('label not found, aborting'); break
                if stack[top] == 0: pc = label[arg];
                top -= 1;
            # input/output ops
            elif op == 'READ': top += 1; stack[top] = float(input());
            elif op == 'SEND': print(stack[top]); top -= 1;
            else:
                print('instruction malformed, aborting'); break

            if top < 0: print('stack underflow, aborting'); break
                
            # print(i, op, arg, top, stack[1:top+1], sep='\t')
            
            # halt if we reached the end of CODE
            if pc >= self.size_code: break
            
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