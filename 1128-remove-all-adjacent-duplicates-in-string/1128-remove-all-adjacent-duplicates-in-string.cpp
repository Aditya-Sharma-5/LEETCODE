class Solution {
public:
    string removeDuplicates(string s) {
        
        //      FIRST APPROACH
        // bool flag = true;
        // while(flag)
        // {
        //     flag =false;
        //     if(s.length()==0){
        //         return s;
        //     }
        //     for(int i = 0 ; i<s.length()-1 ; i++){
        //         if(s[i] == s[i+1]){
        //             s.erase(i , 2);
        //             flag = true;
        //             break;
        //         }
        //     }

        // }

        // return s;


        // Second Approach 

        string ans = "";

        int index = 0;

        while(index<s.length()){
            if(ans.length() >0 && ans[ans.length()-1] == s[index]){
                ans.pop_back();
            }
            else{
                //push
                ans.push_back(s[index]);
            }
            index++;
        }
        return ans;
    }
};