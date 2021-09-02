#include<cstdio>
#include<cstring>
using namespace std;
using ll = long long;
using uint = unsigned int;
const int inf = 0x3f3f3f3f;

ll kmp[1000010];
char s[1000010];

void fkmp(int n)
{
    memset(kmp, 0, sizeof kmp);
    for (int i = 1; i < n; ++i)
    {
        ll j = kmp[i-1];
        while (j>0&&s[j] != s[i])
        {
            j = kmp[j-1];
        }
        if(s[i] == s[j]) ++j;
        kmp[i] = j;
    }
}


/**************关键*****************************/
ll find(int n)
{
    ll t = kmp[n-1],res = 0;
    //逐个枚举“最长”前缀
    while (t>0)
    {
        for (int i = 0; i < n-1; ++i)
        {
            if(kmp[i] == t)
            {
                return t;
            }
        }
        //如果当前长度不满足，t就应该等于他本身的前缀长度比如：aabbaa..(若干)..aabbaa 如果t=6不满足，那么t就应该等于aabbaa的前后缀长度即t = 2
        t = kmp[t-1];
    }
    return 0;
}

int main()
{
    int t;
    scanf("%d",&t);
    while (t--)
    {
        scanf("%s",s);
        int n = strlen(s);
        fkmp(n);
        ll res = find(n);
        if(res)
        {
            for (ll i = 0; i < res; ++i)
            {
                putchar(s[i]);
            }
            putchar('\n');
        }
        else
            printf("not exist\n");
        
    }
    return 0;
}