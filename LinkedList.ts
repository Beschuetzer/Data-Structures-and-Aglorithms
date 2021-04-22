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

  public insert(data: T){
    //Inserts at head O(1)
    if (typeof data !== this._type) return this._TYPE_ERROR;
    if (this._head.data == null) {
      this._size++;
      this._tail.data = data;
      return this._head.data = data;
    }
    
    //NOTE: THis code may be buggy
    const previousHead = this._head;
    const newHead = new LinkedListNode(data);
    newHead.nextNode = previousHead;
    previousHead.previousNode = newHead;
    this._head = newHead;

    if (this._size === 1) {
      this._tail.previousNode = newHead;
    }

    this._size++;
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

  public insertAtIndex(data: T, index: number) {
    if (typeof data !== this._type) return this._TYPE_ERROR;
    if (this._head.data == null) {
      this._size++; 
      return this._head.data = data;
    }
    if (index > this._size - 1) return this._tail

    this._size++;

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
ll.insert(3)
console.log(ll)

// console.log('ll.size =', ll.size);

// ll.insert(3)
// ll.insert(4)