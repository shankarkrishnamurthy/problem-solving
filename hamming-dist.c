#include<stdio.h>
unsigned int totalHammingDistance1(int* nums, int numsSize) {
    int sum = 0;
    int pair = 0;
    for (int i=0; i < numsSize; i++)
        for (int j=i+1; j < numsSize; j++)
            sum += __builtin_popcount(nums[i] ^ nums[j]);
    return sum;
}

unsigned int totalHammingDistance(int* nums, int numsSize) {
    int sum = 0;
    for (int i=0;i < 32; i++) {
        int bit=0;
        for (int j = 0; j < numsSize; j++)
             bit += !!((1U << i) & nums[j]);
        sum += (bit*(numsSize-bit));
    }
    return sum;
}

int main()
{
    int nums[] = { 4, 14 ,2 };
    int numsize = sizeof(nums)/sizeof(int);
    printf("sum = %u\n", totalHammingDistance(nums, numsize));
    printf("sum = %d\n", totalHammingDistance1(nums, numsize));
    return 0;
}
