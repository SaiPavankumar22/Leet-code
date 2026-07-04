class Solution {
    public String addBinary(String a, String b) {
        int la = a.length()-1;
        int lb = b.length()-1;
        int sum =0;
        int carry =0;
        StringBuilder res = new StringBuilder();
        while(la>=0 || lb>=0 || carry ==1){
            sum = carry;
            if(la>=0){
                sum = (a.charAt(la)- '0') + sum;
                la--;
            }
            if(lb>=0){
                sum = (b.charAt(lb)- '0') + sum;
                lb--;
            }
            res.append(sum % 2);
            carry=sum/2;
            

        }
        return res.reverse().toString();
    }
}