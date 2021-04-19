import linked_list as linked_list_class

def merge_sort(linked_list):
  '''
  sorts a linked list in ascending order
  -recursively divide the linked list into sublists containing a single node
  -repeatedly merge the sublists to produce sorted sublists until one remains

  returns a sorted linked list
  '''
  linked_list_size = linked_list.size()
  if linked_list_size <= 1 or linked_list.head is None: return linked_list

  left, right = split(linked_list, linked_list_size)
  # left, right = split_video_example(linked_list, linked_list_size)

  left_result = merge_sort(left)
  right_result = merge_sort(right)

  return merge(left_result, right_result)


def split(linked_list, linked_list_size):
  '''
  divide the unsorted list at midpoint into sub linked-lists
  '''
  middleIndex = linked_list_size // 2
  print('middleIndex = {0}'.format(middleIndex))
  
  left = linked_list_class.LinkedList()
  right = linked_list_class.LinkedList()

  position = 0
  current = linked_list.head
  while current:
    if position < middleIndex: left.add(current)
    elif position >= middleIndex: right.add(current)
    position+=1
    current = current.next_node

  return left, right

def merge(left, right):
  '''
  merges two linked lists sorting by data in the nodes
  returns a new merged list
  '''
  print('left = {0}'.format(left))
  print('right = {0}'.format(right))

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
      left_data = left_current.data.data.data.data
      right_data = right_current.data.data.data.data
      print('left_data = {0}'.format(left_data))
      print('right_data = {0}'.format(right_data))

      if left_data > right_data:
        merged_current.next_node = left_current
        left_current = left_current.next_node
      else:
        merged_current.next_node = right_current
        right_current = right_current.next_node

    current = current.next_node

  merged.remove_at_index(0)
  return merged


def split_video_example(linked_list, linked_list_size):
  if linked_list is None or linked_list.head is None:
    left = linked_list
    right = None

    return left, right
  else: 
    mid = linked_list_size // 2
    mid_node = linked_list.get_node_at_index(mid - 1)

    left = linked_list
    right = linked_list_class.LinkedList()
    right.head = mid_node.next_node
    mid_node.next_node = None

    return left, right


ll = linked_list_class.LinkedList()
ll.add(10)
print(ll)