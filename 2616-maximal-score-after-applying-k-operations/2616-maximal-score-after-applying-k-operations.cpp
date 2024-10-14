class Solution {
public:
    long long maxKelements(vector<int>& nums, int k) {
        priority_queue<int>pq(nums.begin() , nums.end());

        long long ans = 0 ; 
        for(int i = 0 ; i<k ; i++){
            long long temp = pq.top();
            pq.pop();
            ans += temp ;
            temp = ceil((temp)/3.0);
            pq.push(temp);
        }
        return ans ;
    }
};

auto init = []()
{ 
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    return 'c';
}();