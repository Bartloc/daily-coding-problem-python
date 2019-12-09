class Node():
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
    def __repr__(self):
        return ('{}({},{},{})'.format(self.__class__.__name__,self.val,self.left,self.right))

def aritm(a,b,op):
    if op=='+':
        ab=a+b
    elif op=='-':
        ab=a-b
    elif op=='*':
        ab=a*b
    elif op=='/':
        ab=a/b
    else:
        raise Exception('Unknown operator')
    return ab


def eval_tree(root):
    arit='*+-/'
   
    if str(root.val) in arit:
        return aritm(eval_tree(root.left),eval_tree(root.right),root.val)
    elif type(root.val)==float or type(root.val)==int:
        return root.val
    else:
        raise Exception('not a num or {}'.format(arit))
        

assert eval_tree(Node('*',Node('+',Node(3),Node(2)),Node('+',Node(4),Node(5))))==45
