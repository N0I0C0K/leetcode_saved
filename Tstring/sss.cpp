#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
string t,s;
int n;
int kmp[300000];

string base(int n,int x)
{
    string res = "";
    while (n)
    {
        if(n%x >= 10) res += n%x+'A'-10;
        else res += n%x+'0';
        n/=x;
    }
    reverse(res.begin(), res.end());
    return res;
}

bool kmpf(string a)
{
    int n = a.length();
    int tar = t.length();
    memset(kmp, 0, sizeof kmp);
    for (int i = 1; i < n; ++i)
    {
        int j = kmp[i-1];
        while(j>0&&a[j]!=a[i]) j = kmp[j-1];
        if(s[i] == s[j]) j++;
        kmp[i] = j;
        if(j == tar)
            return true;
    }
    return false;
}

int main()
{
    cin>>n;
    cin>>t;
    for (int i = 2; i <= 16; i++)
    {
        string temp = "";
        for (int j = 1; j <= n; ++j)
        {
           temp += base(j,i);
        }
        if(temp.find(t) != -1)
        {
            printf("yes");
            return 0;
        }
    }
    printf("no");
    return 0;
}