def minMazePath(maze,start,end):
    
    def markPath(a,pos):
        sy,sx=pos
        if sy-1>=0 and  a[sy-1][sx] >= a[sy][sx]:
            a[sy-1][sx] = a[sy][sx]+1
            pos=sy-1,sx
            markPath(a,pos)
        if sy+1<len(a) and a[sy+1][sx] >= a[sy][sx]:
            a[sy+1][sx] = a[sy][sx]+1
            pos=sy+1,sx
            markPath(a,pos)
        if sx-1>=0 and a[sy][sx-1] >= a[sy][sx]:
            a[sy][sx-1] = a[sy][sx]+1
            pos=sy,sx-1
            markPath(a,pos)
        if sx+1<len(a[0]) and a[sy][sx+1] >= a[sy][sx]:
            a[sy][sx+1] = a[sy][sx]+1
            pos=sy,sx+1
            markPath(a,pos)
      
    if maze[end[0]][end[1]]=='t':
        return None
    
    maxint = len(maze)*len(maze[0])
    b=[[maxint  if maze[j][i]=='f' else -1 for i in range(len(maze[0]))] for j in range(len(maze))]
    b[start[0]][start[1]]=0
    markPath(b,start)
    return b[end[0]][end[1]] if b[end[0]][end[1]]<maxint else None
    

maze = [['f', 'f', 'f', 'f'],
       ['t', 't', 'f', 't'],
       ['f', 'f', 'f', 'f'],
       ['f', 'f', 'f', 'f']]

assert minMazePath(maze,(3,0),(0,0))==7
