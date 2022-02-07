// https://www.luogu.com.cn/problem/P3372
#include <queue>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
using ll = long long;
using uint = unsigned int;
const int inf = 0x3f3f3f3f;

using cType = long long;                                        //数据要求的类型
const int maxn = 1e5 + 5;                                       //数的个数
cType a[maxn] = {0}, t[maxn << 2] = {0}, lazy[maxn << 2] = {0}; //原数组, 线段树组, lazy标记

inline int ls(int k) { return k << 1; }     //返回k的左孩子
inline int rs(int k) { return k << 1 | 1; } //返回k的右孩子

void Pushup(int k)
{
    t[k] = t[ls(k)] + t[rs(k)];
}

void Pushdown(int k, int l, int r)
{
    if (lazy[k])
    {
        int mid = (l + r) >> 1;
        lazy[ls(k)] += lazy[k];
        lazy[rs(k)] += lazy[k];
        t[ls(k)] += lazy[k] * (mid - l + 1);
        t[rs(k)] += lazy[k] * (r - mid);
        lazy[k] = 0;
    }
}

void build(int k, int l, int r)
{
    if (l == r)
    {
        t[k] = a[l];
        return;
    }
    else
    {
        int m = (l + r) >> 1;
        build(ls(k), l, m);
        build(rs(k), m + 1, r);
        Pushup(k);
    }
}

//查询[ql,qr]区间内的和
cType query(int ql, int qr, int l, int r, int k)
{
    if (ql <= l && r <= qr)
    {
        return t[k];
    }
    else
    {
        Pushdown(k, l, r);
        cType res = 0;
        int mid = (l + r) >> 1;
        if (ql <= mid)
            res += query(ql, qr, l, mid, ls(k));
        if (qr > mid)
            res += query(ql, qr, mid + 1, r, rs(k));
        return res;
    }
}

//将区间内[ul,ur]所有加上v
void update(int ul, int ur, cType v, int l, int r, int k)
{
    if (ul <= l && r <= ur)
    {
        lazy[k] += v;
        t[k] += v * (r - l + 1);
    }
    else
    {
        Pushdown(k, l, r);
        int m = (l + r) >> 1;
        if (ul <= m)
            update(ul, ur, v, l, m, ls(k));
        if (ur > m)
            update(ul, ur, v, m + 1, r, rs(k));
        Pushup(k);
    }
}

int main()
{
    int n, m;
    scanf("%d%d", &n, &m);
    for (int i = 1; i <= n; ++i)
    {
        scanf("%lld", a + i);
    }
    build(1, 1, n);
    int mod, x, y;
    while (m--)
    {
        scanf("%d%d%d", &mod, &x, &y);
        if (mod == 1)
        {
            scanf("%d", &mod);
            update(x, y, mod, 1, n, 1);
        }
        else
        {
            printf("%lld\n", query(x, y, 1, n, 1));
        }
    }
    return 0;
}