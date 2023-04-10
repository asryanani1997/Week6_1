x= [1, 1, 2]

if all(x[i]<x[i+1] for i in range(len(x)-1)):
    print("increasing")
elif all(x[i]>x[i+1] for i in range(len(x)-1)):
    print("decreasing")
else:
    print("neither")
