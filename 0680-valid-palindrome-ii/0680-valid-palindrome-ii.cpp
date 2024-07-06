class Solution {
public:

    bool checkpallindrome(string s , int i , int j)
    {
        while(i<=j)
        {
            if(s[i] !=s[j])
            {
                return false;
            }
            else{
                i++;
                j--;
            }
        }
        return  true;
    }

    bool validPalindrome(string s) 
    {
        int i = 0 ;
        int j = s.length()-1;

        while(i<j)
        {
            if(s[i] == s[j])
            {
                i++ ;
                j-- ;
            }
            else
            {
                bool ans1 = checkpallindrome(s , i+1 , j);
                bool ans2 = checkpallindrome(s , i, j-1);
                return ans1 || ans2;
            }
        }
        return true;
    }
};