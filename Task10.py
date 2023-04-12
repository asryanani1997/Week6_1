x= [3, 2, 1]
y= sorted(x)
z=sorted(x, reverse=True)

if len(x)<=2 or len(set(x))!=len(x):
    print("Neither")
elif x==y:
    print ("Increasing")
elif x==y:
    print("Decreasing")
else:
    print("Neither")

