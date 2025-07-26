from typing import List

class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 10**9+1
        ret = 0
        for i in range(1, len(nums)-1):
            target = nums[i]*2
            left_idx = i-1
            left_cnt = 0
            while left_idx >= 0:
                if nums[left_idx] == target:
                    left_cnt += 1
                left_idx -= 1
            if left_cnt == 0:
                continue

            right_idx = i+1
            right_cnt = 0
            while right_idx <= len(nums)-1:
                if nums[right_idx] == target:
                    right_cnt += 1
                right_idx += 1
            if right_cnt == 0:
                continue
            ret += left_cnt*right_cnt
            ret %= MOD
        print(ret)
        return ret
            
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 10**9+1

        ik_dict = {}
        for idx, n in enumerate(nums):
            if n not in ik_dict:
                ik_dict[n] = [idx]
            else:
                ik_dict[n].append(idx)
        print(ik_dict)
        del_key = []
        for k, v in ik_dict.items():
            if len(v) == 1:
                del_key.append(k)
        for k in del_key:
            del ik_dict[k]
        print(ik_dict)

        ret = 0
        for i in range(1, len(nums)-1):
            target = nums[i]*2
            if target not in ik_dict:
                continue
            print("search target", target, i)
            left_num = 0
            right_num = 0
            for j in range(len(ik_dict[target])): ## ==case 
                if ik_dict[target][j] < i:
                    left_num += 1
                elif i < ik_dict[target][j]:
                    right_num += 1
            ret += left_num*right_num
            ret %= MOD

        print(ret)
        return ret


    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 10**9+1

        ik_dict = {}
        for idx, n in enumerate(nums):
            if n not in ik_dict:
                ik_dict[n] = [idx]
            else:
                ik_dict[n].append(idx)
        print(ik_dict)
        del_key = []
        for k, v in ik_dict.items():
            if len(v) == 1:
                del_key.append(k)
        for k in del_key:
            del ik_dict[k]
        print(ik_dict)

        ret = 0
        for i in range(1, len(nums)-1):
            target = nums[i]*2
            if target not in ik_dict:
                continue
            left_num = 0
            right_num = 0
            print("search target", target, i)
            left, right = 0, len(ik_dict[target])
            # get right
            while left < right:
                mid = left + (right-left)//2
                if ik_dict[target][mid] > i:
                    right = mid
                elif ik_dict[target][mid] <= i:
                    left = mid+1
            right_num = len(ik_dict[target])-right
            print("rr", right_num , right)
            # get left
            left, right = 0, len(ik_dict[target])-1
            while left < right:
                mid = left + (right-left)//2
                print("lmidr", left, mid, right)
                if ik_dict[target][mid] >= i:
                    right = mid-1
                elif ik_dict[target][mid] < i:
                    left = mid+1
            left_num = left+1 if ik_dict[target][0] != i else 0
            print("ll", left_num , left)


            ret += left_num*right_num
            print("inner ret", ret)
            ret %= MOD

        print(ret)
        return ret

su = Solution()
# case bug3
nums = [56,56,87,28,55,56,94]
res = su.specialTriplets(nums)
ans = 2
assert(res == ans)

# case bug2
nums = [46,54,0,23,46,69,15,0,0,30]
res = su.specialTriplets(nums)
ans = 2
assert(res == ans)

# case bug
nums = [28,52,14,28,34,26,14,52]
res = su.specialTriplets(nums)
ans = 2
assert(res == ans)

# case bug
nums = [84,2,93,1,2,2,26]
res = su.specialTriplets(nums)
ans = 2
assert(res == ans)

# case std1
nums = [6,3,6]
res = su.specialTriplets(nums)
ans = 1
assert(res == ans)

# case std2
nums = [0,1,0,0]
res = su.specialTriplets(nums)
ans = 1
assert(res == ans)

# case std3
nums = [8,4,2,8,4]
res = su.specialTriplets(nums)
ans = 2
assert(res == ans)
