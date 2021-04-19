import linked_list as linked_list_class
import time

def merge_sort(linked_list):
  '''
  sorts a linked list in ascending order
  -recursively divide the linked list into sublists containing a single node
  -repeatedly merge the sublists to produce sorted sublists until one remains

  returns a sorted linked list

  runs in O(kn log n)
  '''
  linked_list_size = linked_list.size()
  if linked_list_size <= 1 or linked_list.head is None: return linked_list

  startTime = time.time()
  left, right = split(linked_list, linked_list_size)
  print(f'Time for mine: {time.time() - startTime}')
  startTime = time.time()
  left, right = split_video_example(linked_list, linked_list_size)
  print(f'Time for example: {time.time() - startTime}')

  left_result = merge_sort(left)
  right_result = merge_sort(right)

  return merge(left_result, right_result)


def split(linked_list, linked_list_size):
  '''
  divide the unsorted list at midpoint into sub linked-lists

  run in O(k log n) where k is n/2
  '''
  middleIndex = linked_list_size // 2
  
  left = linked_list_class.LinkedList()
  right = linked_list_class.LinkedList()

  position = 0
  current = linked_list.head
  while current:
    if position < middleIndex: left.add(current.data)
    else: right.add(current.data)
    position+=1
    current = current.next_node

  return left, right

def merge(left, right):
  '''
  merges two linked lists sorting by data in the nodes
  returns a new merged list

  run in O(n) time
  '''

  #create a new linked list that contains nodes from 
  #merging left and right
  merged = linked_list_class.LinkedList()

  #add a fake head that is discarded later
  merged.add(0)

  #set current to the head of the linked list
  merged_current = merged.head

  #obtain head nodes for left and right linked lists
  left_current = left.head
  right_current = right.head

  #iterate over left and right until reaching tail node of one of them
  while left_current or right_current:
    #if head node of left is none, we're past the tail
    #add the node from right to merged linked list
    if left_current is None: 
      merged_current.next_node = right_current

      #call next on right to set loop condition to false
      right_current = right_current.next_node

    elif right_current is None:
      merged_current.next_node = left_current
      left_current = left_current.next_node

    else: 
      #not at either node
      #obtain node data to perform comparison operations
      left_data = left_current.data
      right_data = right_current.data

      if left_data > right_data:
        merged_current.next_node = right_current
        right_current = right_current.next_node
      else:
        merged_current.next_node = left_current
        left_current = left_current.next_node

    merged_current = merged_current.next_node

  merged.remove_at_index(0)
  return merged


def split_video_example(linked_list, linked_list_size):
  '''
  splits the linked list into two linked lists that will differ by a maximum of one element

  returns two linked lists

  runs in O(k log n)
  '''
  if linked_list is None or linked_list.head is None:
    left = linked_list
    right = None

    return left, right
  else: 
    mid = linked_list_size // 2
    #note: this line is the bottleneck here and adds the k factor:
    mid_node = linked_list.get_node_at_index(mid - 1)

    left = linked_list
    right = linked_list_class.LinkedList()
    right.head = mid_node.next_node
    mid_node.next_node = None

    return left, right


ll = linked_list_class.LinkedList()
ll.add(10)
print(ll)