class Solution {
public:
    int minAddToMakeValid(string s) {
        stack<char>st ; 
        int ans = 0 ;
        for(auto ch :s){
            if(ch =='('){
                st.push(ch);
                ++ans;
            }
            else{
                if(!st.empty()){
                    --ans;
                    st.pop();
                }
                else{
                    ++ans;
                }
            }
        }
        return ans ; 
    }
};