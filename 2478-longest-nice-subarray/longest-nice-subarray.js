/**
 * @param {number[]} nums
 * @return {number}
 */
var longestNiceSubarray = function(nums) {
    let maxCount = 0;
    let left = 0;
    let bitMask = 0;

    for (let right = 0; right < nums.length; right++) {
        while ((bitMask & nums[right]) !== 0) { 
            bitMask ^= nums[left]; 
            left++;
        }

        bitMask |= nums[right]; 
        maxCount = Math.max(maxCount, right - left + 1);
    }

    return maxCount;
};