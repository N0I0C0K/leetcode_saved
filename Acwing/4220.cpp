#include <queue>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
using ll = long long;
using uint = unsigned int;
const int inf = 0x3f3f3f3f;

const int maxn = 200005;
int prefixY[maxn];
int prefixX[maxn];
char str[maxn];
int n = 0;
int a, b;
int tx = 0, ty = 0;
bool solve(int l)
{
    for (int i = 0; i <= n - l; ++i)
    {
        int x1 = 0, y1 = 0;
        x1 += (prefixX[i] + prefixX[n] - prefixX[i + l]);
        y1 += (prefixY[i] + prefixY[n] - prefixY[i + l]);
        int dis = abs(a - x1) + abs(b - y1);
        if (dis > l)
            continue;
        if ((l - dis) % 2 != 0)
            continue;
        return true;
    }
    return false;
}

int main()
{
    scanf("%d", &n);
    scanf("%s", str);
    scanf("%d%d", &a, &b);
    for (int i = 0; i < n; ++i)
    {
        prefixX[i] = tx;
        prefixY[i] = ty;
        if (str[i] == 'R')
            ++tx;
        else if (str[i] == 'L')
            --tx;
        else if (str[i] == 'U')
            ++ty;
        else if (str[i] == 'D')
            --ty;
    }
    prefixX[n] = tx;
    prefixY[n] = ty;
    int left = 0, right = n, mid;
    while (left < right)
    {
        mid = (left + right) >> 1;
        if (solve(mid))
            right = mid;
        else
            left = mid + 1;
    }
    if (solve(right))
        printf("%d", right);
    else
        printf("-1");
    return 0;
}