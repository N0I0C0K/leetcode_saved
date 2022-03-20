#include <queue>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
using ll = long long;
using uint = unsigned int;
const int inf = 0x3f3f3f3f;

int nums1[10010], nums2[10010];
int main()
{
    int a, b, c;
    while (scanf("%d%d%d", &a, &b, &c))
    {
        for (int i = 0; i < a; ++i)
            scanf("%d", nums1 + i);
        for (int i = 0; i < b; ++i)
            scanf("%d", nums2 + i);
        sort(nums1, nums1 + a);
        sort(nums2, nums2 + b);
        int t = 0, temp = 0;
        int ta = 0, tb = 0;
        while (t < c)
        {
            temp = nums1[ta] * nums2[tb];
            if (nums1[ta] < nums2[tb])
            {
                if (tb < b - 1)
                    ++tb;
                else
                    ++ta;
            }
            else
            {
                if (ta < a - 1)
                    ++ta;
                else
                    ++tb;
            }
            ++t;
        }
        printf("%d\n", temp);
    }
}