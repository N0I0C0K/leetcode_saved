#include<cstdio>
using namespace std;

int main()
{
    int t,n,x;
    long long ma,mi;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d",&n);
        ma = 0;
        mi = 1e9;
        while(n--)
        {
            scanf("%d",&x);
            if(x>ma)
                ma = x;
            if(x<mi)
                mi =x;
        }
        printf("%d\n",(ma&mi));
    }
    return 0;
}