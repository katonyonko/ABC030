import io
import sys

_INPUT = """\
6
3 4
2 3
1 5 7
3 8 12 13
1 1
1 1
1
1
6 7
5 3
1 7 12 19 20 26
4 9 15 23 24 31 33
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from bisect import bisect_left
  N,M=map(int,input().split())
  X,Y=map(int,input().split())
  T=[X,Y]
  A=list(map(int,input().split()))
  B=list(map(int,input().split()))
  M=[A,B]
  ans=0
  now=0
  a=0
  while now<=M[a][-1]:
    idx=bisect_left(M[a],now)
    now=M[a][idx]+T[a]
    a^=1
    if a==0: ans+=1
  print(ans)