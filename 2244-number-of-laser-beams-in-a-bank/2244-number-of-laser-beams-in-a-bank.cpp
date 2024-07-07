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
        vector<int> device;
        for(auto row : bank){
            device.push_back(countB(row));

        }

        for(int i = 0; i<device.size();i++){
            int j = i+1;
            while(j<device.size()){
                ans += device[i]* device[j];
                if(device[j] == 0){
                    j++;
                }
                else{
                    break;
                }
            }
        }
        return ans ;
    }
};