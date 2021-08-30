#include<cstdio>
using namespace std;
using ll = long long;
using uint = unsigned int;
const int inf = 0x3f3f3f3f;

int main()
{
    int t,x,res;
    scanf("%d",&t);
    while (t--)
    {
        res = 0;
        scanf("%d",&x);
        if(x == 1)
        {
            printf("2\n");
            continue;
        }
        res += (x+1)/2;
        int temp = x-(x-1)/3;
        res += temp/2;
        if((x&1) && (temp&1))
            res++;
        printf("%d\n",res);
    }
    return 0;
}