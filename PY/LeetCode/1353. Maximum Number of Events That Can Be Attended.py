from typing import List
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda x: (x[1], x[0]))
        attend = 0
        ret = 0
        print(events)
        for i in range(len(events)):
            if events[i][0] <= attend <= events[i][1]:
                ret += 1
                attend += 1
            elif attend < events[i][0]:
                attend = events[i][0] + 1
                ret += 1
            elif attend > events[i][1]:
                continue
        
        print(ret)
        return ret

    def maxEvents(self, events: List[List[int]]) -> int:
        import heapq
        events.sort(key=lambda x: x[0])
        min_heap = []
        heapq.heapify(min_heap)
        day = events[0][0]
        ret = 0
        for start, end in events:
            while min_heap and min_heap[0] < day:
                heapq.heappop(min_heap)
            if start > day:
                day = start
            heapq.heappush(min_heap, end)
            if min_heap:
                heapq.heappop(min_heap)
                ret += 1
                day += 1

        print(ret)
        return ret

su = Solution()
# case bug
events = [[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7]]
res = su.maxEvents(events)
ans = 7
assert(res == ans)
