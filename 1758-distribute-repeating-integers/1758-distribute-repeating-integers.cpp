class Solution {
public:

    bool helper(vector<int>&counts , vector<int>&quantity , int ithCustomer){
        // Base Case
        if(ithCustomer == quantity.size()){
            return true;
        }

        for(int i = 0 ; i<counts.size() ; i++)
        {
            if(counts[i]>=quantity[ithCustomer])
            {
                counts[i] -=quantity[ithCustomer];
                if(helper(counts , quantity , ithCustomer+1)){
                    return true;
                }

                // BackTrace
                counts[i] +=quantity[ithCustomer];
            }
        }
        return false;
    }

    bool canDistribute(vector<int>& nums, vector<int>& quantity) {

        // Creating frequency map
        unordered_map<int, int> map;
        for(int n : nums){
            map[n]++;
        }
        // Storing the frequency 
        vector<int>counts;
        for(auto it:map){
            counts.push_back(it.second);
        }

        // Sort in descending order to reduce the time complexity
        sort(quantity.rbegin() , quantity.rend());
        return helper(counts , quantity , 0);
    }
};