#include <set>
#include <unordered_map>
#include <unordered_set>
#include <queue>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
using ll = long long;
using uint = unsigned int;
const int inf = 0x3f3f3f3f;

struct node
{
    int x, y;
    node(int x, int y) : x(x), y(y) {}
};

// struct cmp
// {
//     bool operator()(node a, node b)
//     {
//         return a.w >= b.w;
//     }
// };

// int ggetW(int x1, int y1, int x2, int y2)
// {
//     return abs(x1 - x2) + abs(y1 - y2);
// }

// class Solution1
// {
// public:
//     unordered_map<ll, bool> tmap;
//     unordered_map<ll, bool> vis;
//     int dir[4][2] = {{0, 1}, {0, -1}, {1, 0}, {0, -1}};
//     bool isEscapePossible(vector<vector<int>> blocked, vector<int> source, vector<int> target)
//     {
//         for (auto &&item : blocked)
//         {
//             tmap.emplace(item[0] * 1e6 + item[1], true);
//         }
//         return Astar(source[0], source[1], target[0], target[1]);
//     }
//     bool outMap(node temp)
//     {
//         return temp.x < 0 || temp.x >= 1e6 || temp.y < 0 || temp.y >= 1e6 || vis[temp.x * 1e6 + temp.y];
//     }
//     bool outMap(int x, int y)
//     {
//         return x < 0 || x >= 1e6 || y < 0 || y >= 1e6 || vis[x * 1e6 + y];
//     }
//     bool Astar(int sx, int sy, int tx, int ty)
//     {
//         priority_queue<node, vector<node>, cmp> que;
//         que.emplace(sx, sy, ggetW(sx, sy, tx, ty));
//         while (!que.empty())
//         {
//             auto temp = que.top();
//             que.pop();
//             if (outMap(temp))
//                 continue;
//             ll key = temp.x * 1e6 + temp.y;
//             vis[key] = true;
//             if (tmap.count(key))
//                 continue;
//             else if (temp.x == tx && temp.y == ty)
//                 return true;
//             else
//             {
//                 for (int i = 0; i < 4; ++i)
//                 {
//                     int x_ = temp.x + dir[i][0], y_ = temp.y + dir[i][1];
//                     if (!outMap(x_, y_))
//                         que.emplace(x_, y_, ggetW(x_, y_, tx, ty));
//                 }
//             }
//         }
//         return false;
//     }
// };

class Solution
{
public:
    int mmax;
    int dir[4][2] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    unordered_set<ll> blockmap;
    bool isEscapePossible(vector<vector<int>> blocked, vector<int> source, vector<int> target)
    {
        for (auto &&item : blocked)
        {
            blockmap.emplace(item[0] * 1e6 + item[1]);
        }
        mmax = ((blocked.size() + 1) * (blocked.size() + 2)) / 2;
        return bfs(source[0], source[1], target[0], target[1]) && bfs(target[0], target[1], source[0], source[1]);
    }
    bool bfs(int x, int y, int tx, int ty)
    {
        unordered_set<ll> vis;
        queue<node> que;
        que.emplace(x, y);
        while ((!que.empty()) && vis.size() <= mmax)
        {
            auto temp = que.front();
            que.pop();
            for (int i = 0; i < 4; ++i)
            {
                int x_ = temp.x + dir[i][0], y_ = temp.y + dir[i][1];
                ll k = x_ * 1e6 + y_;
                if (x_ < 0 || x_ > 1e6 || y_ < 0 || y_ > 1e6 || blockmap.count(k))
                    continue;
                if (vis.count(k))
                    continue;
                if (tx == x_ && ty == y_)
                    return true;
                vis.emplace(k);
                que.emplace(x_, y_);
            }
        }
        return vis.size() > mmax;
    }
};

int main(int argc, char const *argv[])
{
    Solution a;
    if (a.isEscapePossible({{1, 0}, {0, 1}}, {0, 0}, {2, 2}))
    {
        printf("YES");
    }
    return 0;
}
