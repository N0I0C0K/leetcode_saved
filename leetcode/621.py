from typing import List
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_map = Counter(tasks)
        a = list(task_map.values())
        a.sort()
        counts = 0
        len_a = len(a)
        n += 1
        for i in range(0, len_a):
            if i+n >= len_a:
                temp = a[len_a-1]
                counts+=(temp-1)*n
                for j in range(i, len_a):
                    if a[j] == temp:
                        counts+=1
                break
            else:
                if a[i] == 0:
                    continue
                else:
                    temp = a[i]
                    counts+=temp*n
                    for j in range(i,i+n):
                        a[j] -= temp
        return counts

so = Solution()
print(so.leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"], 2))
                

            
    
