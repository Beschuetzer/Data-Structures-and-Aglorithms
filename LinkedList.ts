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
  public type: InstanceTypes;
  public head: LinkedListNode <T>;
  private _size: number = 0;

  // public tail: LinkedListNode<T>;

  get size() {
    return this._size;
  }

  constructor(type: InstanceTypes) {
    this.type = type;
    this.head = new LinkedListNode(null);
  }

  public insert(data: T){
    //Inserts at head O(1)
    if (typeof data !== this.type) return this._TYPE_ERROR;
    if (this.head.data == null) {
      return this.head.data = data;
    }

    const previousHead = this.head;
    const newHead = new LinkedListNode(data);
    newHead.nextNode = previousHead;
    previousHead.previousNode = newHead;
    this.head = newHead;
    console.log('previousHead =', previousHead);
    console.log('newHead =', newHead);
    this._size++;
  }

  public insertAtIndex(data: T, index: number) {
    if (typeof data !== this.type) return this._TYPE_ERROR;
    if (this.head.data == null) return this.head.data = data;
    if (index > this._size - 1) return this.tail

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
console.log('ll =', ll);
ll.insert(3)
ll.insert(4)