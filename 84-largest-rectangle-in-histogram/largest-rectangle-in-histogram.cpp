class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        stack<int>st;
        int n = heights.size();
        vector<int>left_small(n);
        vector<int>right_small(n);

        for(int i=0;i<n;i++){
            while(!st.empty() && heights[st.top()]>=heights[i]){
                st.pop();
            }
            if(st.empty()){
                left_small[i] = 0;
            }
            else{
                left_small[i] =st.top() + 1;
            }
            st.push(i);
        }

        while(!st.empty()){
            st.pop();
        }
        for(int j=n-1;j>=0;j--){
            while(!st.empty() && heights[st.top()]>=heights[j]){
                st.pop();
            }
            if(st.empty()){
                right_small[j] = n-1;
            }
            else{
                right_small[j] = st.top()-1;
            }
            st.push(j);
        }
        int max_area =0;
        for(int k = 0;k<n;k++){
            int wi = right_small[k] - left_small[k] +1;
            max_area = max(max_area, heights[k]*wi);
        }
        return max_area;
    }
};