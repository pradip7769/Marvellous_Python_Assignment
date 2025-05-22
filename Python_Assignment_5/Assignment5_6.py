#Q6. Celsius to Fahrenheit Converter
# Accept temperature in Celsius and convert it to Fahrenheit using the formula:
# F = (c * 9/5) + 32
# Expected Input : Enter temperature in Celsius : 25
# Expected Output : Temperature in Fahrenheit : 77.0°F
CtoF = lambda C : (C * 9/5) + 32

# def CtoF(C):
#     F = (C * 9/5) + 32
#     return F

def main():
    print("Enter Temperature in Celsius : ")
    temp = int(input())
    ret = CtoF(temp)
    print("Temperature in Faherenheit: ",ret,"°F")

if __name__ == "__main__":
    main()