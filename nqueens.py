import numpy as np

def chk_cross(pos):
    l=list(board[pos[0]])
    newb=list(board.transpose()[pos[1]])
    if l.count(2)>=1:
        # print("unsafe,same row")
        return False
                
    elif newb.count(2)>=1:
        # print("unsafe,same col")
        return False
    else:
        return True

def diag(pos,n):
    x,y=pos[0],pos[1]
    while(x>0 and y>0): #top left
        x=x-1
        y=y-1
        if board[x][y]==2:
            # print("unsafe top left")
            return False
    x,y=pos[0],pos[1]
    while(x<n and y<n): #bottom left
        x=x+1
        y=y+1
        if board[x][y]==2:
            # print("unsafe bottom right")
            return False
    x,y=pos[0],pos[1]
    while(x>0 and y<n): #top right
        x=x-1
        y=y+1
        if board[x][y]==2:
            # print("unsafe top left")
            return False
    x,y=pos[0],pos[1]
    while(x<n and y>0): # bottom right
        x=x+1
        y=y-1
        if board[x][y]==2:
            # print("unsafe bottom right")
            return False
    return True
def solve(i,n):
    if i>n-1:
        print(board)
        print("done")
        return 
    for x in range(n):
        if chk_cross([i,x]) and diag([i,x],n-1):
            board[i][x]=2
            solve(i+1,n)
            board[i][x]=0
  
  
    return 
dim =int(input("enter dimensions"))
board=np.array([[n*0 for n in range(dim)]]*dim)
solve(0,dim)
