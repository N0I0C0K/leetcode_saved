#include <queue>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
using ll = long long;
using uint = unsigned int;
const int inf = 0x3f3f3f3f;

int dp[20020] = {0};
int main()
{
    int n, t;
    scanf("%d%d", &n, &t);
    memset(dp, inf, sizeof dp);
    dp[0] = 0;
    int a, b;
    for (int i = 0; i < t; ++i)
    {
        scanf("%d%d", &a, &b);
        for (int i = a; i <= 20000; ++i)
        {
            if (b > 0)
            {
                dp[i] = min(dp[i], dp[i - a] + 1);
                --b;
            }
        }
    }
    printf("%d", dp[n]);
    return 0;
}