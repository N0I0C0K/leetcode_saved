#include <cstdio>
using namespace std;

struct Node
{
    int x;      //这个节点的值
    Node *next; //下一个节点的地址
    Node(int x, Node *next = nullptr)
    {
        this->x = x;
        this->next = next;
    }
};
Node *head = nullptr;

void pushEnd(int x)
{
    Node *tail = head;
    while (tail->next != nullptr)
        tail = tail->next;
    Node *n = new Node(x);
    tail->next = n;
}

Node *search(int x)
{
    Node *tail = head->next;
    while (tail != nullptr)
    {
        if (tail->x == x)
            return tail;
        tail = tail->next;
    }
    return nullptr;
}

Node *lsearch(int x)
{
    Node *tail = head;
    while (tail->next != nullptr)
    {
        if (tail->next->x == x)
            return tail;
        tail = tail->next;
    }
    return nullptr;
}

void ddelete(int x)
{
    Node *tar = search(x);
    Node *ltar = lsearch(x);
    if (tar->next == nullptr)
    {
        ltar->next = nullptr;
    }
    else
    {
        ltar->next = tar->next;
    }
}

void pprint()
{
    Node *temp = head->next;
    while (temp)
    {
        printf("%2d ", temp->x);
        temp = temp->next;
    }
    printf("\n");
}

int main(int argc, char const *argv[])
{
    head = new Node(0, nullptr);
    pushEnd(1);
    pushEnd(2);
    pushEnd(3);
    pushEnd(4);
    ddelete(3);
    pprint();
    return 0;
}
