//https://www.luogu.com.cn/problem/P2880

#include <queue>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
using ll = long long;
using uint = unsigned int;
const int inf = 0x3f3f3f3f;
const int maxn = 50005;

int a[maxn] = {};
int lg[maxn] = {-1};
int mmax[maxn][50] = {};
int mmin[maxn][50] = {};

int main()
{
    int n, m;
    scanf("%d%d", &n, &m);
    for (int i = 1; i <= n; ++i)
    {
        scanf("%d", a + i);
        lg[i] = lg[i >> 1] + 1;
        mmax[i][0] = a[i];
        mmin[i][0] = a[i];
    }
    for (int i = 1; i <= lg[n]; ++i)
    {
        for (int j = 1; j + (1 << i) - 1 <= n; ++j)
        {
            mmax[j][i] = max(mmax[j][i - 1], mmax[j + (1 << (i - 1))][i - 1]);
            mmin[j][i] = min(mmin[j][i - 1], mmin[j + (1 << (i - 1))][i - 1]);
        }
    }
    int l, r;
    while (m--)
    {
        scanf("%d%d", &l, &r);
        int len = lg[r - l + 1];
        printf("%d\n", max(mmax[l][len], mmax[r - (1 << len) + 1][len]) - min(mmin[l][len], mmin[r - (1 << len) + 1][len]));
    }
    return 0;
}