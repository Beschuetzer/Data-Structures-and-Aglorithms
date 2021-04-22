//My implementation of a LinkedList using TypeScript
import { InstanceTypes } from './Stack.js'
class LinkedListNode <T> {
  public data: T;
  public nextNode: any = null;
  public previousNode: any = null;

  constructor(data: T) {
    this.data = data;
  }
}
class LinkedList <T> {
  private _TYPE_ERROR: string = 'Incorect Type!';
  private _type: InstanceTypes;
  private _head: LinkedListNode <T>;
  private _tail: LinkedListNode <T>;
  private _size: number = 0;

  // public tail: LinkedListNode<T>;
  
  get size() {
    return this._size;
  }
  get type() {
    return this._type;
  }
  get head() {
    return this._head;
  }
  get tail() {
    return this._tail;
  }

  constructor(type: InstanceTypes) {
    this._type = type;
    this._head = new LinkedListNode(null) as any;
    this._tail = new LinkedListNode(null) as any;
  }

  private _insert(data: T, nodeToInsertAt: LinkedListNode <T>) {
    //Inserts at head O(1)
    if (typeof data !== this._type) return this._TYPE_ERROR;
    const newHead = new LinkedListNode(data);

    if (nodeToInsertAt === this._tail) {
      newHead.previousNode = nodeToInsertAt;
      nodeToInsertAt.previousNode = newHead;
      this._tail = newHead;
    }
    else {
      newHead.nextNode = nodeToInsertAt;
      nodeToInsertAt.previousNode = newHead;
      this._head = newHead;
    }

    if (this._size === 1) {
      this._tail.previousNode = newHead;
    }

    this._size++;
  }

  public insert(data: T){
    if (this._head.data == null) {
      this._size++;
      this._tail.data = data;
      return this._head.data = data;
    }
    
    this._insert(data, this._head);
  }

  public insertAtIndex(data: T, index: number) {
    //inserts at index if it exists otherwise, inserts after tail
    
    if (this._head.data == null) {
      this._size++; 
      this._tail.data = data;
      return this._head.data = data;
    }

    if (index > this._size - 1) {
      return this._insert(data, this._tail);
    }

    //TODO: Finish regular case logic:
    // this._insert(data, current)
  }

  public searchFromStart(data: T) {
    if (typeof data !== this._type) return this._TYPE_ERROR;
    
    let traverser = this._head;
    let count = 0
    while (traverser.data) {
      if (data === traverser.data) return count;
      count++;
      traverser = traverser.nextNode;
    }
    return -1;
  }

  public searchFromEnd(data: T) {
    if (typeof data !== this._type) return this._TYPE_ERROR;
    
    let traverser = this._tail;
    let count = 0
    while (traverser.data) {
      if (data === traverser.data) return this._size - count;
      count++;
      traverser = traverser.previousNode;
    }
    return -1;
  }

  public delete() {
    this._size--;
  }

  public deleteAt() {
    this._size--;
  }

}

const ll = new LinkedList(InstanceTypes.number);
ll.insert(1)
ll.insert(2)
ll.insertAtIndex(3,4)
// ll.insert(2)
// ll.insert(3)
console.log(ll)

// console.log('ll.size =', ll.size);

// ll.insert(3)
// ll.insert(4)