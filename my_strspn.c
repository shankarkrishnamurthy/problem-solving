#include <string.h>
#include<stdio.h>
size_t my_strspn(const char *s, const char *t)
{
    int i, sz = 0;
    char strmap[256]={[0 ... 255] = 0};
    if (!s || !t) 
        return 0;
    for (i=0;i<strlen(t);i++) {
        if (strmap[t[i]])
            continue;
        strmap[t[i]] = 1;
    }
    for (i=0;i<strlen(s);i++) {
        if (strmap[s[i]])
            sz += 1;
        else
            break;
    }
    return sz;
}
int main()
{
   int len;
   //const char str1[] = "ABCDEFG019874";
   //const char str2[] = "ABBDC";
  const char str1[] = "129th";
  const char str2[] = "1234567890";
  //const char str1[] = "129th";
  //const char str2[] = "";
  //const char str1[] = "";
  //const char str2[] = "abc";

   len = my_strspn(str1, str2);
   printf("Length of initial segment matching %d real %d\n", len, strspn(str1,str2) );
   
   return (0);
}
/*
#include <string.h>
#include<stdio.h>
int main()
{
   int len;
   const char str1[] = "ABCDEFG019874";
   const char str2[] = "ABBDE";

   len = strspn(str1, str2);

   printf("Length of initial segment matching %d\n", len );
   
   return(0);

}
*/
