#include<cstdio>

using namespace std;

int nums[100010];
int main()
{
    int n,m,x,y;
    scanf("%d",&n);
    while(n--)
    {
        scanf("%d%d",&m,&x);
        for (size_t i = 0; i < m; i++)
        {
            scanf("%d",&nums[i]);
        }
        int pre = nums[0];
        int all = 0;
        for (size_t i = 1; i < m; i++)
        {
            if(i+1<m)
            {
                if(nums[i] < nums[i-1] && nums[i]<nums[i+1])
                    all++;
            }
            else
            {
                if(nums[i] < nums[i-1])
                    all++;
            }
        }
        printf("%d\n",all);
        if(all<x)
            printf("Yes\n");
        else
            printf("No\n");
        
    }
    return 0;
}