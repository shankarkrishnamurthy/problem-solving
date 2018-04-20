/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
    var rev=[];
    var prod = 1;
    for (var i=0;i < nums.length; i++) {
        prod *= nums[nums.length-i-1];
        rev[nums.length-i-1] = prod;
    }
    rev[nums.length] = 1;
    prod = 1;
    var res = [];
    for (var i=0;i < nums.length; i++) {
        res[i] = rev[i+1] * prod;
        prod *= nums[i];
    }
    return res;
};

console.log(productExceptSelf([]));
console.log(productExceptSelf([4]));
console.log(productExceptSelf([4,3]));
console.log(productExceptSelf([1,2,3,4]));
