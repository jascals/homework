```
public class Solution {
    int sumCount=Integer.MAX_VALUE;
    public int numSquares(int n) {
        List<Integer> squareList = new ArrayList<>();
        for(int i=1;i*i<=n;i++) squareList.add(0,i*i);
        dfs(squareList,0,n);
        return sumCount;
    }
    private void dfs(List<Integer> squreList, int currCount, int sum){
        if(sum==0){
            sumCount=Math.min(sumCount,currCount);
            return;
        }
        for(int i=0;i<squreList.size();i++){
            if(currCount+1>=sumCount) break;
            if(sum-squreList.get(i)<0) continue;
            dfs(squreList,currCount+1,sum-squreList.get(i));
        }
    }
}
```
