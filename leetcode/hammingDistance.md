```
class Solution {
    public int hammingDistance(int x, int y) {
        if(x==0&&y==0) return 0;
        if(x%2!=y%2){
            return 1+hammingDistance(x/2, y/2);
        }else{
            return hammingDistance(x/2, y/2);
        }
    }
}
```
