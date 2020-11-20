import math

# A brute force approach based  
# implementation to find if a number 
# can be written as sum of two squares. 
  
# function to check if there exist two 
# numbers sum of whose squares is n. 
def sumSquare(n) : 
    i = 1 

    for i in range(n):
        for j in range(n):
            if i ** 2 + j ** 2 == n ** 2:
                print(f"{i}\t{j}\t{n}\t\t{i**2}\t{j**2}\t{n ** 2}")
                return
    return False
   
# driver Program 
n = 25
# print("x\ty\tn\t\tx^2\ty^2\tn^2")
# print("--------------------------------------------------------------")
# for i in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]:
#     sumSquare(i)
      

print(math.sqrt(65 ** 2 + 72 ** 2))