```
class Solution {
    public int[] countBits(int num) {
        int[] res = new int[num+1];
        for(int i=0;i<=num;++i){
            res[i] = count(i);
        }
        return res;
    }
    
    int count(int m){
        if(m==0) return 0;
        else return m%2==1?(1+count(m-1)):count(m/2);
    }
}
```
