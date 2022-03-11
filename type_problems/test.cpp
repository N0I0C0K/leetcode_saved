#include <queue>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
using ll = long long;
using uint = unsigned int;
const int inf = 0x3f3f3f3f;

int a[10];
int idx = 0;
int tail = 0;

void push(int x)
{
    a[idx++] = x;
}

int pop()
{
    if (tail > idx)
        return 0;
    return a[tail++];
}

int main()
{
    return 0;
}