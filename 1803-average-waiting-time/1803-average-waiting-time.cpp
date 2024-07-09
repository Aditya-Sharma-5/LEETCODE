class Solution {
public:
    double averageWaitingTime(vector<vector<int>>& customers) {
        double count = 0, curr = 0;
        for(auto& a : customers)
        {
            curr = max(curr, a[0] * 1.0) + a[1];
            count += curr - a[0];
        }
        return count / customers.size();
    }
};