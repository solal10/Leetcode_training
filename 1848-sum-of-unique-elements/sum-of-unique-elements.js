/**
 * @param {number[]} nums
 * @return {number}
 */
var sumOfUnique = function(nums) {
    var dict = nums.reduce((dict, num) => {
        dict[num] = (dict[num] || 0) + 1;
        return dict;
    }, {});
    return Object.entries(dict)
        .filter(([key, value]) => value === 1) // Keep only entries where value is 1
        .reduce((sum, [key]) => sum + Number(key), 0);
};