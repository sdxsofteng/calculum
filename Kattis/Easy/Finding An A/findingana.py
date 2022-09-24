s = input()
p = False
for l in s:
    if l == "a" and not p:
        print(l, end="")
        p = True
    elif p:
        print(l, end="")