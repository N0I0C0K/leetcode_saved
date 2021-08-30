#include<cstdio>
#include<map>
using namespace std;
using ll = long long;
using uint = unsigned int;
const int inf = 0x3f3f3f3f;

char ss[100010];
int main()
{
    int t,l;
    char temp;
    map<ll,bool> keys;
    scanf("%d",&t);
    while (t--)
    {
        keys.clear();
        ll x = 0,y = 0,res = 0;
        keys[0] = true;
        scanf("%d",&l);
        scanf("%s",ss);
        for (int i = 0; i < l; ++i)
        {
            temp = ss[i];
            if(temp == 'U')
                ++y;
            else if(temp == 'D')
                --y;
            else if(temp == 'L')
                --x;
            else if(temp == 'R')
                ++x;
            ll h = x+y*1000000;
            if(keys.find(h) != keys.end())
                res++;
            else
                keys[h] = true;
        }
        printf("%lld\n",res);
    }
    return 0;
}