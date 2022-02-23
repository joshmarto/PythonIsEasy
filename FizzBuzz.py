for i in range(1, 101):
    c = 0
    for x in range(1, i+1):
        if c>2:
            break
        if i%x == 0:
            c += 1
    if c == 2:
        print("Prime", end=" ")
    if i%3 == 0 and i%5 == 0:
        print("Fizz Buzz")
        continue
    elif i%3 == 0:
        print("Fizz")
        continue
    elif i%5 == 0:
        print("Buzz")
        continue
    else:
        print(i)

