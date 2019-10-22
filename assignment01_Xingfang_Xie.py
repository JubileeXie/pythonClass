# Xingfang Xie
# 15/10/2019
# Assignmment 01
import math
# exercise 1 function 1
    def square(x):
        """ Function to calculate square of a list of numbers

        Parameters
        ----------
        x

        Returns
        -------
        squared numbers
        """
        return x*x

x=[3,6,9,12,15]
sqrlist=map(square, x)
print(list(sqrlist))

# exercise 2 function 2
    def squareroot(y):
        """ Function to calculate square root of single number,
        if this number is not negative, print error can not calculate
        if this number > = 0, print result

        Parameters
        ----------
        y

        Returns
        -------
        error or
        square root of the y
        """
        if y < 0:
            print("Oops, negative numbers your function cannot calculate the square root")
        else:
            return math.sqrt(y)

print (squareroot(-5))
print (squareroot(9))

