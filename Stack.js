"use strict";
// A stack is a one-ended linear data structure which models a real-world stack, by having two primary operations (push and pop);  Also known as a FILO (first-in-last-out) or LIFO (last-in-first-out) structure
var StackItemTypes;
(function (StackItemTypes) {
    StackItemTypes["number"] = "number";
    StackItemTypes["object"] = "object";
    StackItemTypes["string"] = "string";
})(StackItemTypes || (StackItemTypes = {}));
;
//A dynamic-array-based Stack implementation:
class Stack {
    constructor(type) {
        this.type = type;
        this.data = [];
        this.INCORRECT_TYPE_MSG = 'Invalid item type!';
        this.NO_ITEMS_IN_STACK_MSG = 'This Stack is empty!';
        this._size = 0;
        this._isEmpty = true;
    }
    get size() {
        return this._size;
    }
    get isEmpty() {
        return this._size === 0;
    }
    setIsEmpty() {
        if (this.data.length === 0)
            this._isEmpty = true;
        else
            this._isEmpty = false;
    }
    push(item) {
        if (typeof item !== this.type)
            return this.INCORRECT_TYPE_MSG;
        this.setIsEmpty();
        this._size++;
        return this.data.push(item);
    }
    pop() {
        if (this.data.length < 1)
            return this.NO_ITEMS_IN_STACK_MSG;
        this.setIsEmpty();
        this._size--;
        return this.data.pop();
    }
}
const stack = new Stack(StackItemTypes.number);
console.log(stack.push(1));
console.log(stack.push(2));
console.log(stack.push(3));
console.log(stack.push(4));
console.log(stack.pop());
console.log('stack.size =', stack.size);
console.log('stack.isEmpty =', stack.isEmpty);
