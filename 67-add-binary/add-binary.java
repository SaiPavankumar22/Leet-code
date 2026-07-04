class Solution {
    public String addBinary(String a, String b) {
        int la = a.length()-1;
        int lb = b.length()-1;
        int sum =0;
        int carry =0;
        String res ="";
        while(la>=0 || lb>=0 || carry ==1){
            sum = 0;
            if(la>=0){
                sum = (a.charAt(la)- '0') + sum;
                la--;
            }
            if(lb>=0){
                sum = (b.charAt(lb)- '0') + sum;
                lb--;
            }
            if(carry==1){
                carry =0;
                sum = sum + 1;
            }
            if(sum==0){
                res = "0"+res;
            }
            else if(sum==1){
                res = "1"+res;
            }
            else if(sum==2){
                res = "0"+res;
                carry = 1;
            }
            else{
                res = "1" +res;
                carry = 1;
            }

        }
        return res;
    }
}