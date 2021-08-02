#include<cstdio>
#include<algorithm>
#include<cstring>
using namespace std;
const int IINF = 0x3f3f3f3f;
int map[510][510];
int temp[510];
int m,n;


int main()
{
    int s,an;
    scanf("%d%d",&m,&n);
    memset(map, IINF, sizeof(map));
    for (size_t i = 0; i < m; i++)
    {
        s = 0, an = 1;
        while(an != 10)
        {
            scanf("%d",&temp[s++]);
            an = getchar();
        }
        for (size_t j = 0; j < s-1; j++)
        {
            for (size_t k = j+1; k < s; k++)
            {
                map[temp[j]][temp[k]] = 1;
            }
        }
        
    }
    for (size_t i = 1; i <= n; i++)
    {
        for (size_t j = 1; j <= n; j++)
        {
            for (size_t k = 1; k <= n; k++)
            {
                map[j][k] = min(map[j][k], map[j][i]+map[i][k]);
            }
        }
    }
    if(map[1][n] == IINF) printf("NO");
    else printf("%d",map[1][n]-1);
    return 0;

}