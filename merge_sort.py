import json, time
#the merge sort algorithm divides the array into single arrays then merges the individual arrays one at a time while sorting at the same time

def merge_sort(list):
  '''
  sorts a list in ascending order
  returns a new sorted list
  
  Divide: first find the midpoint of the list and divide into sublists
  Conquer: recursively sort the sublists created in previous steps
  Combine: Merge the sorted sublists created in previous step

  runs in O(n log n) time
  split runs in O(log n) and merge in O(n)
  '''
  if len(list) <= 1: return list

  left, right = split(list)

  left_result = merge_sort(left)
  right_result = merge_sort(right)

  return merge(left_result, right_result)


def split(list):
  middleIndex = len(list) // 2
  left = list[:middleIndex]
  right = list[middleIndex:]
  return left, right

#region my own attemp to implement
def merge(list1, list2):
  #iterate through each index in the shorter list
  # print('list1 = {0}'.format(list1))
  # print('list2 = {0}'.format(list2))

  #figuring out which list is longer and then calling mergeInForLoop()
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
  insertionIndex = -1
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
      # if insertionIndex == -1: 
        # print('longer before = {0}'.format(longer))

        insertionIndex = getInsertionIndex(insertionIndex, longer, shorter[i])
        longer.insert(insertionIndex, shorter[i])
        # print('insertionIndex = {0}'.format(insertionIndex))
        # print('longer after = {0}'.format(longer))
        # print('')
      # else:
        #is the 1st item in 2nd array smaller than item at index 'i' but greater than item at index 'i-1' or greater than index 'i' and less than 'i + 1'?
        # pass

  return longer
 
  #if so,


def getInsertionIndex(startIndex, longer, valueToMerge):
  '''
  finds the index at which the item being merged is less than i + 1 but greater than or equal to i

  currentIndexlonger is the index in longer that we are currently at (we are assuming that longer and shorter are in ascending order)
  '''
  #dynamically start at either the front or the end depending on what the item to merge is and the first and last items are  
  # print('valueToMerge = {0}'.format(valueToMerge))

  middleIndex = len(longer) // 2
  middleValue  = longer[middleIndex]

  #return early easy cases
  if valueToMerge <= longer[0]: 
    # print('1')
    return 0
  if valueToMerge >= longer[-1]: 
    # print('2')
    
    return len(longer)
  if valueToMerge == middleValue: 
    # print('3')
    # print('middleIndex = {0}'.format(middleIndex))
    return middleIndex

  #change start index of loop depending on middle value
  loopStartIndex = 0
  loopEndIndex = len (longer)
  if valueToMerge < middleValue:
    loopEndIndex = middleIndex
  else:
    if startIndex == -1: loopStartIndex = middleIndex + 1
    else: loopStartIndex = startIndex

  #start from the left side and return the index, where longer[index] is smaller than valueToMerge and longer[index + 1] is greater
  for i in range(loopStartIndex, loopEndIndex):
    valueInLonger = longer[i]
    # print('valueInLonger = {0}'.format(valueInLonger))
    #here -1 is used as a flag to indicate there is no value
    nextValueInLonger = -1        
    if (i + 1) < len(longer): nextValueInLonger = longer[i + 1]

    #should never have to deal with valueToMerge < valueInLonger
   
    if valueToMerge > valueInLonger:
      if nextValueInLonger == -1:
        # print(4)
        return len(longer)
      else:
        if valueToMerge <= nextValueInLonger: 
          # print('nextValueInLonger = {0}'.format(nextValueInLonger))
          # print('i = {0}'.format(i))
          # print(5)
          return i + 1
        # else:
          # print("unaccounted for-----------------------------")
          # print('valueToMerge = {0}'.format(valueToMerge))
    else:
      # print(6)
      return i 

  
  #this should never actually be reached but just in case
  # print('Assumption 2 violated');
  return i
#endregion
          


def merge_sort_example(list):
  '''
  copied from video example
  '''
  if len(list) <= 1: return list

  left, right = split(list)

  left_result = merge_sort(left)
  right_result = merge_sort(right)

  return merge_video_example(left_result, right_result)

def merge_video_example(left, right) :
  l = []   
  i = 0
  j = 0
  
  #equally long lists 
  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      l.append(left[i])
      i += 1
    else:
      l.append(right[j])
      j += 1

  #right list longer
  while i < len(left):
    l.append(left[i])
    i += 1

  #left list longer
  while j < len(right):
    l.append(right[j])
    j += 1

  return l


def merge_sort_example2(list):
  if len(list) <= 1: return list

  #note: splitting
  middle_index = len(list) // 2
  left_values = merge_sort_example2(list[:middle_index])
  right_values = merge_sort_example2(list[middle_index:])
  # print('%15s %-15s' % (left_values, right_values))

  #note: merging
  sorted_values = []
  left_index = 0
  right_index = 0
  while left_index < len(left_values) and right_index < len(right_values):
    if left_values[left_index] < right_values[right_index]:
      sorted_values.append(left_values[left_index])
      left_index += 1
    else:
      sorted_values.append(right_values[right_index])
      right_index += 1

  sorted_values += left_values[left_index:]
  sorted_values += right_values[right_index:]
  return sorted_values

numbers = []
with open('numbers-1million.json') as f:
  numbers = json.load(f)

# start_own = time.time()
# sorted = merge_sort(numbers)
# print (f'Time elapsed own implementation: {time.time() - start_own}')

# start_example = time.time()
# sorted2 = merge_sort_example(numbers)
# print (f'Time elapsed example implementation: {time.time() - start_example}')

start_example2 = time.time()
sorted3 = merge_sort_example2(numbers)
# sorted3 = merge_sort_example2([1,2,5,4,3,1,2,9,8,7])
print (f'Time elapsed example2 implementation: {time.time() - start_example2}')