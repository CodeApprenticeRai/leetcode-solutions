/*
    Given an array of size n, find the majority element

*/

#include <math.h>
#include <map>

class Solution {
public:
    int majorityElement(vector<int>& nums) {
        std::map<int,int> number_count;
        int majority_element; 

        for ( auto &number : nums ){
            if (number_count.count(number) != 1){
                number_count[ number ] = 1;
            } else {
                number_count[ number ] ++;
            }
            if ( number_count[ number ] > floor( nums.size()/ 2 )){
                majority_element=number;
                return number;
            }
        }
        return majority_element;
    }
};