
def recursive_sum(numbers):
  print('\nnew call to recursive sum------------------')
  print(f"numbers = {numbers}")
  if len(numbers) == 0: return 0
  
  recursion_result = recursive_sum(numbers[1:])
  sum = numbers[0] + recursion_result
  print(f"adding {numbers[0]} and {recursion_result}")
  print(f"sum = {sum}")

  return sum


print(recursive_sum([1,2,3,4,5,6,7,8,9]))