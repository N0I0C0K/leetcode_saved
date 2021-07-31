#include<cstdio>
//#include<queue>
#include<deque>
using namespace std;
using ll = long long int;
const int MAX = 1e5+5;

int n,m;
ll nums[MAX];

ll getnum(int k)
{
    deque<int> minq;
    deque<int> maxq;
    ll ans = 0;
    int j = 0;
    for(int i = 0;i<n;++i)
    {
        while (j<n)
        {
            while(!minq.empty() && nums[minq.back()] >= nums[j])
                minq.pop_back();
            minq.push_back(j);
            while(!maxq.empty() && nums[maxq.back()] <= nums[j])
                maxq.pop_back();
            maxq.push_back(j);
            if(nums[maxq.front()] - nums[minq.front()] > k)
                break;
            j++;
        }
        if(minq.front() == i)
            minq.pop_front();
        if(maxq.front() == i)
            maxq.pop_front();
        ans += ll(n-j);
        
    }
    return ans;
}


int main()
{
    int x;
    scanf("%d%d",&n,&m);
    for (size_t i = 0; i < n; i++)
    {
        scanf("%lld",&nums[i]);
    }
    while(m--)
    {
        scanf("%d",&x);
        printf("%lld\n",getnum(x));
    }
    return 0;
}