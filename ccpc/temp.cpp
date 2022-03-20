#include <queue>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
using ll = long long;
using uint = unsigned int;
const int inf = 0x3f3f3f3f;
const int maxn = 1e5;

int numa[maxn], numb[maxn];
int a, b, k;

bool check(int val)
{
    int cnt = 0;
    for (int i = 0, j = b - 1; i < a; ++i)
    {
        while (j >= 0 && numa[i] * numb[j] > val)
            --j;
        cnt += (j + 1);
    }
    return cnt >= k;
}

int find()
{
    int left = numa[0] * numb[0], right = numa[a - 1] * numb[b - 1];
    while (left < right)
    {
        int mid = (left + right) >> 1;
        if (!check(mid))
            left = mid + 1;
        else
            right = mid;
    }
    return left;
}

int main()
{
    while (scanf("%d%d%d", &a, &b, &k) != EOF)
    {
        for (int i = 0; i < a; ++i)
        {
            scanf("%d", numa + i);
        }
        for (int i = 0; i < b; ++i)
        {
            scanf("%d", numb + i);
        }
        sort(numa, numa + a);
        sort(numb, numb + b);
        printf("%d\n", find());
    }
    return 0;
}