'''
@ASSESSME.USERID: mm2945
@ASSESSME.AUTHOR: author, list of authors
@ASSESSME.DESCRIPTION: Assignment 3.1
@ASSESSME.ANALYZE: YES
'''
import math

def fact(factorial):
    if factorial > 0:
        return math.factorial(factorial)
    else:
        return 0



def root(root):
    if root > 0:
        return math.sqrt(root)
    else:
        return 0


def trunk(trunc):
   if isinstance(trunc, (int, float)):
       return math.trunc(trunc)
   else:
       return 0
        

   





def main():
   number = int(input("Enter a numeric value:"))
   print(number, "factorial =", fact(number))

   number1 = float(input("Enter a numeric value:"))
   print("The square root of",number1, "= ", root(number1))
   
   number2 = float(input("Enter a numeric value:"))
   print(number2, "truncated =", trunk(number2))

if __name__ == "__main__":
    main()