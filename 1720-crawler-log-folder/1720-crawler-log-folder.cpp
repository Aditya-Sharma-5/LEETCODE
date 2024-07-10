class Solution {
public:
    int minOperations(vector<string>& logs) {
        // vector<string> ans ; 
        // for(auto log : logs){
        //     if(log == "../"){
        //         if(!ans.empty()){
        //             ans.pop_back();
        //         }
        //     }
        //     else if( log != "./"){
        //         ans.push_back(log);
        //     }
        // }
        // return ans.size();

        int n = 0;
        for (int i = 0; i < logs.size(); i++) {
            if (logs[i] == "../") {
               if(n>0) n--;
            } else if (logs[i] == "./") {
                continue;
            } else {
                n++;
            }
        }
        if(n<0) return 0;
        return n;
    }
};