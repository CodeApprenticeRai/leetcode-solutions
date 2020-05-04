/*
    Given a binary array find the maximum number of consecutive 1s in this array.


*/

#include <algorithm>

class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int i=0;
        int max_count=0;
        int count=0;

        while(i < nums.size()){
            if (nums[i]){
                count++;
            } else {
                count=0;
            }
            i++;

            if ( count > max_count ){
                max_count = count;
            }
        }

        return max_count;
    }
};