from re import subn
from sys import argv
import math

def allLines(program):
    return sum(1 for line in open(program))

def allComments(program):
    fstr = open(program).read()
    return re.subn('(/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+/)|(//.*)',"",fstr)[1]
    
def percentage(part,whole):
    return 100 * float(part)/float(whole)
    
def main(program):
    total = allLines(program)
    comments = allComments(program)
    print(percentage(comments,total))

if __name__=='__main__':
    if (len(argv) != 2):
        print('No root directory supplied! Please supply a directory path!')
    program = argv[1]
    main(program)
