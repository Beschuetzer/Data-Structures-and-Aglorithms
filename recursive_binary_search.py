
def recursive_binary_search(list, target):
  #returns true or false if target exists in list

  #list must be sorted for this to work
  if len(list) == 0:
    return False

  middleIndex = len(list) // 2

  #get the value at middleIndex
  middleValue = list[middleIndex]

  #check if middleValue is target and return middleIndex if true
  print('middleValue = {0}'.format(middleValue))
  if list[len(list) // 2] == target:
    return True

  sub_list = list[middleIndex + 1:]
  if middleValue > target:
    sub_list = list[:middleIndex]

  return recursive_binary_search(sub_list , target)




