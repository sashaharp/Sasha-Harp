import sys
import io

def bfeval(bfStr, bfarr = [0], bfptr = 0, debug = False, ln = -1, bp = -1, ot = False):
    lst = ['+', '-', '>', '<', '[', '.', ',']
    ptr = bfptr
    arr = bfarr
    evi = 0
    while evi < len(bfStr):
        if debug & lst.__contains__(bfStr[evi]):
            print(str(evi) + ") Current state:")
            print(arr)
            print(" "*(ptr*3+1) + "^")
            print("next operation: ")
            print(bfStr)
            print(" "*evi + "^")
        if evi == bp:
            print("Breakpoint reached")
            print("Current state:")
            print(arr)
            print(" "*(ptr*3+1) + "^")
            print("next operation: ")
            print(bfStr)
            print(" "*evi + "^")
            arr, ptr, t = bfeval(input("Commands (in bf): "), arr, ptr)
            if ot:
                bp = -1
        if bfStr[evi] == '+':
            arr[ptr] += 1
        elif bfStr[evi] == '-':
            arr[ptr] -= 1
        elif bfStr[evi] == '>':
            ptr += 1
            if ptr == len(arr):
                arr.append(0)
        elif bfStr[evi] == '<':
            ptr -= 1
        elif bfStr[evi] == '.':
            print(arr[ptr])
        elif bfStr[evi] == ',':
            arr[ptr] = int(input("enter a number: "))
        elif bfStr[evi] == '[':
            tmp = int(evi)
            lnc = 0
            cnt = 1
            evi += 1
            while cnt > 0:
                if bfStr[evi] == '[':
                    cnt += 1
                elif bfStr[evi] == ']':
                    cnt -= 1
                evi += 1
            evi -= 1
            while arr[ptr] != 0:
                if (ln > 0) & (lnc >= ln):
                    print("exception: number of loops exceeded the maximum!")
                    exit()
                arr, ptr, bp = bfeval(bfStr[tmp+1:evi], list(arr), ptr, debug, ln, bp-tmp-1)
                lnc += 1
        if ptr < 0:
            print("exception: negative pointer in")
            print(bfStr)
            print(" "*evi + "^")
            exit()
            return [0], 0
        evi += 1

    return list(arr), ptr, bp

if len(sys.argv) < 2:
    print("syntax: python3 " + sys.argv[0] + " [BF_CODE] [arguments]")
    print("python3 " + sys.argv[0] + " -h for more information")
    exit()
if sys.argv[1] == "-h":
    print("syntax: python3 " + sys.argv[0] + " [-f FILENAME] [BF_CODE] [arguments]")
    print("arguments:")
    print("    -h    help")
    print("    -d    show debug information")
    print("    -ln   set maximum number of loops before crash")
    print("    -bn   set breakpoint at the nth character")
    print("    -obn  set a one-time breakpoint at the nth character")
    print("    -f    get BF code from a file")
bfc = ""
if sys.argv[1] == "-f":
    if len(sys.argv) < 3:
        print("command syntax error!")
        exit()
    bfc = str(io.FileIO(sys.argv[2]).readall())
else:
    bfc = sys.argv[1]

debug = False
ln = -1
bp = -1
ot = False
for s in sys.argv:
    if s == "-d":
        debug = True
    if (len(s) > 1) & (s[1] == 'l'):
        ln = int(s[2:])
    if (len(s) > 1) & (s[1] == 'b'):
        bp = int(s[2:])
    if (len(s) > 1) & (s[1] == 'o'):
        bp = int(s[3:])
        ot = True


bfeval(bfc, debug=debug, ln = ln, bp = bp, ot = ot)