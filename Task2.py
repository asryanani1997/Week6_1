def damage(x, y, z):
    if x<0 or y<0:
        return "Invalid"
    if z=="second":
        return (x*y)
    elif z=="minute":
        return (x*y*60)
    elif z=="hour":
        return (x*y*3600)

print(damage(2, 100, "hour"))