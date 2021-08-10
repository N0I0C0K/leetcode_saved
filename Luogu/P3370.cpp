#include<cstdio>
#include<algorithm>
#include<cstring>
using namespace std;
using ull = unsigned long long;
const int maxn = 1e5+5;
char st[1505];
ull allHash[maxn];
ull base = 131;

ull ghash(char *s)
{
    ull ans = 0;
    size_t n = strlen(s);
    for (size_t i = 0; i < n; ++i)
    {
        ans = ans*base+(ull)s[i];
    }
    return ans;
}

int main()
{
    int n,ans=0;
    scanf("%d",&n);
    for (size_t i = 0; i < n; ++i)
    {
        scanf("%s",st);
        allHash[i] = ghash(st);
        //printf("%llu\n", allHash[i]);
    }
    sort(allHash,allHash+n);
    for (size_t i = 1; i < n; ++i)
    {
        if(allHash[i] == allHash[i-1])
            ans++;
    }
    printf("%d",n-ans);
    return 0;
}