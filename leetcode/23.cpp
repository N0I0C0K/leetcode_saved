#include <queue>

using namespace std;
//Definition for singly-linked list.
struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

struct cmp
{
    bool operator()(ListNode *a, ListNode *b)
    {
        return a->val >= b->val;
    }
};

class Solution
{
public:
    ListNode *mergeKLists(vector<ListNode *> &lists)
    {
        priority_queue<ListNode *, vector<ListNode *>, cmp> pqueue;
        ListNode *res = new ListNode();
        for (auto item : lists)
        {
            if (item)
                pqueue.push(item);
        }
        ListNode *head = res;
        while (!pqueue.empty())
        {
            auto te = pqueue.top();
            pqueue.pop();
            if (!te)
                continue;
            head->next = te;
            if (te->next)
                pqueue.push(te->next);
            te->next = nullptr;
            head = te;
        }
        return res->next;
    }
};