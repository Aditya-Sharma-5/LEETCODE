class Solution {
public:
    string decodeMessage(string key, string message) {
        char start = 'a';
        char map[280] = {0};

        //Create Mapping 

        for(auto ch : key){
            if(ch !=' ' && map[ch] == 0){
                map[ch] = start++;
            }
        }

        string ans = "";
        //use map 
        for(auto ch : message){
            if(ch == ' '){
                ans.push_back(' ');
            }
            else{
                char curr = map[ch];
                ans.push_back(curr);
            }
        }
        return ans;
    }
};