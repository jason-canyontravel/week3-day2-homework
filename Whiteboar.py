# Write a function that when given an integer as an argument, returns "Even" if the number is even, and "Odd" if the number is odd.
def evens(n):
    if n % 2 == 0:
       return "even"
    else: 
       return "odd" 
   
print(evens(3))
    