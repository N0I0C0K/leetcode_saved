#include <iostream>
#include <queue>

using namespace std;

class Solution
{
public:
    void insert(int num)
    {
        this->maxHeap.push(num);
        if (maxHeap.size() > minHeap.size() + 1)
        {
            auto t = maxHeap.top();
            maxHeap.pop();
            minHeap.push(t);
        }
        while (minHeap.size() && maxHeap.top() > minHeap.top())
        {
            auto t1 = maxHeap.top();
            auto t2 = minHeap.top();
            maxHeap.pop();
            maxHeap.push(t2);
            minHeap.pop();
            minHeap.push(t1);
        }
    }

    double getMedian()
    {
        if (maxHeap.size() == minHeap.size())
            return (maxHeap.top() + minHeap.top()) / 2.0;
        else
            return maxHeap.top();
    }

private:
    priority_queue<int> maxHeap;
    priority_queue<int, vector<int>, greater<int>> minHeap;
};