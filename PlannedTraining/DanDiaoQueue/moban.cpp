// https://www.luogu.com.cn/problem/P1886
// 单调队列模板
#include <queue>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
using ll = long long;
using uint = unsigned int;
const int inf = 0x3f3f3f3f;

const int maxn = 1e6 + 5;
int a[maxn];

int main()
{
    int n, k;
    scanf("%d%d", &n, &k);
    deque<int> mque; //单调递减队列, front储存最大值
    deque<int> aque; //单调递增队列, front储存最小值
    for (int i = 1; i <= n; ++i)
    {
        scanf("%d", a + i);
    }
    for (int i = 1; i <= n; i++)
    {
        while (!aque.empty() && a[aque.back()] > a[i])
        {
            aque.pop_back();
        }
        aque.push_back(i);
        if (i >= k)
        {
            while (!aque.empty() && aque.front() < i - k + 1)
            {
                aque.pop_front();
            }
            printf("%d%c", a[aque.front()], i < n ? ' ' : '\n');
        }
    }
    for (int i = 1; i <= n; ++i)
    {
        while (!mque.empty() && a[mque.back()] < a[i])
        {
            mque.pop_back();
        }
        mque.push_back(i);

        if (i >= k)
        {
            while (!mque.empty() && mque.front() < i - k + 1)
            {
                mque.pop_front();
            }
            printf("%d%c", a[mque.front()], i < n ? ' ' : '\n');
        }
    }
    return 0;
}