

def chkPrime(value):
   print(value)
   sum = 0
   for i in value:
      # print("value i : ",i)
      count = 0
      for x in range(1,i):
         # print("value x : ",x)
         if i % x == 0:
               count +=1
      if count < 2:
            sum += i
            # print("prime : ",i)
   # print("Sum : ", sum)
   return sum

  

