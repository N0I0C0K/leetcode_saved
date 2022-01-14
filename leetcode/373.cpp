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
    vector<vector<int>> kSmallestPairs(vector<int> &nums1, vector<int> &nums2, int k)
    {
        auto cmp = [&](const pair<int, int> &a, const pair<int, int> &b)
        {
            return nums1[a.first] + nums2[a.second] > nums1[b.first] + nums2[b.second];
        };
        int n = nums1.size();
        int m = nums2.size();
        vector<vector<int>> res;
        priority_queue<pair<int, int>, vector<pair<int, int>>, decltype(cmp)> pque(cmp);
        for (int i = 0; i < min(n, k); ++i)
        {
            pque.emplace(i, 0);
        }
        while (k-- > 0 && !pque.empty())
        {
            auto temp = pque.top();
            pque.pop();
            res.emplace_back(initializer_list<int>{nums1[temp.first], nums2[temp.second]});
            if (temp.second + 1 < m)
            {
                pque.emplace(temp.first, temp.second + 1);
            }
        }
        return res;
    }
};