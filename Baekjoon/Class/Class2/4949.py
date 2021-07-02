string = input()

while string != ".":
    s = []
    flag = True
    for c in string:
        if c == "(":
            s.append("(")
        elif c == "[":
            s.append("[")
        elif c == ")":
            if len(s) == 0 or s[-1] != "(":
                flag = False
                break
            else :
                s.pop()
        elif c == "]":
            if len(s) == 0 or s[-1] != "[":
                flag = False
                break
            else :
                s.pop()
    if flag and len(s) == 0:
        print("yes")
    else :
        print("no")

    string = input()