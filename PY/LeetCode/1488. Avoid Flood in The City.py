from typing import List
from collections import defaultdict

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        seen = defaultdict(int)
        dry_chance = 0
        dry = []
        start = False
        for r in rains:
            if r == 0:
                if start:
                    dry_chance += 1
                continue
            start = True
            seen[r] += 1
            if seen[r] == 2:
                if dry_chance:
                    seen[r] -= 1
                    dry_chance -= 1
                    dry.append(r)
                else:
                    return []
        cnt = 0
        ret = []
        for r in rains:
            if r > 0:
                ret.append(-1)
            elif cnt < len(dry):
                ret.append(dry[cnt])
                cnt += 1
            else:
                ret.append(1)
        return ret



from typing import List
from collections import defaultdict

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        seen = defaultdict(int)
        dry_chance = 0
        dry = []
        cnt = 0
        while rains[cnt] == 0:
            cnt += 1
        rains = rains[cnt:]
        rains = rains[::-1]
        cnt = 0
        while rains[cnt] == 0:
            cnt += 1
        for r in rains:
            if r == 0:
                dry_chance += 1
                continue
            seen[r] += 1
            if seen[r] == 2:
                if dry_chance:
                    seen[r] -= 1
                    dry_chance -= 1
                    dry.append(r)
                else:
                    return []
        cnt = 0
        ret = []
        for r in rains:
            if r > 0:
                ret.append(-1)
            elif cnt < len(dry):
                ret.append(dry[cnt])
                cnt += 1
            else:
                ret.append(1)
        return ret[::-1]
            