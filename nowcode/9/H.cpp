#include<cstdio>
using namespace std;

int nu[4] = {2,3,6,0};
int mm[100];

int main()
{
    int n;
    scanf("%d",&n);
    int x,y,i = 0;
    do
    {
        --n;
        x = n/3;
        y = n%3;
        n = x;
        mm[i++] = y;
    } while (x!=0);
    for (int k = i-1; k >= 0; --k)
    {
        printf("%d",nu[mm[k]]);
    }
    

    return 0;
}