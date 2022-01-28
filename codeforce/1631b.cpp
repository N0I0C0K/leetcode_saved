#include <queue>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
using ll = long long;
using uint = unsigned int;
const int inf = 0x3f3f3f3f;
const int maxn = 2e5 + 5;

int a[maxn];
int n, m;
int getAns()
{
    int pre = m - 2;
    int ans = 0;
    int l = 0;
    for (int i = 1;; i = i << 1)
    {
        for (int j = pre; j >= max(0, pre - i + 1); --j)
        {
            if (a[j] != a[m - 1])
            {
                ans++;
                break;
            }
        }
        if (pre - i + 1 < 0)
            break;
        pre = pre - i;
        for (int j = pre; j >= 0; j++)
        {
            if (a[j] != a[m - 1])
                break;
            l++;
        }
    }
    return ans;
}
int main()
{
    scanf("%d", &n);
    while (n--)
    {
        scanf("%d", &m);
        for (int i = 0; i < m; ++i)
        {
            scanf("%d", a + i);
        }
        int len = 1, ans = 0;
        while (len < m)
        {
            if (a[m - 1 - len] != a[m - 1])
            {
                len *= 2;
                ans++;
            }
            else
                ++len;
        }
        printf("%d\n", ans);
    }
    return 0;
}