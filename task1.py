'''
* ISAT 6250-1 Assignment: Python Basics & Tools
* 09/14/2024
* Shiron Thalagala (W0793591)
'''

# Function to calculate median of a given set of numbers
def findMedian(numArray):
    median = (numArray[1] + numArray[2]) / 2

    return(median)


# Function to find if the input number is prime or not
def checkPrime(num):
    if num == 2: 
        isPrime = True
    elif num > 1:
        for n in range(2, num):
            if num % n == 0:
                isPrime = False
                break                
            else:
                isPrime = True          
    else:
        isPrime = False
        
    return isPrime


# Get four numbers from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
num4 = int(input("Enter the fourth number: "))

numArray = [num1, num2, num3, num4]

# Compute the median and report it
median = findMedian(numArray)
print(f"\nThe median is {median}\n")


# Check for prime numbers using the checkPrime function
for number in numArray:
    if checkPrime(number):
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")
