#include <iostream>
#include <algorithm>
using namespace std;
typedef long long ll;

int main()
{
    // freopen("a5.in", "r", stdin);
    // freopen("a5.out", "w", stdout);
    int t;
    cin >> t;
    ll x, y;
    while (t--)
    {
        cin >> x >> y;
        if (x == y)
        {
            cout << x << endl;
            continue;
        }
        if (x > y)
        {
            cout << x + y << endl;
        }
        else
        {
            cout << y - (y % x) / 2 << endl;
        }
    }
    return 0;
}
