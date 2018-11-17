from copy import copy, deepcopy

layer = []
length = 151
itirNum = 200
rule = 120

def initLayer(length, layer):
    for n in range(0, length):
        layer.append(0)
    layer[round(len(layer)/2)] = 1

def step(rule, layer, length):
    rulestr = str(bin(rule))[2:]
    ruleformatted = []
    while len(rulestr) < 8:
        rulestr = '0' + rulestr
    for n in rulestr:
        ruleformatted.append(int(n))
    templayer = []
    initLayer(length, templayer)
    for n in range(0, len(layer) - 2):
        templayer[n+1] = ruleformatted[layer[n]*4 + layer[n+1]*2 + layer[n+2]]
    copylst(templayer, layer)

def copylst(lst1, lst2):
    for n in range(0, len(lst1)):
        lst2[n] = lst1[n] 

def printlyr(layer):
    outputstr = ""
    for n in layer:
        if n == 0:
            outputstr += " "
        else:
            outputstr += "@"
    print(outputstr)
            

length = int(input("width: "))
rule = int(input("rule: "))
itirNum = int(input("number of itirations: "))

initLayer(length, layer)
printlyr(layer)
for n in range(0, itirNum):
    step(rule, layer, length)
    printlyr(layer)