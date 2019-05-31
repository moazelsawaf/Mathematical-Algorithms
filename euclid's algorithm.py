'''
In mathematics, the Euclidean algorithm,or Euclid's algorithm, is an efficient method for computing the greatest common divisor (GCD) of two numbers,
the largest number that divides both of them without leaving a remainder.
It is named after the ancient Greek mathematician Euclid.

To learn more about Euclid's algorithm and how it works visit this link on wikipedia : https://en.wikipedia.org/wiki/Euclidean_algorithm

The code written by : Moaz El-sawaf .

Thanks...
'''

# Here is the function of calculating the GCD...

def gcd(firstNum,secondNum):
    if secondNum == 0:
        return firstNum
    else:
        return gcd(secondNum,firstNum % secondNum)

# This stuff just to give you an example of how to use it or in case if you want to test...

firstNum = int(input("Enter the first number : "))
secondNum = int(input("Enter the second number : "))

print("\nGCD({},{}) = {}".format(firstNum,secondNum,gcd(firstNum,secondNum)))

