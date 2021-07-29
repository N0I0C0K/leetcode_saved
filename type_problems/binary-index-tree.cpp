#include<cstdio>
#include<cmath>
#include<cstring>
using namespace std;

const int MAX = 5e4+5;
int c[MAX];

int lowbit(int x){return x&(-x);}

void update(int x,int y,int n)
{
    for (int i = x; i <= n; i+=lowbit(i))
    {
        c[i]+=y;
    }

}

int query(int x)
{
    int ans = 0;
    for (int i = x; i > 0; i-=lowbit(i))
    {
        ans+=c[i];
    }
    return ans;
}

int main()
{
    int n;
    scanf("%d",&n);
    for(int cc = 1;cc<=n;++cc)
    {
        int m,z,x,y;
        char s[10];
        scanf("%d",&m);
        memset(c, 0, sizeof(c));
        for (size_t i = 1; i <= m; i++)
        {
            scanf("%d",&z);
            update(i,z,m);
        }
        printf("Case %d:\n",cc);
        while (true)
        {
            scanf("%s", s);
            if(s[0] == 'E')
                break;
            scanf("%d%d",&x,&y);
            if(s[0] == 'Q')
            {
                printf("%d\n",query(y)-query(x-1));
            }
            else if(s[0] == 'A')
            {
                update(x,y,m);
            }
            else
            {
                update(x,-y,m);
            }

        }

    }

    return 0;
}