class Solution {
public:
    int minOperations(vector<string>& logs) {
        vector<string> ans ; 
        for(auto log : logs){
            if(log == "../"){
                if(!ans.empty()){
                    ans.pop_back();
                }
            }
            else if( log != "./"){
                ans.push_back(log);
            }
        }
        return ans.size();
    }
};