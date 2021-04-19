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
    current = current.nextNode

  return left, right

def merge(left, right):
  '''
  merges two linked lists sorting by data in the nodes
  returns a new merged list
  '''


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