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
    _insert(data, nodeToInsertAt, isInsertAtHead = true) {
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
            const tempPrevious = nodeToInsertAt.previousNode;
            nodeToInsertAt.previousNode = newHead;
            newHead.previousNode = tempPrevious;
            if (isInsertAtHead)
                this._head = newHead;
            else
                tempPrevious.nextNode = newHead;
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
        let count = 0;
        while (count !== index) {
            traverser = traverser.nextNode;
            count++;
        }
        this._insert(data, traverser, false);
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
    viewList(startFromHead = true) {
        const values = [];
        if (startFromHead) {
            let start = this._head;
            while (start) {
                values.push(start.data);
                start = start.nextNode;
            }
        }
        else {
            let start = this._tail;
            while (start) {
                values.push(start.data);
                start = start.previousNode;
            }
        }
        console.log(values.join('=>'));
    }
}
const ll = new LinkedList(Stack_js_1.InstanceTypes.number);
ll.insert(1);
ll.insert(2);
ll.insert(3);
ll.insert(4);
ll.insertAtIndex(31, 1);
ll.insertAtIndex(32, 1);
ll.insertAtIndex(33, 4);
// ll.insertAtIndex(40,3)
// ll.insertAtIndex(5,4)
// ll.insertAtIndex(6,4)
// ll.insert(2)
// ll.insert(3)
ll.viewList();
ll.viewList(false);
// console.log('ll.size =', ll.size);
// ll.insert(3)
// ll.insert(4)
