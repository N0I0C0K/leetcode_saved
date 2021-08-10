#A* 算法实现
from typing import List
import random
import heapq

class Node: #保存节点信息
    x:int   #x
    y:int   #y
    cost:int    #f(x)代价
    def __init__(self, x, y, cost) -> None:
        self.x = x
        self.y = y
        self.cost = cost
    
    def __str__(self) -> str:
        return f'{self.x} {self.y}'

    def __lt__(self, b):    #比较函数，用于排序
        if isinstance(b, Node):
            return self.cost < b.cost   #按照花费从小到大排序
        return True

map:List[List[int]] = []       #以二维数组为地图, 0:空地, 1:障碍, 2:起点, 3:终点
comefrom:List[List[Node]] = []  #保存路径信息
vis:List[List[bool]] = []       #储存节点是否访问过
dir = [[1,0],[-1,0],[0,1],[0,-1]]   #四个方向，上下左右


#代价函数，使用曼哈顿距离作为代价函数
def dist(x1,y1,x2,y2) -> int:
    return abs(x1-x2)+abs(y1-y2)


def Astar(posInfo:list):
    width = (len(map[0]))
    height = len(map)
    que:List[Node] = []     #使用小顶堆优先队列，优化时间复杂度
    heapq.heappush(que, Node(posInfo[0][0], posInfo[0][1], dist(posInfo[0][0], posInfo[0][1], posInfo[1][0], posInfo[1][1])))
    while len(que) > 0:
        t = heapq.heappop(que)  #每次弹出f(x)最小的节点进行搜索
        if t.x >= height or t.x < 0 or t.y >= width or t.y < 0 or vis[t.x][t.y]:    #判断是否超出边界
            continue
        #print(f'{t.x} {t.y}')
        vis[t.x][t.y] = True
        if map[t.x][t.y] == 1:  #如果遇到障碍，跳出
            continue
        elif map[t.x][t.y] == 3: #抵达终点
            return True
        else:
            for i in range(4):  #将此节点周围四个节点弹入
                tx = t.x+dir[i][0]
                ty = t.y+dir[i][1]
                heapq.heappush(que, Node(tx, ty, dist(tx,ty, posInfo[1][0], posInfo[1][1])))
                if tx>=0 and tx<height and ty>=0 and ty<width:
                    comefrom[tx][ty] = t
    return False

def printRoute(posInfo):    #打印路径，使用回溯算法
    pos = posInfo[0]
    print(f'{pos[0]} {pos[1]}')
    while dist(pos[0],pos[1], posInfo[1][0], posInfo[1][1]) > 1:
        print(comefrom[pos[0]][pos[1]])
        pos = comefrom[pos[0]][pos[1]].x, comefrom[pos[0]][pos[1]].y
    print(f'{posInfo[1][0]} {posInfo[1][1]}')

def initMap(width:int, height:int)-> list: #初始化地图（随机）
    hasEnd = False
    hasStart = False
    res = [[0,0],[height-1,width-1]]
    for h in range(height):
        vis.append([False]*width)
        comefrom.append([None]*width)
        temp = []
        for w in range(width):
            a = random.randint(1,100)
            b = 0
            if a>= 75:
                b = 1
            
            temp.append(b)
        map.append(temp.copy())
    if not hasStart:
        map[0][0] = 2
    if not hasEnd:
        map[height-1][width-1] = 3
    for l in map:
        print(str(l).replace(',',' '))
    return res

def main():
    pos = initMap(10, 10)
    print(pos)
    if Astar(pos):
        print('Yes')
        printRoute(pos)
    else:
        print('No')
    pass

if __name__ == '__main__':
    main()