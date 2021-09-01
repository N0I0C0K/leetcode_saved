#include<cstdio>
#include<map>
#include<unordered_map>
#include<string>
using namespace std;
using ll = long long;
using uint = unsigned int;
const int inf = 0x3f3f3f3f;

char ss[100010];

int main()
{
    int t,l;
    char temp;
    scanf("%d",&t);
    while (t--)
    {
        unordered_map<ll,ll> keys;
        ll h = 0;
        ll res = 0;
        keys[0] = 1;
        scanf("%d",&l);
        scanf("%s",ss);
        for (int i = 0; i < l; ++i)
        {
            temp = ss[i];
            if(temp == 'U')
                h+=100000;
            else if(temp == 'D')
                h-=100000;
            else if(temp == 'L')
                --h;
            else if(temp == 'R')
                ++h;
            if(keys.find(h)!=keys.end())
            {
                res+=keys[h];
            }
            keys[h]++;
        }
        printf("%lld\n",res);
    }
    return 0;
}