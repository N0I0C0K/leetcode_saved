//https://www.luogu.com.cn/problem/P2731

#include <stack>
#include <queue>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
using ll = long long;
using uint = unsigned int;
const int inf = 0x3f3f3f3f;

const int maxn = 502;

int map[maxn][maxn] = {0};
int du[maxn] = {0};
int n, m;

stack<int> res;

void Euler(int u)
{
    for (int v = 1; v <= n; ++v)
    {
        if (map[u][v])
        {
            map[u][v]--;
            map[v][u]--;
            Euler(v);
        }
    }
    res.push(u);
}

int main()
{
    scanf("%d", &m);
    int u, v;
    for (int i = 0; i < m; ++i)
    {
        scanf("%d%d", &u, &v);
        n = max(n, u);
        n = max(n, v);
        map[u][v]++;
        map[v][u]++;
        du[u]++;
        du[v]++;
    }
    int s = 1;
    for (int i = 1; i <= n; ++i)
    {
        if (du[i] % 2)
        {
            s = i;
            break;
        }
    }
    Euler(s);
    while (!res.empty())
    {
        printf("%d\n", res.top());
        res.pop();
    }
    return 0;
}