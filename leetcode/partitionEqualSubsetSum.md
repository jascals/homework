```
class Solution {
    public boolean canPartition(int[] nums) {
        int sum = 0;
        for(int i:nums)
            sum += i;
        if(sum%2==1)
            return false;
        Arrays.sort(nums);
        return backtrack(nums,0,0,nums.length-1,sum);
    }
    boolean backtrack(int [] nums, int sum1, int sum2, int pos, int sum)
    {
        if(sum1>sum/2 || sum2>sum/2)
            return false;
        if(pos == -1)
            return sum1==sum2;
        return backtrack(nums, sum1+nums[pos],sum2,pos-1,sum) || backtrack(nums, sum1,sum2+nums[pos],pos-1,sum);
    }
}
```
