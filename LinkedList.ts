//My implementation of a LinkedList using TypeScript
class LinkedListNode <T> {
  public data: T;
  public nextNode: any;
  public previousNode: any;

  constructor(data: T) {
    this.data = data;
  }
}
class LinkedList <T> {
  public type: InstanceTypes;
  public head: LinkedListNode<T>;
  // public tail: LinkedListNode<T>;

  constructor(type: InstanceTypes) {
    this.type = type;
    this.head = LinkedListNode();
  }

  public insert(){

  }

  public insertAt() {

  }

  public delete() {

  }

  public deleteAt() {

  }

}

