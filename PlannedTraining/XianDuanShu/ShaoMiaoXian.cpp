//  https://www.luogu.com.cn/problem/P5490
// 扫描线模板
#include <queue>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
using ll = long long;
using uint = unsigned int;
const int inf = 0x3f3f3f3f;

using tType = long long;                           //数据要求的类型
const int maxn = 1e5 + 5;                          //数的个数
int cover[maxn << 2], length[maxn << 2], yy[maxn]; //节点覆盖, 长度, 离散化的y

inline int ls(int k) { return k << 1; }     //返回k的左孩子
inline int rs(int k) { return k << 1 | 1; } //返回k的右孩子

struct ScanLine
{
    int x, upy, downy, inout;
    ScanLine() {}
    ScanLine(int x, int upy, int downy, int inout) : x(x), upy(upy), downy(downy), inout(inout) {}
} line[maxn];

bool cmp(ScanLine &l, ScanLine &r) { return l.x < r.x; }

void pushup(int l, int r, int rt)
{
    if (cover[rt])
        length[rt] = yy[r] - yy[l];
    else if (l + 1 == r)
        length[rt] = 0;
    else
        length[rt] = length[ls(rt)] + length[rs(rt)];
}

void update(int yl, int yr, int io, int l, int r, int rt)
{
    if (yl > r || yr < l)
        return;
    if (yl <= l && r <= yr)
    {
        cover[rt] += io;
        pushup(l, r, rt);
        return;
    }
    if (l + 1 == r)
        return;
    int m = (l + r) >> 1;
    if (yl <= m)
        update(yl, yr, io, l, m, ls(rt));
    if (yr > m)
        update(yl, yr, io, m, r, rs(rt));
    pushup(l, r, rt);
}

int main()
{
    int n;
    scanf("%d", &n);
    int x1, y1, x2, y2;
    int cnt = 0;
    for (int i = 0; i < n; ++i)
    {
        scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
        line[++cnt] = ScanLine(x1, y2, y1, 1);
        yy[cnt] = y1;
        line[++cnt] = ScanLine(x2, y2, y1, -1);
        yy[cnt] = y2;
    }
    sort(yy + 1, yy + cnt + 1);
    sort(line + 1, line + 1 + cnt, cmp);
    int len = unique(yy + 1, yy + 1 + cnt) - yy - 1;
    memset(cover, 0, sizeof cover);
    memset(length, 0, sizeof length);
    ll ans = 0;
    int yl, yr;
    for (int i = 1; i <= cnt; ++i)
    {
        ans += length[1] * (line[i].x - line[i - 1].x);
        yl = lower_bound(yy + 1, yy + len + 1, line[i].downy) - yy;
        yr = lower_bound(yy + 1, yy + len + 1, line[i].upy) - yy;
        update(yl, yr, line[i].inout, 1, len, 1);
    }
    printf("%lld", ans);
    return 0;
}