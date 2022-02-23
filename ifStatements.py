def equality(a, b, c):
    a, b, c = int(a), int(b), int(c)
    if a == b or a == c or b == c:
        return True
    else:
        return False

print(str(equality(5, "5", 3)))