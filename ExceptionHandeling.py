try:
    a = int(input("Enter a number"))
    b = int(input("Enter a number"))
    c = a/b
    print("Result = ",c)
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print(e)
except:
    print("Some Exception")
else:
    print("No Exception")
finally:
    print("Finally")
print("Hello")
