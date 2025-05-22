#Q3. Voting Eligibility Checker
# Accept age from the user and check whether the person is eligible to vote. 
#(Age should be 18 or above)
#Expeced Input : 19   Expected Output : Eligible to vote.
a = "You are elligible for voting..."
b = "you are not elligible for voting..."

checkVote = lambda Age : a if Age >= 18 else b

# def checkVote(Age):
#     if Age >= 18:
#         print("You are elligible for voting...")
#     else:
#         print("you are not elligible for voting...") 

def main():
    print("Enter the age : ", end="")
    age = int(input())
    ret = checkVote(age)
    print(ret)

if __name__ == "__main__":
    main()