# n = int(input("Enter a number to check if it is a perfect number: "))

def sum_of_proper_div(n):
  # A perfect number must be greater than 1
  if n <= 1:
    print("Please enter number greater than 1.")
  
  #Find the sum of proper divisors
  divisors = 0
  for i in range(1, n):
    if n % i == 0:
      divisors += i

  if divisors == n:
    return divisors

#Function for finding the perfect number in given range
def find_perfect_numbers(start, end):
  #Empty list, which will store all the perfect numbers in given range.
  perfect_numbers = []

  #This loop will be iterating through the given start and end values.
  for num in range(start, end + 1):
    if sum_of_proper_div(num):# Validating the value through the function which checks the number is the perfect number or not.
      perfect_numbers.append(num)#Appending the value in the list
      
  return perfect_numbers

#Input range
start = int(input("Enter the starting number of the range: "))
end = int(input("Enter the ending number of the range: "))

#Find and display the perfect number in the range
perfect_numbers = find_perfect_numbers(start, end)

if perfect_numbers:
  print(f"The numbers between {start}  and {end}: {perfect_numbers}.")

else:
  print(f"No perfect numbers found between {start} and {end}.")
