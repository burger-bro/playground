from typing import List
class Node:
    def __init__(self, val, ending=False):
        self.val = val
        self.ending = ending
        self.next = {}
    
    def __str__(self):
        s1 = "val " + self.val + '\n'
        s2 = "son "
        for n in self.next.values():
            s2 += n.val + ' '
        return s1 + s2 + ("E" if self.ending else "") + '\n'


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        those_folder = set(folder)
        ret = []
        for f in folder:
            root = f.rsplit('/', 1)[0]
            if root not in those_folder:
                ret.append(f)
        print(ret)
        return ret

    def removeSubfolders(self, folder: List[str]) -> List[str]:
        ret = []
        n = len(folder)
        for i in range(n):
            flag = True
            for j in range(n):
                if i == j: continue
                if folder[i].startswith(folder[j]):
                    flag = False
                    break
            if flag:
                ret.append(folder[i])
        return ret
    
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        # build prefix tree
        root = Node('')
        for f in folder:
            f_list = f.split('/')[1:]
            cur = root
            for ff in f_list:
                if ff not in cur.next:
                    new_node = Node(ff)
                    cur.next[ff] = new_node
                cur = cur.next[ff]
            cur.ending = True

        # traverse the tree
        ret = []
        def traverse(root: Node, path):
            print(root)
            nxt_path = path + '/' + root.val
            if root.ending:
                ret.append(nxt_path[1:])
                return
            for k, v in root.next.items():
                traverse(v, nxt_path)
            return 
        traverse(root, '')
        print(ret)
        return ret
            


su = Solution()
# case bug
folder = ["/ah/al/am","/ah/al"]
res = su.removeSubfolders(folder)
ans = ["/ah/al"]
assert(res == ans)

# case std1
folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
res = su.removeSubfolders(folder)
ans = ["/a","/c/d","/c/f"]
assert(res == ans)

