/**
 * @param {number[]} nums
 * @param {number} k
 * @param {number} multiplier
 * @return {number[]}
 */
var getFinalState = function(nums, k, multiplier) {
    nums.indexOf(Math.min(...nums));
    for(var i =0;i<k;i++){
        nums[nums.indexOf(Math.min(...nums))]=nums[nums.indexOf(Math.min(...nums))]*multiplier
    }
    return nums

};