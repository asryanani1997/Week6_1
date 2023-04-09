x= (["A", 0, "Edabit", 1729, "Python", "1729"])
z=[]
for i in x:
    if isinstance(i, int):
        z.append(i)

print(z)