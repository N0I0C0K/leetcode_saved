#include<cstdio>
using namespace std;
using ll = long long;
using uint = unsigned int;
const int inf = 0x3f3f3f3f;

int nums[110];
int prefix[110];
int main()
{
    int t,n,idx;
    scanf("%d",&t);
    while (t--)
    {
        scanf("%d",&n);
        scanf("%d",&nums[0]);
        prefix[0] = nums[0];
        idx = nums[0] == 1 ? 0:-1;
        for (int i = 1; i < n; ++i)
        {
            scanf("%d",&nums[i]);
            if(nums[i] == 0)
            {
                prefix[i] = prefix[i-1];
                if (nums[i-1] == 1)
                {
                    prefix[i]++;
                }
                
            }
            else
            {
                prefix[i] = prefix[i-1]+1;
                if(i>=2 && nums[i-1] == 0 && nums[i-2] == 0 && idx!=-1)
                    prefix[i]--;
                idx = i;
            }
        }
        if(idx != -1)
            printf("%d\n",prefix[idx]);
        else
            printf("0\n");
    }
    return 0;
}