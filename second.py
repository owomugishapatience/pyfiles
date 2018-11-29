
x= int (input("enter year birth:"))
y =int(input("enter current year:"))
z=y-x
print (z)
if z<=18:
    print (" the person is a minor")
elif z>18 and z<40:

    print ("the person is youth")
else:
      print ("the person is adult")
