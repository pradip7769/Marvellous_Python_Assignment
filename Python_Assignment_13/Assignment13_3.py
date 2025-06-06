
# Q3 Write a program which contains one class named as Numbers. 
# Arithmetic class contains one instance variables as Value. 
# Inside init  method initialise that instance variables to the value which is accepted from user. 
# Ther are four instance methods inside class as ChkPrime(), chkPerfect(), sumFactors(), Factors(). 
# chkPrime() method will returns true if number is prime otherwise return false. 
# ChkPerfect() method will returns true if number is perfect otherwise return false. 
# Factors() method will display all factors of instance variable. 
# SumFactors() method will return addition of all factors. Use this method in any another method as helper method if required. 
# After dedigning the above class call all instance methods by creating multiple objects. 


class Numbers:
    def __init__(self,value):
        self.value = value

    def chkPrime(self):
        count = 0
        for i in range(1,self.value):
            if self.value % i == 0:
                count +=1
        if count < 2:
            return True
        else:
            return False

    def chkPerfect(self):
        return self.sumFactors() == self.value

    def sumFactors(self):
        sum = 0
        for i in range(1,self.value):
            if self.value % i == 0:
                sum += i
        return sum
            
    def Factors(self):
        print("Factors : ")
        for i in range(1,self.value):
            if self.value % i == 0:
                print(i,end=" ")


def main():
    num1 = Numbers(28)

    ret = num1.chkPrime()
    if ret: 
        print(num1.value, "is Prime")
    else:
        print(num1.value, "is not prime")

    ret = num1.chkPerfect()
    if ret: 
        print(num1.value, "is Perfect")
    else:
        print(num1.value, "is not Perfect")
    
    sum = num1.sumFactors()
    print("Sum of Factor is : ", sum)

    num1.Factors()
    
    print("\n")
    print("-" * 30)

    num2 = Numbers(5)

    ret = num2.chkPrime()
    if ret: 
        print(num2.value, "is Prime")
    else:
        print(num2.value, "is not prime")

    ret = num2.chkPerfect()
    if ret: 
        print(num2.value, "is Perfect")
    else:
        print(num2.value, "is not Perfect")
    
    sum = num2.sumFactors()
    print("Sum of Factor is : ", sum)

    num2.Factors()

if __name__ == "__main__":
    main()