#include<cstdio>
using namespace std;

int main()
{
    int n;
    long long int x = 0;
    scanf("%d",&n);
    while (n--)
    {
        scanf("%lld", &x);
        if(x<=6)
            printf("15\n");
        else{
            if(x%2 == 0)
                x = x*(2.5);
            else
                x = (x+1)*(2.5);
            printf("%lld\n",x);
        }
    }
    
}