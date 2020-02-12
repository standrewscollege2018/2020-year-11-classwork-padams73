age = int(input("Age"))
if age > 13:
    student = input("Student? (y/n)")
    if student == "y":
        print("$8")
    elif age >= 18:
        print("$12")
    else:
        print("$9")
elif age >= 5:
    print("$7")
else:
    print("free")

