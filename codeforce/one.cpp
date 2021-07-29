#include<cstdio>
#include<algorithm>
#include<cstring>

using namespace std;

char s[50];
char s_p[50];
int main()
{
    int n,x;
    scanf("%d",&n);
    for (size_t i = 0; i < n; i++)
    {
        scanf("%d",&x);
        scanf("%s",s);
        strcpy(s_p, s);
        sort(s, s+x);
        int nums = 0;
        for (size_t j = 0; j < x; j++)
        {
            if(s[j] != s_p[j])
                nums++;
        }
        printf("%d\n",nums);
    }
    
}