from re import subn
from sys import argv
import math

def allLines(program):
    fstr = open(filename)                  
    lines = 0
    buf_size = 1024 * 1024
    read_f = f.read # loop optimization
    buf = read_f(buf_size)
    while buf:
        lines += buf.count('\n')
        buf = read_f(buf_size)
    return lines

def allComments(program):
    fstr = open(path).read()
    return re.subn('(/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+/)|(//.*)',"",fstr)[1]
    
def percentage(part,whole):
    return 100 * float(part)/float(whole)
    
def main(program):
    total = allLines(program)
    comments = allComments
    print(percentage(comments,total))

if __name__=='__main__':
    # confirm that program is supplied with a file to analyze
    if (len(argv) != 2):
        print('No root directory supplied! Please supply a directory path!')
    else:
        program = argv[1]
        main(program)
