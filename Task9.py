x=("")
if x.islower() and all(i.isalpha() or i.isspace() for i in x):
    print(True)
else:
    print(False)


