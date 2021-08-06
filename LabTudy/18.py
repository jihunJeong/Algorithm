def split(string):
    count = 0
    u, v = "", ""
    for s in string:
        if s =="(":
            count += 1
        else :
            count -= 1
        u += s
        if count == 0:
            break
    v = string[len(u):]
    return u, v

def check(string):
    stack = []
    for s in string:
        if s == "(":
            stack.append(s)
        else :
            if stack:
                stack.pop()
            else :
                return False
    return True

def recurrent(string):
    if string == "":
        return ""
    u, v = split(string)
    if check(u):
        return u + recurrent(v)
    else :
        ans = "(" + recurrent(v) + ")"
        for i in range(1, len(u)-1):
            if u[i] == "(":
                ans += ")"
            else :
                ans += "("
        return ans
        
def solution(p):
    if p == "":
        return p
    answer = recurrent(p) 
    return answer