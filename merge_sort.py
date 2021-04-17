#the merge sort algorithm divides the array into single arrays then merges the individual arrays one at a time while sorting at the same time

def merge_sort(list):
  '''
  sorts a list in ascending order
  returns a new sorted list
  
  Divide: first find the midpoint of the list and divide into sublists
  Conquer: recursively sort the sublists created in previous steps
  Combine: Merge the sorted sublists created in previous step
  '''
  if len(list) <= 1: return list

  middleIndex = len(list) // 2
  left = list[:middleIndex]
  right = list[middleIndex:]

  left_result = merge_sort(left)
  right_result = merge_sort(right)

  return merge(left_result, right_result)




def merge(list1, list2):
  #iterate through each index in the shorter list
  listOneIsLonger = True
  if len(list2) > len(list1): listOneIsLonger = False

  if listOneIsLonger is True: 
    return mergeInForLoop(list1, list2)
  else:
    return mergeInForLoop(list2, list1)

def mergeInForLoop(larger, smaller):
  '''
  executes the logic necessary to merge the two lists
  '''
  for i in range(len(larger)):
    pass
    #is the 1st item in 2nd array smaller than item at index 'i' but greater than item at index 'i-1' or greater than index 'i' and less than 'i + 1'?
  #if so,



    
    
