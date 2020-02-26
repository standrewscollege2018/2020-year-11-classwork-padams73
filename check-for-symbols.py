chars = set('0123456789$,!@#%^&*()')

names = []

keep_asking = True

while keep_asking == True:
        name = input("Enter your name: ")
        
        if any((c in chars) for c in name):
                print("Enter a valid name")
        elif name.lower() == "end":
                keep_asking = False
        else:
                names.append(name)

print(names)
