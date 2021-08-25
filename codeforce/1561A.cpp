#include<cstdio>
#include<algorithm>
#include<cmath>
using namespace std;
using ll = long long;
using uint = unsigned int;
const int inf = 0x3f3f3f3f;

int nums[1010];
int t,n;
void mswap(int i,int j)
{
    nums[i] = nums[j]^nums[i];
    nums[j] = nums[j]^nums[i];
    nums[i] = nums[j]^nums[i];
}

void fun(int ii)
{
    int res = 0;
    if(ii&1)
    {
        
        for(int i = 1;i<n-1;i+=2)
        {
            if(nums[i]>nums[i+1])
            {
                mswap(i,i+1);
                ++res;
            }
        }
    }
    else
    {
        for (int i = 2; i < n; i+=2)
        {
            if(nums[i]>nums[i+1])
            {
                mswap(i,i+1);
                ++res;
            }
        }
    }
    
}

bool check()
{
    for (int i = 1; i < n; ++i)
    {
        if(nums[i] > nums[i+1])
            return false;
    }
    return true;
}

int main()
{
    scanf("%d",&t);
    while (t--)
    {
        scanf("%d",&n);
        for (int i = 1; i <= n; ++i)
        {
            scanf("%d",nums+i);
        }
        for (int i = 1; i < 1200; i++)
        {
            if(check())
            {
                printf("%d\n",i-1);
                break;
            }
            fun(i);
        }
        
    }
    return 0;
}