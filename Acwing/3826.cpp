#include<cstdio>
#include<cstring>
using namespace std;
using ll = long long;
using uint = unsigned int;
const int inf = 0x3f3f3f3f;

int kmp[100];
char s[10000010];

void fkmp(int n)
{
    memset(kmp, 0, sizeof kmp);
    for (int i = 1; i < n; ++i)
    {
        int j = kmp[i-1];
        while (j>0&&s[j] != s[i])
        {
            j = kmp[j-1];
        }
        if(s[i] == s[j]) ++j;
        kmp[i] = j;
    }
    
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
        int t = kmp[n-1],res = 0;
        bool ok = false;
        for (int i = 1; i<n-1 ; ++i)
        {
            if(kmp[i] <= t && kmp[i] > res)
            {
                ok = true;
                res = kmp[i];
            }
        }
        if(ok)
        {
            for (int i = 0; i < res; ++i)
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