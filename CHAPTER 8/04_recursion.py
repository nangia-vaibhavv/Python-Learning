# code to get factorial of numer using recursion.

# n=4
# product=1  # default value of factorial number
# for i in range(n):
#     product=product*(i+1) 
# print(product)     


# writing this inside my uncction
def factorial(n):
    product=1
    for i in range(n):
      product=product*(i+1) 
    return product 


f=factorial(5)
print(f)    
