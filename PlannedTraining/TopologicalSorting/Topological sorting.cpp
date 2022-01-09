// 请不要被标签迷惑

#include <cstdio>
#include <algorithm>
#include <queue>
using namespace std;
using ll = long long;
using uint = unsigned int;
const int inf = 0x3f3f3f3f;

const int maxn = 100001;

int in[maxn] = {0};
vector<int> edge[maxn];
vector<int> mem;
int dfs(int i, int nums = 1)
{
    if (mem[i] != -1)
        return mem[i];
    else if (edge[i].size() > 0)
    {
        mem[i] = 0;
        for (auto e : edge[i])
            mem[i] += dfs(e, nums + 1);
        return mem[i];
    }
    else if (edge[i].size() == 0 && nums > 1)
        return 1;
    return 0;
}

int main()
{
    int n, m, a, b;
    queue<int> que;
    scanf("%d%d", &n, &m);
    for (int i = 0; i < m; ++i)
    {
        scanf("%d%d", &a, &b);
        in[b]++;
        edge[a].push_back(b);
    }
    mem.push_back(-1);
    for (int i = 1; i <= n; ++i)
    {
        mem.push_back(-1);
        if (in[i] == 0)
            que.push(i);
    }
    int res = 0;
    while (!que.empty())
    {
        auto i = que.front();
        que.pop();
        res += dfs(i);
    }
    printf("%d", res);
    return 0;
}