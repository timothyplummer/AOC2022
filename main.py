from curses.ascii import islower
import numpy as np
import re


def read_input_file(filepath: str, function) -> list[any]:
    with open(filepath, "r") as file1:
        Lines = file1.readlines()
        output = []
        for line in Lines:
            num = function(line)
            output = output + [num]
    return output


def convert_to_int(line):
    if line != "\n":
        num = int(line)
    else:
        num = 0
    return num


def day_1():
    lines = read_input_file("Inputs/Day1.txt", convert_to_int)
    elves = [0]
    for line in lines:
        if line == 0:
            elves = elves + [0]
        else:
            elves[-1] = elves[-1] + line
    elves.sort(reverse=True)
    print(sum(elves[0:3]))


def convert_to_RPS_score(line):
    if "X" in line:
        num = 0
        if "A" in line:
            num = num + 3
        elif "B" in line:
            num = num + 1
        elif "C" in line:
            num = num + 2
        else:
            ValueError("Don't know which RPS enemy threw.")
    elif "Y" in line:
        num = 3
        if "A" in line:
            num = num + 1
        elif "B" in line:
            num = num + 2
        elif "C" in line:
            num = num + 3
        else:
            ValueError("Don't know which RPS enemy threw.")
    elif "Z" in line:
        num = 6
        if "A" in line:
            num = num + 2
        elif "B" in line:
            num = num + 3
        elif "C" in line:
            num = num + 1
        else:
            ValueError("Don't know which RPS enemy threw.")
    else:
        ValueError("Don't know which RPS you threw.")
    return num


def day_2():
    lines = read_input_file("Inputs/Day2.txt", convert_to_RPS_score)
    print(sum(lines))


def trim(line):
    return line.strip()


def day_3():
    lines = read_input_file("Inputs/Day3.txt", trim)
    match = []
    for line in lines:
        s1 = slice(0, len(line) // 2)
        s2 = slice(len(line) // 2, len(line))
        l1 = line[s1]
        l2 = line[s2]
        for c in l1:
            if c in l2:
                match = match + [c]
                break
    score = 0
    for m in match:
        output = PackingScore(m)
        score = score + output
    print(score)
    score2 = 0
    for groups in [lines[i : i + 3] for i in range(0, len(lines), 3)]:
        for c in groups[0]:
            if c in groups[1] and c in groups[2]:
                output = PackingScore(c)
        score2 = score2 + output
    print(score2)


def PackingScore(m):
    if islower(m):
        output = ord(m) - ord("a") + 1
    else:
        output = ord(m) - ord("A") + 26 + 1
    return output


def intArrayBuilder(line):
    arr = []
    for cha in line:
        if cha != "\n":
            arr = arr + [int(cha)]
    return arr


def day_10_2021():
    octopusGrid = np.array(read_input_file("sample.txt", intArrayBuilder))
    print((octopusGrid + 2) >= 10)
    


def pair_reader(line):
    matches = re.search(r"(\d*)-(\d*),(\d*)-(\d*)", line)
    output = []
    for m in matches.groups():
        num = int(m)
        output = output + [num]
    return output


def day_4():
    lines = read_input_file("Inputs/Day4.txt", pair_reader)
    countcontains = 0
    countoverlap = 0
    for arr in lines:
        elf1 = range(arr[0], arr[1] + 1)
        elf2 = range(arr[2], arr[3] + 1)
        if (set(elf1).issubset(set(elf2))) or (set(elf2).issubset(elf1)):
            countcontains += 1
        if range(max(elf1[0], elf2[0]), min(elf1[-1], elf2[-1]) + 1):
            countoverlap += 1
    print(f"number of sections contains: {countcontains}")
    print(f"number of sections overlap: {countoverlap}")


def day_5():
    stacks, instuctions = read_crates_file("Inputs/Day5.txt")
    for line in instuctions:
        matches = re.search(r"move (\d*) from (\d*) to (\d*)", line)
        output = []
        for m in matches.groups():
            num = int(m)
            output = output + [num]
        tempStack = []
        for i in range(int(output[0])):
            tempStack.append(stacks[int(output[1])-1].pop())
        print(tempStack)
        for i in range(int(output[0])):
                stacks[int(output[2])-1].append(tempStack.pop())
    out = ""
    for s in stacks:
        out = out + s[-1]
    print(out)
    
def read_crates_file(filepath:str):
    with open(filepath, "r") as file1:
        Lines = file1.readlines()
        outputDrawing = []
        outputInstuctions = []
        afterEmptyLine = False
        for line in Lines:
            if line.strip() == "":
                afterEmptyLine = True
                continue
            if afterEmptyLine:
                outputInstuctions = outputInstuctions + [line]
            else:
                outputDrawing = outputDrawing + [line]
    stacks = []           
    for  i, crateNum in enumerate(outputDrawing[-1]):
        if crateNum!=' ':
            stack = []
            for level in reversed(outputDrawing[0:-1]): 
                if level[i]!= ' ' and level[i]!= "\n":
                    stack = stack+[level[i]]
            stacks.append(stack)    
            print(f"{stacks[0:-1]}")
    stacks.pop()
    print(stacks)
    return (stacks, outputInstuctions)


def day_6():
    lines = read_input_file("Inputs/Day6.txt",str)
    n=14
    for i in range(len(lines[0])-n+1):
        batch = lines[0][i:i+n]
        if uniqueCharacters(batch):
            print(i+n)
            break
    
def uniqueCharacters(st):
 
    # Using sorting
    st = sorted(st)
 
    for i in range(len(st)-1):
 
        # if at any time, 2 adjacent
        # elements become equal,
        # return false
        if (st[i] == st[i + 1]) :
            return False
             
    return True 
if __name__ == "__main__":
    # day_1()
    # day_2()
    # day_3()
    # day_4()
    # day_5()
    day_6()
    #day_10_2021()
