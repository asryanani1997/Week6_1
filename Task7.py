x="1"
y=git2

if isinstance(x, int) and isinstance(y, int):
    z=str(x)+str(y)
elif isinstance (x, str) and isinstance (y, str):
    z=(int(x)+int(y))
else:
    z= None
      
print(z)
