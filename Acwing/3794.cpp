#include<cstdio>
using namespace std;
using ll = long long;
using uint = unsigned int;
const int inf = 0x3f3f3f3f;


char temp[2010];
char res[2010];
int idx[2010];
int main()
{
    int n,base;
    scanf("%d",&n);
    base = n%2==0?1:-1;
    scanf("%s",temp);
    if (n<=2)
    {
        printf("%s",temp);
        return 0;
    }
    idx[0] = (n-1)/2;
    res[idx[0]] = temp[0];
    idx[1] = idx[0]+base;
    res[idx[1]] = temp[1];
    for (int i = 2; i < n; ++i)
    {
        if(i&1)
            idx[i] = idx[i-2]+base;
        else
            idx[i] = idx[i-2]-base;
        res[idx[i]] = temp[i];
    }
    for (int i = 0; i < n; ++i)
    {
        putchar(res[i]);
    }
    
    return 0;
}