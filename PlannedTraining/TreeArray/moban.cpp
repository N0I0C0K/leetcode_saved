#include <queue>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
using ll = long long;
using uint = unsigned int;
const int inf = 0x3f3f3f3f;

const int maxn = 5e5 + 5;
int n, m;
int a[maxn] = {0}, c[maxn] = {0};
inline int lowbit(int x) { return x & (-x); }

//i位置加上k
void update(int i, int k)
{
    while (i <= n)
    {
        c[i] += k;
        i += lowbit(i);
    }
}

//[1,i]区间的和
int query(int i)
{
    int res = 0;
    while (i > 0)
    {
        res += c[i];
        i -= lowbit(i);
    }
    return res;
}

int main()
{
    scanf("%d%d", &n, &m);
    for (int i = 1; i <= n; ++i)
    {
        scanf("%d", a + i);
        update(i, a[i]);
    }
    int t, x, y;
    while (m--)
    {
        scanf("%d%d%d", &t, &x, &y);
        if (t == 1)
        {
            update(x, y);
        }
        else
        {
            printf("%d\n", query(y) - query(x - 1));
        }
    }
    return 0;
}