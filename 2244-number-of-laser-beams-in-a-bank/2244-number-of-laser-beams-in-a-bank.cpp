class Solution {
public:
    int countB(string b){
        int c = 0;
        for(auto i:b){
            c+= i -'0';
        }
        return c;
    }
    int numberOfBeams(vector<string>& bank) {
        int ans = 0;
        int prev_count = 0;
        for (int i = 0; i < bank.size(); i++) {
            int current_count = countB(bank[i]);
            if (current_count > 0) {
                ans += prev_count * current_count;
                prev_count = current_count;
            }
        }
        return ans;

    }
};