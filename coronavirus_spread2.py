"""There are N athletes (numbered 1 through N) in a line. For each valid i, the i-th athlete starts at the position i and his speed is Vi, i.e. for any real number t≥0, the position of the i-th athlete at the time t is i+Vi⋅t.

Unfortunately, one of the athletes is infected with a virus at the time t=0. This virus only spreads from an infected athlete to another whenever their positions are the same at the same time. A newly infected athlete may then infect others as well.

We do not know which athlete is infected initially. However, if we wait long enough, a specific set of athletes (depending on the athlete that was infected initially) will become infected. Your task is to find the size of this set, i.e. the final number of infected people, in the best and worst possible scenario.

Input
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains a single integer N.
The second line contains N space-separated integers V1,V2,…,VN.
Output
For each test case, print a single line containing two space-separated integers ― the smallest and largest final number of infected people.

Constraints
1≤T≤104
3≤N≤5
0≤Vi≤5 for each valid i
Subtasks
Subtask #1 (1 point): N=3
Subtask #2 (99 points): original constraints

Example Input
4
3
1 2 3
3
3 2 1
3
0 0 0
3
1 3 2
Example Output
1 1
3 3
1 1
1 2
Explanation
Example case 1: No two athletes will ever have the same position, so the virus cannot spread.

Example case 2: It does not matter who is initially infected, the first athlete would always spread it to everyone.

Example case 3: The athletes are not moving, so the virus cannot spread.

Example case 4: The best possible scenario is when the initially infected athlete is the first one, since he cannot infect anyone else. In the worst possible scenario, eventually, the second and third athletes are infected."""


# cook your dish here
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
def re(arr,final,time,x,n,ss,visited):
    for i in range(n):
        if arr[i]>=time:
            final[x][i]=1
            if visited[i]!=1:
                re(ss[i],final,arr[i],x,n,ss,visited)
        visited[i]=1
        




t=inp()
for _ in range(t):
    n=inp()
    arr=inlt()
    ss=[[0 for i in range(n)]for j in range(n)]
    final=[[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        final[i][i]=1
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]-arr[j]!=0:
                time=(j-i)/(arr[i]-arr[j])
            else:
                time=0
            if time>0:
                ss[i][j]=time
                ss[j][i]=time
    for i in range(n):
        for j in range(n):
            if ss[i][j]>0:
                final[i][j]=1
                visited=[0 for i in range(n)]
                visited[i]=1
                re(ss[j],final,ss[i][j],i,n,ss,visited)
    z=[]
    for i in final:
        z.append(sum(i))
    
    print(min(z),max(z))
    


    
    


