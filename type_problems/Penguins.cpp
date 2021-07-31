#include<cstdio>
#include<iostream>
#include<queue>
#include<cstring>
#include<string>
using namespace std;
struct Node
{
    int x1,y1,x2,y2;
    string s;
    Node(int a,int b,int c,int d,string e){x1 = a,y1 = b,x2 = c,y2 = d,s = e;}
};

char map[2][25][25];
bool vis[21][21][21][21];
int dx[4] = {1,-1,0,0};
int dy[4][2] = {{0,0},{0,0},{-1,1},{1,-1}};
Node bfs()
{
    queue<Node> que;
    Node* ans;
    que.emplace(20,20,20,1,"");
    //vis[20][20][20][1] = true;
    while (!que.empty())
    {
        //printf("a\n");
        auto t = que.front();
        que.pop();
        if(vis[t.x1][t.y1][t.x2][t.y2]){
            continue;
        }
        vis[t.x1][t.y1][t.x2][t.y2] = true;
        if(t.x1 == 1 && t.y1 == 20 && t.x2 == 1 && t.y2 == 1)
        {
            ans = &t;
            return *ans;
        }
        Node temp = Node(t.x1,t.y1,t.x2,t.y2,t.s);
        if(temp.x1+1 <= 20 && map[0][temp.x1+1][temp.y1] != '#')
        {
            temp.x1+=1;
        }
        if(temp.x2+1 <= 20 && map[1][temp.x2+1][temp.y2] != '#')
        {
            temp.x2+=1;
        }
        temp.s += 'D';
        que.emplace(temp.x1, temp.y1, temp.x2, temp.y2, temp.s);
        temp = Node(t.x1,t.y1,t.x2,t.y2,t.s);
        if(temp.x1-1 > 0 && map[0][temp.x1-1][temp.y1] != '#')
        {
            temp.x1-=1;
        }
        if(temp.x2-1 > 0 && map[1][temp.x2-1][temp.y2] != '#')
        {
            temp.x2-=1;
        }
        temp.s += 'U';
        que.emplace(temp.x1, temp.y1, temp.x2, temp.y2, temp.s);
        temp = Node(t.x1,t.y1,t.x2,t.y2,t.s);
        if(temp.y1+1<=20 && map[0][temp.x1][temp.y1+1] != '#')
        {
            temp.y1 += 1;
        }
        if(temp.y2-1>0 && map[1][temp.x2][temp.y2-1] != '#')
        {
            temp.y2 -= 1;
        }
        temp.s += 'R';
        que.emplace(temp.x1, temp.y1, temp.x2, temp.y2, temp.s);
        temp = Node(t.x1,t.y1,t.x2,t.y2,t.s);
        if(temp.y1-1>0 && map[0][temp.x1][temp.y1-1] != '#')
        {
            temp.y1 -= 1;
        }
        if(temp.y2+1<=20 && map[1][temp.x2][temp.y2+1] != '#')
        {
            temp.y2 += 1;
        }
        temp.s += 'L';
        que.emplace(temp.x1, temp.y1, temp.x2, temp.y2, temp.s);
    }
    return *ans;
}

void printMap(Node node)
{

}

 int main()
 {
    for (size_t i = 1; i <= 20; ++i)
    {
        scanf("%s %s",map[0][i],map[1][i]);
    }
    memset(vis, false, sizeof(vis));
    //printf("start\n");
    auto a = bfs();
    cout<<a.s.size()<<" "<<a.s<<endl;
    return 0;
 }