from typing import *


class MyData:
    def __init__(self, key: str, count: int):
        self.key = key
        self.count = count

    def __lt__(self, rhs: 'MyData'):
        return self.count < rhs.count

    def __gt__(self, rhs: 'MyData'):
        return self.count > rhs.count


class Node:
    def __init__(self, key: str = '', count=0) -> None:
        self.key = key
        self.count = count
        self.next: 'Node' = None
        self.pre: 'Node' = None

    def insert(self, node: 'Node'):
        node.pre = self
        node.next = self.next
        self.next = node
        node.next.pre = node

    def remove(self):
        self.pre.next = self.next
        self.next.pre = self.pre


class AllOne:
    def __init__(self):
        self.data: Dict[str, Node] = {}
        self.head = Node('', 0)
        self.tail = Node('', 1e5)
        self.head.next = self.tail
        self.tail.pre = self.head

    def inc(self, key: str) -> None:
        if key not in self.data:
            n = Node(key, 1)
            self.head.insert(n)
            self.data[key] = n
        else:
            n = self.data[key]
            n.count += 1
            t = n.next
            while n.count > t.count:
                t = t.next
            n.remove()
            t.insert(n)

    def dec(self, key: str) -> None:
        n = self.data[key]
        if n.count == 1:
            n.remove()
            self.data.pop(key)
        else:
            n.count -= 1
            t = n.next
            while n.count < t.count:
                t = t.next
            n.remove()
            t.insert(n)

    def getMaxKey(self) -> str:
        return self.maxd.key

    def getMinKey(self) -> str:
        return self.mind.key
