#include <queue>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
using ll = long long;
using uint = unsigned int;
const int inf = 0x3f3f3f3f;

int req[2] = {0, 0};
int has[2] = {0, 0};
char str[200005];
int n = 0;

int main()
{
    scanf("%d", &n);
    scanf("%s", str);
    int a, b;
    scanf("%d%d", &a, &b);
    req[0] = a;
    req[1] = b;
    for (int i = 0; i < n; ++i)
    {
        switch (str[i])
        {
        case 'R':
            ++has[0];
            break;
        case 'L':
            --has[0];
            /* code */
            break;
        case 'U':
            ++has[1];
            /* code */
            break;
        case 'D':
            --has[1];
            /* code */
            break;
        }
    }
    if (abs(req[0] - has[0]) % 2 != 0 || abs(req[1] - has[1]) % 2 != 0)
    {
        printf("-1");
        return 0;
    }
    if (req[0] == has[0] && req[1] == has[1])
    {
        printf("0");
        return 0;
    }
    int mid = inf, mxid = -1;
    for (int i = 0; i < n; ++i)
    {
        switch (str[i])
        {
        case 'R':
            if (has[0] > req[0])
            {
                has[0] -= 2;
                mid = min(i, mid);
                mxid = max(i, mxid);
            }
            break;
        case 'L':
            if (has[0] < req[0])
            {
                has[0] += 2;
                mid = min(i, mid);
                mxid = max(i, mxid);
            }
            break;
        case 'U':
            if (has[1] > req[1])
            {
                has[1] -= 2;
                mid = min(i, mid);
                mxid = max(i, mxid);
            }
            break;
        case 'D':
            if (has[1] < req[1])
            {
                has[1] += 2;
                mid = min(i, mid);
                mxid = max(i, mxid);
            }
            break;
        }
    }
    if (req[0] == has[0] && req[1] == has[1])
    {
        printf("%d", mxid - mid + 1);
    }
    else
    {
        printf("-1");
    }
    return 0;
}