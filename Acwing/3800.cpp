#include<cstdio>
using namespace std;

int nums[100100];
int main()
{
    int t,b,k;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d%d",&b,&k);
        for (size_t i = 1; i <= k; i++)
        {
            scanf("%d",&nums[i]);
        }
        if(b%2 == 0)
        {
            if(nums[k] %2 == 0)
                printf("even\n");
            else
                printf("odd\n");
        }
        else if(b%2 != 0)
        {
            bool ist = true;
            for (size_t i = 1; i <= k; i++)
            {
                if(nums[i]%2 != 0)
                {
                    ist = !ist;
                }
            }
            if(ist)
                printf("even\n");
            else
                printf("odd\n");
        }
        
    }
    return 0;
}