import sys
sys.setrecursionlimit(10**6)
class BinaryTree:
    def __init__(self):
        self.root = None
        self.preoder = []
        self.postoder = []
    
    def insert(self, node):
        if self.root:
            cur_node = self.root
            # 만드는 부분 수정?
            while cur_node:
                if cur_node.data > node.data:
                    if cur_node.left:
                        cur_node = cur_node.left
                    else:
                        cur_node.left = node
                        break
                
                else:
                    if cur_node.right:
                        cur_node = cur_node.right
                    else:
                        cur_node.right = node
                        break
        else:
            self.root = node
        
    def _preoder(self, node): # r - l - R
        if node == None:
            return
        self.preoder.append(node.node)
        self._preoder(node.left)
        self._preoder(node.right)
            
    
    def _postorder(self, node): # l - R - r
        if node == None:
            return
        self._postorder(node.left)
        self._postorder(node.right)
        self.postoder.append(node.node)
        
        

class Node:
    def __init__(self, data, node):
        self.data = data
        self.node = node
        self.left = None
        self.right = None
        

def solution(nodeinfo):
    answer = [[]]
    bt = BinaryTree()
    
    nodeinfo = sorted(list(enumerate(nodeinfo)), key=lambda x:[-x[1][1], x[1][0]])
    
    for i in range(len(nodeinfo)):    
        node = Node(nodeinfo[i][1][0], nodeinfo[i][0]+1)
        bt.insert(node)
        
    bt._preoder(bt.root)
    bt._postorder(bt.root)
    
    return [bt.preoder, bt.postoder]