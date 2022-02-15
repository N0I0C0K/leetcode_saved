#include <queue>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
using ll = long long;
using uint = unsigned int;
const int inf = 0x3f3f3f3f;

int a[505];

int main()
{
    int t, n, l, tar, r;
    scanf("%d", &t);
    while (t--)
    {
        scanf("%d", &n);
        tar = -1;
        l = 0, r = 0;
        for (int i = 1; i <= n; ++i)
        {
            scanf("%d", a + i);
            if (a[i] != i && l == 0)
            {
                l = i;
            }
            if (l != 0 && a[i] == l)
            {
                r = i;
            }
        }
        reverse(a + l, a + r + 1);
        for (int i = 1; i <= n; ++i)
        {
            printf("%d ", a[i]);
        }
        printf("\n");
    }

    return 0;
}