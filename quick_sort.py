import json

def own_quick_sort(list):
  '''
  challenge: my own ascending quick sort implementation attempt after just learning about the quick sort algorithm 

  runs at O()
  '''
  if len(list) <= 1: return list
  pivot = list[0]
  less_than_or_equal_to_pivot = get_items(pivot, list, True)
  greater_than_pivot = get_items(pivot, list, False)
  # print('')
  # print(f"pivot = {pivot}")
  # print(f"less_than_or_equal_to_pivot = {less_than_or_equal_to_pivot}")
  # print(f"greater_than_pivot = {greater_than_pivot}")

  less_than_result = own_quick_sort(less_than_or_equal_to_pivot)
  greater_than_result = own_quick_sort(greater_than_pivot)

  return merge(less_than_result, pivot, greater_than_result)

def merge(less_than_result, pivot, greater_than_result):
  '''
  merges the arrays into one using a for loop if one of the arrays is empty
  runs at O(1) time
  '''
  # print('merge------------------')
  # print(f"pivot = {pivot}")
  # print(f"less_than_result = {less_than_result}")
  # print(f"greater_than_result = {greater_than_result}")
  # print('')
  less_than_result.append(pivot)
  if len(greater_than_result) > 0:
    for i in range(len(greater_than_result)):
      less_than_result.append(greater_than_result[i])
  
  return less_than_result

def get_items(pivot, list, get_less_than = True):
  '''
  this returns either the items in list[1:] that are less than or equal to pivot if get_less_than is true otherwise the items in list[1:] that are greater than pivot

  runs at O(1) time but adds O(n/2) space complexity due to items
  '''
  items = []

  for i in range(1, len(list)):
    item = list[i]
    if get_less_than:
      if item <= pivot: items.append(item)
    else:
      if item > pivot: items.append(item)
  
  return items



# numbers = test_merge_sort.getRandomList(20000)
# numbers = [1.2, 2.1, .2, .1, .55, 1, 2.3, 55, 43]
# print(own_quick_sort(numbers))

numbers = []
with open('numbers-1million.json', 'r') as f:
  numbers = json.load(f)

sorted = own_quick_sort(numbers)
print(f"len(numbers) = {len(numbers)}")
print(f"len(sorted) = {len(sorted)}")
# print(f"sorted = {sorted}")

