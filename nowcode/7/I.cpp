#include<cstdio>
#include<cmath>
using uint = unsigned int;
using ull = unsigned long long;

int bitNumber1 (ull number) {
    int ret = 0;
 
    while (number != 0) {
        if ((number & 1) == 1)
            ret++;
        number = number >> 1;
    }
    return ret;
}

bool can(ull a,ull b)
{
    ull ta;
    ull tb;
    while(a!=0 || b!=0)
    {
        ta = a&1;
        tb = b&1;
        if(ta == 1 && tb != 1)
            return false;
        a = a>>1;
        b = b>>1;
    }
    return true;
}

int main()
{
    ull x,s;
    scanf("%llu%llu",&x,&s);
    ull t = x&s;
    if(!can(x,s))
        printf("0");
    else
    {
        t = bitNumber1(t);
        t = pow(2, t);
        if(x == s)
            t-=1;
        printf("%llu",t);
    }
    return 0;
}