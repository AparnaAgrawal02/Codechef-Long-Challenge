""" ADA KING"""


"""Chef Ada is training her calculation skills. She wants to place a king and some obstacles on a chessboard in such a way that the number of distinct cells the king can reach is exactly K.

Recall that a chessboard has 8 rows (numbered 1 through 8) and 8 columns (numbered 1 through 8); let's denote a cell in row r and column c by (r,c).

In one move, a king can move to any adjacent cell which shares a side or corner with its current cell and does not contain an obstacle. More formally, a king in a cell (r,c) can move to any cell (rn,cn) if (rn,cn) is a valid cell of the chessboard which does not contain an obstacle and (r−rn)2+(c−cn)2≤2.

A cell (x,y) can be reached by a king if, after an arbitrary number of moves (including zero), the king is in the cell (x,y).

Help Ada find any valid configuration of the board such that the king can reach exactly K distinct cells. It is guaranteed that such a configuration always exists. If there are multiple solutions, you may find any one.

Input
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first and only line of each test case contains a single integer K.
Output
For each test case, print 8 lines describing a chessboard, each containing 8 characters. For each valid i and j, the j-th character on the i-th line should be one of the following:

'O' if the cell (i,j) initially contains the king; there should be exactly one such cell
'X' if the cell (i,j) contains an obstacle
'.' if the cell (i,j) is empty
Constraints
1≤T≤64
1≤K≤64
Subtasks
Subtask #1 (10 points): K≤8
Subtask #2 (90 points): original constraints

Example Input
4
1
5
9
64
Example Output
........
........
........
.XXX....
.XOX....
.XXX....
........
........

........
........
........
........
........
XXX.....
..XX....
O..X....

........
.XXXXXXX
.X.O...X
.X...XXX
.XXX.X..
...XXX..
........
........

........
........
........
...O....
........
........
........
........
Explanation
The descriptions of the chessboard for each test case are separated by blank lines for clarity. Note that these lines should not appear on the output of your submission.

Example case 1: The king is surrounded by obstacles, so it cannot move ― the only cell it can reach is its initial cell.

Example case 4: The king can visit all cells of the board."""






# cook your dish here
tests=int(input())
for _ in range(tests):
    n=int(input())
    ch=0
    mor=0
    
    for _ in range(n):
        a1,b1=map(str,input().split())
        pa1=0
        pb1=0
        for i in a1:
            pa1+=int(i)
        for i in b1:
            pb1+=int(i)
        a1=pa1
        b1=pb1
    
        if a1>b1:
            ch+=1
        elif a1==b1:
            ch+=1
            mor+=1
        else:
            mor+=1
    if ch>mor:
        print(0,ch)
    elif ch==mor:
        print(2,ch)
    else :
        print(1,mor)


