class Node:
  '''
  an object for storing a single node of a linked list.
  Models two attributes - data and the link to the next node in the list
  '''
  data = None
  next_node = None

  def __init__(self, data):
    self.data = data

  # def __str__(self):
  #     return '\
  #     <Node data: {0}\n\
  #     \tnext_node: {1}>\n\
  #     '.format(str(self.data), self.next_node)

  def __repr__(self):
    return "<Node data: %s>" % self.data

  def getNext(self):
    return self.next_node

class LinkedList:
  '''
  singly-linked list
  '''
  def __init__(self):
    self.head = None

  def is_empty(self):
    return self.head == None

  def size(self):
    '''
    returns number of nodes in list;getting the size/length is an O(n) operation for linked-lists
    '''
    count = 0
    current = self.head
    while current:
      print(current.data)
      count += 1
      current = current.next_node

    return count 

  def add(self, data):
    '''
    prepends data to the head of the list O(1)
    '''
    current_head = self.head
    self.head = Node(data)
    self.head.next_node = current_head

  def search(self, data):
    '''
    traverses list in search of data
    returns node containing data if found otherwise None
    takes O(n) time
    '''
    current = self.head
    while current:
      if current.data == data: return current
      current = current.next_node

    return None

  def insert(self, data, position):
    '''
    inserts data at position
    position starts at 0 (0 == head)
    inserting take O(1) time but finding the correct position takes O(n) time
    '''
    new_node = Node(data)
    count = 0
    current = self.head
    previous = None


    print('position = {0}'.format(position))
    while current:
      print('count = {0}'.format(count))
      print('current = {0}'.format(current))
      if position == 0:
          #when inserting a new head
          self.add(data)
          return count
      elif count == position:        
        previous.next_node = new_node 
        previous.next_node.next_node = current
        return count
      elif current.next_node == None:
        print(current)
        print(previous)
        current.next_node = new_node
        return count
      

      count += 1
      previous = current
      current = current.next_node

    return -1

  def remove(self, data):
    '''
    Removes the node from the list that contains data
    '''
    current = self.head
    previous = None

    while current:
      if current.data == data:
        if current is self.head:
          self.head = current.next_node
        else:
          previous.next_node = current.next_node

        del current
        return

      previous = current
      current = current.next_node

  def remove_at_index(self, index): 
    '''
    removes the node at index
    '''
    current = self.head
    previous = None
    count = 0
    while current:
      print('current = {0}'.format(current))
      if count == index:
        if current is self.head:
          self.head = current.next_node
        else:
          previous.next_node = current.next_node

        del current
        return

      previous = current
      current = current.next_node
      count += 1

  def get_node_at_index(self, index):
    '''
    returns the node at index
    '''
    current = self.head
    i = 0

    while current:
      if index == i: return current
      i+=1
      current = current.next_node

  def __repr__(self):
    '''
    returns a string representation of the list 
    take 0(n) time
    '''

    nodes = []
    current = self.head
    
    while current:
      if current is self.head:
        nodes.append("[Head: %s]" % current.data)
      elif current.next_node is None:
        nodes.append("[Tail: %s]" % current.data) 
      else:
        nodes.append("[%s]" % current.data)

      current = current.next_node
    return "->".join(nodes)

  def __eq__(self, other):
    if isinstance(other, LinkedList):
      if self.__repr__() == other.__repr__(): return True
    return False

linked_list = LinkedList()

# linked_list.add(20)
# linked_list.add(22)
# linked_list.add(30)
linked_list.add(31)
linked_list.add(32)
linked_list.add(33)
linked_list.insert(34,-1)
linked_list.remove(34)
linked_list.remove_at_index(0)
print(linked_list)
print(linked_list.get_node_at_index(1))

