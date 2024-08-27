import random

frequency = {}
frequency[2] = 0
frequency[3] = 0
frequency[4] = 0
frequency[5] = 0
frequency[6] = 0
frequency[7] = 0
frequency[8] = 0
frequency[9] = 0
frequency[10] = 0
frequency[11] = 0
frequency[12] = 0


for i in range(1, 1001):
  dice1 = random.randint(1, 6)
  dice2 = random.randint(1, 6)
  global result_sum
  result_sum = dice1 + dice2
  frequency[result_sum] += 1 
  print("First dice's value: " + str(dice1) + " + " + "Second dice's value: " + str(dice2) + "   The sum is: " + " = " +  str(result_sum))
  
  
# Print out the results
for sum_value in range(2, 13):
    print(f"Sum {sum_value}: {frequency[sum_value]}")

    
  
    
  
