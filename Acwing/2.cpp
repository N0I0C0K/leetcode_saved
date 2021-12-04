#include <cstdio>
#include <algorithm>
using namespace std;
using ll = long long;
using uint = unsigned int;
const int inf = 0x3f3f3f3f;

int f[1001];
int w[1001], v[1001];

int main()
{
    int N, V;
    scanf("%d%d", &N, &V);
    for (uint i = 0; i < N; ++i)
    {
        scanf("%d%d", &v[i], &w[i]);
    }
    for (uint i = 0; i < N; ++i)
    {
        for (uint j = V; j >= v[i]; --j)
        {
            f[j] = max(f[j], f[j - v[i]] + w[i]);
        }
    }
    printf("%d", f[V]);
    return 0;
}