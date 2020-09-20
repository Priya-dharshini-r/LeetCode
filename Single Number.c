
int singleNumber(int* nums, int numsSize){
if(numsSize == 0)
        return 0;
    
    int i, result = nums[0];

    for(i = 1; i < numsSize; i++) {
        result = (result ^ nums[i]);
    }

    return result;
}
