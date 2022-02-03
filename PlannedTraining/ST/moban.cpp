// https://www.luogu.com.cn/problem/P3865
#include <queue>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
using ll = long long;
using uint = unsigned int;
const int inf = 0x3f3f3f3f;

const int maxn = 100005;

int a[maxn] = {};
int lg[maxn] = {-1};     //预处理log_2_(x)
int mmax[maxn][50] = {}; //表示mmax[i][j]表示 a[i][i+2^j-1]区间内的最大值

int main()
{
    int n, m;
    scanf("%d%d", &n, &m);
    for (int i = 1; i <= n; ++i)
    {
        scanf("%d", a + i);
        lg[i] = lg[i >> 1] + 1;
        mmax[i][0] = a[i];
    }
    for (int i = 1; i <= lg[n]; ++i)
    {
        for (int j = 1; j + (1 << i) - 1 <= n; ++j)
        {
            mmax[j][i] = max(mmax[j][i - 1], mmax[j + (1 << (i - 1))][i - 1]);
        }
    }
    int l, r;
    while (m--)
    {
        scanf("%d%d", &l, &r);
        int len = lg[r - l + 1];
        printf("%d\n", max(mmax[l][len], mmax[r - (1 << len) + 1][len]));
    }
    return 0;
}