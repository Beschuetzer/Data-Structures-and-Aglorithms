"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
//My implementation of a LinkedList using TypeScript
const Stack_js_1 = require("./Stack.js");
class LinkedListNode {
    constructor(data) {
        this.nextNode = null;
        this.previousNode = null;
        this.data = data;
    }
}
class LinkedList {
    constructor(type) {
        this._TYPE_ERROR = 'Incorect Type!';
        this._size = 0;
        this.type = type;
        this.head = new LinkedListNode(null);
    }
    // public tail: LinkedListNode<T>;
    get size() {
        return this._size;
    }
    insert(data) {
        //Inserts at head O(1)
        if (typeof data !== this.type)
            return this._TYPE_ERROR;
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
    insertAtIndex(data, index) {
        if (typeof data !== this.type)
            return this._TYPE_ERROR;
        if (this.head.data == null)
            return this.head.data = data;
        if (index > this._size - 1)
            return this.tail;
        this._size++;
    }
    delete() {
        this._size--;
    }
    deleteAt() {
        this._size--;
    }
}
const ll = new LinkedList(Stack_js_1.InstanceTypes.number);
ll.insert(1);
ll.insert(2);
console.log('ll =', ll);
ll.insert(3);
ll.insert(4);
