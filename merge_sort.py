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

def mergeInForLoop(longer, shorter):
  '''
  executes the logic necessary to merge the two lists
  '''

  currentIndexLarger = 0
  for i in range(len(shorter)):
    #there are two cases to handle:
    # both are len 1
    if (len(shorter) == 1 and (len(longer) == 1 or len(longer) == 0)) or (len(longer) == 1 and (len(shorter) == 1 or len(shorter) == 0)):
      if longer[0] > shorter[0]: return [shorter[0], longer[0]]
      if longer[0] <= shorter[0]: return [longer[0], shorter[0]]

    # if 1 is len 1 and the other is 
    # elif len(shorter) == 1 and len(longer) != 1 or len(shorter) != 1 and len(longer) == 1:
      # pass
    #otherwise
    else:
      #this only runs one time and finds the index where the first item in smaller is larger than 'bigger[index]' and smaller than 'bigger[index + 1]'
      if currentIndexLonger == 0: currentIndexLonger = getStartIndex(longer, shorter[i])
      #is the 1st item in 2nd array smaller than item at index 'i' but greater than item at index 'i-1' or greater than index 'i' and less than 'i + 1'?

      pass
 
  #if so,


def getStartIndex(longer, valueToMerge):
  '''
  finds the index at which the item being merged is less than i + 1 but greater than or equal to i

  currentIndexlonger is the index in longer that we are currently at (we are assuming that longer and shorter are in ascending order)
  '''
  #dynamically start at either the front or the end depending on what the item to merge is and the first and last items are

  middleIndex = len(longer) // 2
  middleValue  = longer[middleIndex]

  #return early easy cases
  if valueToMerge <= longer[0]: return 0
  if valueToMerge >= longer[-1]: return len(longer)
  if valueToMerge == middleIndex: return middleIndex

  #change start index of loop depending on middle value
  loopStartIndex = 0
  loopEndIndex = len (longer)
  if valueToMerge < middleValue:
    loopEndIndex = middleIndex
  else:
    loopStartIndex = middleIndex + 1

  #start from the left side and return the index, where longer[index] is smaller than valueTomerge and longer[index + 1] is greater
  for i in range(loopStartIndex, loopEndIndex):
    valueInLonger = longer[i]
    nextValueInLonger = -1
    if (i + 1) <= len(longer): nextValueInLonger = longer[i + 1]


    if valueToMerge > valueInLonger:
      if nextValueInLonger == -1:
        return len(longer)
      else:
        if valueToMerge <= nextValueInLonger:

          



#how are python list arguments passed? by ref or by val?
    
    
