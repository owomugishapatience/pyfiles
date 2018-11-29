
x=input("enter a string:")
def countvowels(x):
   count=0
   vowels="aeiou"
   for letter in x:
      if letter in vowels:
         count=count+1
   y=(print(count,letter))
   
countvowels(x)
