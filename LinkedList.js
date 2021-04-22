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
        this._type = type;
        this._head = new LinkedListNode(null);
        this._tail = new LinkedListNode(null);
    }
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
    _insert(data, nodeToInsertAt) {
        //Inserts at head O(1)
        if (typeof data !== this._type)
            return this._TYPE_ERROR;
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
    insert(data) {
        if (this._head.data == null) {
            this._size++;
            this._tail.data = data;
            return this._head.data = data;
        }
        this._insert(data, this._head);
    }
    insertAtIndex(data, index) {
        //inserts at index if it exists otherwise, inserts after tail
        if (this._head.data == null) {
            this._size++;
            this._tail.data = data;
            return this._head.data = data;
        }
        if (index > this._size - 1) {
            return this._insert(data, this._tail);
        }
        let traverser = this._head;
        while (traverser) {
            //TODO: Finish regular case logic:
            //need to traverse to correct node by checking nextNode  and seeing if it match the data, if it does do the swap
        }
        // this._insert(data, traverser)
    }
    searchFromStart(data) {
        if (typeof data !== this._type)
            return this._TYPE_ERROR;
        let traverser = this._head;
        let count = 0;
        while (traverser) {
            if (data === traverser.data)
                return count;
            count++;
            traverser = traverser.nextNode;
        }
        return -1;
    }
    searchFromEnd(data) {
        if (typeof data !== this._type)
            return this._TYPE_ERROR;
        let traverser = this._tail;
        let count = 0;
        while (traverser.data) {
            if (data === traverser.data)
                return this._size - count;
            count++;
            traverser = traverser.previousNode;
        }
        return -1;
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
ll.insertAtIndex(3, 4);
// ll.insert(2)
// ll.insert(3)
console.log(ll);
// console.log('ll.size =', ll.size);
// ll.insert(3)
// ll.insert(4)
