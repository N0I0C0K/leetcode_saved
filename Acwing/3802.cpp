#include<cstdio>
#include<cstdlib>
#include<algorithm>
using namespace std;
int nums[20];

int dfs(int l, int len)
{
    if(len == 1)
        return 1;
    /*int maxl = 1;
    int temp = 1;
    for (size_t i = l+1; i < l+len; ++i)
    {
        if(nums[i] >= nums[i-1])
        {
            temp++;
            if(temp>maxl)
                maxl = temp;
        }
        else
            temp = 1;
    }
    if(maxl >= (int)len/2)
        return maxl;*/
    bool isT = true;
    for (size_t i = l+1; i < l+len; ++i)
    {
        if(nums[i] < nums[i-1])
        {
            isT = false;
            break;
        }
    }
    return isT ? len: max(dfs(l, len/2), dfs(l+len/2, len/2));
}

int main()
{
    system("ifconfig");
    return 0;
}