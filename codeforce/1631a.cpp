#include <queue>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
using ll = long long;
using uint = unsigned int;
const int inf = 0x3f3f3f3f;

int a[105], b[105];
int main()
{
    int n, m;
    scanf("%d", &n);
    while (n--)
    {
        scanf("%d", &m);
        for (int i = 0; i < m; ++i)
        {
            scanf("%d", a + i);
        }
        for (int i = 0; i < m; ++i)
        {
            scanf("%d", b + i);
        }
        for (int i = 0; i < m; ++i)
        {
            if (b[i] > a[i])
            {
                swap(a[i], b[i]);
            }
        }
        int maxa = 0, maxb = 0;
        for (int i = 0; i < m; ++i)
        {
            maxa = max(maxa, a[i]);
            maxb = max(maxb, b[i]);
        }
        printf("%d\n", maxa * maxb);
    }
    return 0;
}