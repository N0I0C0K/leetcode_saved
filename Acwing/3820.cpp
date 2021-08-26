#include<cstdio>
using namespace std;
using ll = long long;
using uint = unsigned int;
const int inf = 0x3f3f3f3f;

int main()
{
    int a,b,k,m,t;
    scanf("%d%d%d%d",&a,&b,&k,&m);
    int ai,bi;
    for (int i = 0; i < a; ++i)
    {
        scanf("%d",&t);
        if(i == k-1)
            ai = t;
    }
    for (int i = 0; i < b; ++i)
    {
        scanf("%d",&t);
        if(i == b-m)
            bi = t;
    }
    if(ai<bi)
        printf("YES");
    else
        printf("NO");
    return 0;
}