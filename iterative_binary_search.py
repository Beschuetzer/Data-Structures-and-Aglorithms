#Time complexity: O(log n)
#Space Complexity: O(1)
#preferred approach in non-tail call optimizing languages like Python and JS


import math


def binary_search(list, target):
  #list must be sorted for this to work
  #returns index of target in list otherwise None

  print('list = {0}'.format(list))
  firstIndex = 0
  lastIndex = len(list) - 1

  while lastIndex >= firstIndex:
    currentArray = list[firstIndex: lastIndex + 1]
    print('currentArray = {0}'.format(currentArray))
    #get the middle index
    middleIndex = (firstIndex + lastIndex) // 2

    #get the value at middleIndex
    middleValue = list[middleIndex]

    #check if middleValue is target and return middleIndex if true
    print('middleValue = {0}'.format(middleValue))
    if middleValue == target:
      return middleIndex

    #adjust indexes
    if target > middleValue:
      firstIndex = middleIndex + 1
    else:
      lastIndex = middleIndex - 1

    print('firstIndex = {0}'.format(firstIndex))
    print('lastIndex = {0}'.format(lastIndex))

  #returning None if target not present in list
  return None
