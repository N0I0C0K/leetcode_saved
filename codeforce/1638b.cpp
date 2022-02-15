#include <queue>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
using ll = long long;
using uint = unsigned int;
const int inf = 0x3f3f3f3f;

int main()
{
    int t, n, a, maxodd, maxenn;
    scanf("%d", &t);
    while (t--)
    {
        scanf("%d", &n);
        maxodd = 0, maxenn = 0;
        bool can = true;
        while (n--)
        {
            scanf("%d", &a);
            if (!can)
                continue;
            if ((a & 1))
            {
                if (a < maxodd)
                {
                    can = false;
                }
                maxodd = max(maxodd, a);
            }
            else
            {
                if (a < maxenn)
                {
                    can = false;
                }
                maxenn = max(maxenn, a);
            }
        }
        if (can)
            printf("Yes\n");
        else
            printf("No\n");
    }
    return 0;
}