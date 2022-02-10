#include <queue>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
using ll = long long;
using uint = unsigned int;
const int inf = 0x3f3f3f3f;

using tType = long long;  //数据要求的类型
const int maxn = 1e6 + 5; //数的个数
int xx[maxn << 1];        //离散化的x

inline int ls(int k) { return k << 1; }     //返回k的左孩子
inline int rs(int k) { return k << 1 | 1; } //返回k的右孩子

struct ScanLine
{
    int l, r, y;
    int mark;
    void set(int l, int r, int y, int mark)
    {
        this->l = l;
        this->r = r;
        this->mark = mark;
        this->y = y;
    }
} line[maxn << 1];

bool cmp(ScanLine &l, ScanLine &r) { return l.y < r.y; }

struct SegTree
{
    int l, r, sum, len;

} tree[maxn << 2];

void pushup(int x)
{
    int l = tree[x].l, r = tree[x].r;
    if (tree[x].sum)
        tree[x].len = xx[r + 1] - xx[l];
    else
        tree[x].len = tree[ls(x)].len + tree[rs(x)].len;
}

void build(int x, int l, int r)
{
    tree[x].l = l;
    tree[x].r = r;
    tree[x].len = 0;
    tree[x].sum = 0;
    if (l == r)
        return;
    int mid = (l + r) >> 1;
    build(ls(x), l, mid);
    build(rs(x), mid + 1, r);
}

void update(int x, int ql, int qr, int mark)
{
    int l = tree[x].l, r = tree[x].r;
    if (xx[r + 1] <= ql || qr <= xx[l])
        return;
    if (ql <= xx[l] && xx[r + 1] <= qr)
    {
        tree[x].sum += mark;
        pushup(x);
        return;
    }
    update(ls(x), ql, qr, mark);
    update(rs(x), ql, qr, mark);
    pushup(x);
}

int main()
{
    int n;
    scanf("%d", &n);
    int x1, y1, x2, y2;
    for (int i = 1; i <= n; ++i)
    {
        scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
        xx[i * 2 - 1] = x1, xx[i * 2] = x2;
        line[i * 2 - 1].set(x1, x2, y1, 1);
        line[i * 2].set(x1, x2, y2, -1);
    }
    n <<= 1;
    sort(line + 1, line + 1 + n, cmp);
    sort(xx + 1, xx + 1 + n);
    int tol = unique(xx + 1, xx + 1 + n) - xx - 1;
    build(1, 1, tol - 1);
    ll ans = 0;
    for (int i = 1; i < n; ++i)
    {
        update(1, line[i].l, line[i].r, line[i].mark);
        ans += ll(tree[1].len) * (line[i + 1].y - line[i].y);
    }
    printf("%lld", ans);
    return 0;
}