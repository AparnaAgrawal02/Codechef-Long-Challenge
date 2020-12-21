"""A permutation p1,p2...pN of {1,2,...,N} is beautiful if pi&pi+1 is greater than 0 for every 1≤i<N . You are given an integer N, and your task is toconstruct a beautiful permutation of length N or determine that it's impossible.

Note that a&b denotes the bitwise AND of a and b.

Input:
First line will contain T, number of testcases. Then the testcases follow. Each testcase contains a single line of input, an integer N.

Output:
For each test case output −1 if there is no suitable permutation of length N, otherwise output N integers in a single line which form a beautiful permutation. If there are multiple answers output any of them.

Constraints
1≤N≤105
The sum of N over all test cases does not exceed 106
Subtasks
50 points : 1≤N,T≤9
50 points : Original constraints
Sample Input:
3
4
3
5
Sample Output:
-1
1 3 2
2 3 1 5 4
"""
import sys
input = sys.stdin.readline

############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))


t=inp()
for i in range(t):
    n=inp()
    x=n
    while(x%2==0):
        x=x//2
    if n==1:
        print(1)
        continue
    elif x==1:
        print(-1)
        continue
    else:
        d=[2,3,1]
        r=4
        while(r<=n):
            x=r
            while (x % 2 == 0):
                x = x // 2
            if x==1:
                d.append(r+1)
                d.append(r)
                r+=2
            else:
                d.append(r)
                r+=1
        print(*d)






