#include<cstdio>
using namespace std;
using ll = long long;
using uint = unsigned int;
const int inf = 0x3f3f3f3f;
const int maxn = 2e5+10;
char s[maxn];
int main()
{
    int t,n,mi;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d",&n);
        scanf("%s",s);
        mi = n-1;
        for (int i = 0; i < n-1; i++)
        {
            if(s[i] > s[i+1])
            {
                mi = i;
                break;
            }
        }
        for (int i = 0; i < n; i++)
        {
            if(i != mi)
                putchar(s[i]);
        }
        putchar('\n');
    }
    return 0;
}