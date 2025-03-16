/**
 * @param {number[]} nums
 */
var ArrayWrapper = function(nums) {
    this.nums = nums; // Store the array
};

/**
 * @return {number}
 */
ArrayWrapper.prototype.valueOf = function() {
    return this.nums.reduce((sum, num) => sum + num, 0); // Sum all elements
};

/**
 * @return {string}
 */
ArrayWrapper.prototype.toString = function() {
    return JSON.stringify(this.nums); // Convert array to string format
};

/**
 * Example Usage:
 */
const obj1 = new ArrayWrapper([1, 2]);
const obj2 = new ArrayWrapper([3, 4]);

console.log(obj1 + obj2); // 10  (1+2+3+4)
console.log(String(obj1)); // "[1,2]"
console.log(String(obj2)); // "[3,4]"
