/**
 * @param {number} n
 * @return {number}
 */
var arrangeCoins = function(n) {
    let left = 0, right = n;
    
    while (left <= right) {
        let mid = Math.floor((left + right) / 2);
        let sum = (mid * (mid + 1)) / 2;
        
        if (sum === n) return mid;
        if (sum < n) left = mid + 1;
        else right = mid - 1;
    }
    
    return right;
};