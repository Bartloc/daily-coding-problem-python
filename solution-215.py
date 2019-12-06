class Node():
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
  

def tree_bottom_view(node):
    def tree_travers(node,hds=None,hd=0,lev=0):
        if not hds:
            hds={}

        if hd not in hds.keys():
            hds[hd]=(lev,node.val)
        elif hds[hd][0]<lev:
            hds[hd]=(lev,node.val)

        if node.left:
            tree_travers(node.left,hds,hd-1,lev+1)
        if node.right:
            tree_travers(node.right,hds,hd+1,lev+1)

        return hds
    return [p[1] for p in tree_travers(node).values()]



b=Node(5,Node(3,Node(1,Node(0,None,None),None),Node(4,None,None)),\
  Node(7,Node(6,None,None),Node(9,Node(8,None,None),None)))

assert tree_bottom_view(b)==[4, 3, 1, 0, 8, 9]
