from typing import List

class Node:
    def __init__(self, val):
        self.val = val
        self.next: dict[str:Node] = {}
        self.parent = None
        self.delete = False
        self.ending = False

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        # build tree
        root = Node('')
        for path in paths:
            cur = root
            for p in path:
                if p not in cur.next:
                    new_node = Node(p)
                    cur.next[p] = new_node
                    new_node.parent = cur
                cur = cur.next[p]
            cur.ending = True
        # traverse the tree to find leaf nodes
        leaf_dict = {}
        def dfs(root):
            if not root.next:
                if root.val not in leaf_dict:
                    leaf_dict[root.val] = [root]
                else:
                    leaf_dict[root.val].append(root)
                return
            for n in root.next.values():
                dfs(n)
            return
        dfs(root)
        print(leaf_dict)
        # mark func
        def mark(tmp_d: dict[str: List[Node]]):
            if not tmp_d:
                return
            new_dict = {}
            for k, v in tmp_d.items():
                if len(v) == 1:
                    v[0].delete = True
                else:
                    for n in v:
                        n.delete = True
                        if n.parent is not None:
                            n = n.parent
                            if n.val not in new_dict:
                                new_dict[n.val] = [n]
                            else:
                                new_dict[n.val].append(n)
            mark(new_dict)

        # deal the replicate path
        for k, v in leaf_dict.items():
            if len(v) == 1: continue
            tmp_dict = {k: v}
            mark(tmp_dict)

        # collect ans
        ret = []
        def dfs(root, path):
            new_p = (path+[root.val]) if root.val else path
            print("dbg", new_p)
            if root.ending and not root.delete:
                ret.append(new_p)
            for nxt in root.next.values():
                dfs(nxt, new_p)
        dfs(root, [])
        print("ret", ret)
        return ret

        
su = Solution()
# case std1
paths = [["a"],["c"],["d"],["a","b"],["c","b"],["d","a"]]
res = su.deleteDuplicateFolder(paths)
ans = [["d"],["d","a"]]
assert(res == ans)
