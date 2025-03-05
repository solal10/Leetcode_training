/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    var dict = new Map(); // Using a Map for better key handling

    return function(...args) {
        const key = JSON.stringify(args); // Convert args to a string key

        if (dict.has(key)) {
            return dict.get(key); // Return cached result
        } else {
            const result = fn(...args); // Compute result
            dict.set(key, result); // Store in cache
            return result;
        }
    };
}

/** Example Usage */
let callCount = 0;
const memoizedFn = memoize(function (a, b) {
    callCount += 1;
    return a + b;
});

console.log(memoizedFn(2, 3)); // 5 (computed)
console.log(memoizedFn(2, 3)); // 5 (cached)
console.log(callCount); // 1 (function was only called once)
