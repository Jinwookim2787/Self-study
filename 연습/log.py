import re

def parse1():
    for line in open("C:\코딩킴\연습\log.txt"):
        print(line.split("[")[1].split("]")[0])

def parse2():
    for line in open("C:\코딩킴\연습\log.txt", "r"):
        print(line.split()[3].strip("[]"))

def parse3():
    for line in open("C:\코딩킴\연습\log.txt", "r"):
        print(" ".join(line.split("[" or "]")[3:5]))

def parse4():
    for line in open("C:\코딩킴\연습\log.txt", "rw"):
        print(" ".join(line.split()[3:5]).strip("[]"))
  
def parse5():
    for line in open("C:\코딩킴\연습\log.txt"):
        print(re.split("\[|\]", line)[1])

#print(parse1())
#print(parse2())
#print(parse3())
#print(parse4())
print(parse5())


