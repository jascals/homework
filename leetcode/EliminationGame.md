class Solution {
    public int lastRemaining(int n) {
        return help(n, true);
    }
    
    private int help(int n, boolean flag){
        if(n==1) return 1;
        if(flag){
            return 2*help(n/2, false);
        }else{
            return 2*help(n/2, true)-1+n%2;
        }
    } 
}
