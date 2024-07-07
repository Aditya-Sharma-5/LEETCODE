class Solution {
public:
    int numWaterBottles(int numBottles, int numExchange) {
        // int empB = numBottles;
        int ans = numBottles;
        while(numBottles>= numExchange){
            int que = numBottles/ numExchange;
            int rem = (numBottles%numExchange);
            ans += que ; 
            numBottles = que + rem;
        }
        return ans;

    }
};