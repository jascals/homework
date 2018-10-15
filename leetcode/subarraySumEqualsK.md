Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.


```
class Solution {
    public int subarraySum(int[] nums, int k) {
        int count = 0;
        for (int start = 0; start < nums.length; start++) {
            int sum=0;
            for (int end = start; end < nums.length; end++) {
                sum+=nums[end];
                if (sum == k)
                    // consider every subarray possible.
                    count++;
            }
        }
        return count;
    }
}
```
