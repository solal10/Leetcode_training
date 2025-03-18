/**
 * @param {number[]} arr
 * @return {number}
 */
var trimMean = function(arr) {
    if (arr.length < 20) return []; // Handle small arrays where 5% trimming removes too much

    arr.sort((a, b) => a - b); // Step 1: Sort the array in ascending order

    let removeCount = Math.floor(arr.length * 0.05); // Step 2: Find the 5% cutoff

    var temp = arr.slice(removeCount, arr.length - removeCount);
    return temp.reduce((sum, num) => sum + num, 0)/temp.length
};