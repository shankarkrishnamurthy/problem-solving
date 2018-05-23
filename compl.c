#include  <stdio.h>
int findComplement(int num) {
    unsigned int j, i, mask;
    for (i=31;i>=0;i--)
        if (num  & (1<<i)) break;
    num = ~num;
    for (j=31;j>i;j--)
        num = num & (~(1<<j));
    return (num);
}

int main()
{
    printf("%d\n",findComplement(5));
    printf("%d\n",findComplement(1));
}
