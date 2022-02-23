#ERROR HANDLING
float("123.4") #-> 123.4
#float("N/A") #-> error

keyWord = input("Enter something ")
try:
    raise ValueError
    raise NameError
except ValueError:
    print("Got a value error")
    pass
except Exception as e:
    print(str(e))
    pass
finally:
    print("Finally")
print("Passed exception")