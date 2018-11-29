x=int(input("enter the base"))
y=int(input("enter the powerraised"))
def power(x,y):
    if y==1:
        return x
    else:
        return x*power(x,y-1)
    
print(power(x,y))
