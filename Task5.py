x= ["a", 12, True]
result =[]
for i in x: 
    if isinstance(i, int) and i%2==0:
        result.append(i+1)
    elif isinstance(i, str):
        result.append(i.capitalize()+"i")
    elif isinstance(i, bool):
        result.append(not i)
    else:
        result.append(i)

print(result)