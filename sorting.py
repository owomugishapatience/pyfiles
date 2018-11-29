numbers=[1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,'j','b','h']
def list_sort(numbers):
   nums = {'evens': [], 'odds': [] ,'chars':[]}
   for m in numbers:
      if type(m) == str:
            nums['chars'].append(m)
      elif type(m)==int:
         if int(m) % 2==0:
          nums['evens'].append(m)
         else:
           nums['odds'].append(m)
   print (nums)
   return(nums)

list_sort(numbers)
