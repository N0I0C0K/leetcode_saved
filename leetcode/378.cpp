#include <unordered_set>
#include <iostream>
#include <queue>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
using ll = long long;
using uint = unsigned int;
const int inf = 0x3f3f3f3f;

class Solution
{
public:
    int kthSmallest(vector<vector<int>> matrix, int k)
    {
        auto cmp = [&](const pair<int, int> l, const pair<int, int> r)
        {
            return matrix[l.first][l.second] < matrix[r.first][r.second];
        };
        int n = matrix.size();
        int m = matrix[0].size();
        unordered_set<int> vis;
        priority_queue<pair<int, int>, vector<pair<int, int>>, decltype(cmp)> que(cmp);
        que.emplace(0, 0);
        vis.emplace(0);
        while (!que.empty() && que.size() < k && que.size() < n * m)
        {
            auto temp = que.top();
            if (temp.first + 1 < n && !vis.count((temp.first + 1) * 300 + temp.second))
            {
                que.emplace(temp.first + 1, temp.second);
            }
            if (temp.second + 1 < m && !vis.count(temp.first * 300 + temp.second + 1))
            {
                que.emplace(temp.first, temp.second + 1);
            }
        }
        if (que.size() > k)
        {
            que.pop();
        }
        auto res = que.top();
        return matrix[res.first][res.second];
    }
};

int main()
{
    Solution a;
    cout << a.kthSmallest({{1, 5, 9}, {10, 11, 13}, {12, 13, 15}}, 3) << endl;
    return 0;
}