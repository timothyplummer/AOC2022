from curses.ascii import islower
from difflib import Match
from distutils.log import error
from http.client import FORBIDDEN


def read_input_file(filepath:str,function)->list[int]:
    with open(filepath, 'r') as file1:
        Lines = file1.readlines()
        output = []
        for line in Lines:
            num = function(line)
            output = output + [num]
    return output

def convert_to_int(line):
    if  line !=  '\n':
        num = int(line)
    else:
        num = 0
    return num
        
def day_1():
    lines = read_input_file('Inputs/Day1.txt',convert_to_int)
    elves = [0]
    for line in lines:
        if line == 0:
            elves = elves+[0]
        else:
            elves[-1]=elves[-1]+line
    elves.sort(reverse=True)
    print(sum(elves[0:3]))

def convert_to_RPS_score(line):
    if 'X' in line:
        num=0
        if 'A' in line:
            num = num+3
        elif 'B' in line:
            num = num+1
        elif 'C' in line:
            num = num+2
        else:
            error("Don't know which RPS enemy threw.")
    elif 'Y' in line:
        num=3
        if 'A' in line:
            num = num+1
        elif 'B' in line:
            num = num+2
        elif 'C' in line:
            num = num+3
        else:
            error("Don't know which RPS enemy threw.")
    elif 'Z' in line:
        num=6
        if 'A' in line:
            num = num+2
        elif 'B' in line:
            num = num+3
        elif 'C' in line:
            num = num+1
        else:
            error("Don't know which RPS enemy threw.")
    else:
        error("Don't know which RPS you threw.")
    return num

def day_2():
    lines = read_input_file('Inputs/Day2.txt',convert_to_RPS_score)
    print(sum(lines))

def trim(line):
    return line.strip()

def day_3():
    lines=read_input_file('Inputs/Day3.txt',trim)
    match = []
    for line in lines:
        s1 = slice(0,len(line)//2)
        s2 = slice(len(line)//2,len(line))
        l1 = line[s1]
        l2 = line[s2]
        for c in l1:
            if c in l2:
                match = match + [c]
                break
    score = 0
    for m in match:
        if islower(m):
            output = ord(m)-ord('a')+1
        else:
            output = ord(m)-ord('A')+26+1    
        score = score +output
    print(score)
if __name__ == '__main__':
    #day_1()
    #day_2()
    day_3()