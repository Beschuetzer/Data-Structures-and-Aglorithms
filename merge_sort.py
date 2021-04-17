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

  return 

    
    
