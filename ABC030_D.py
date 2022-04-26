import io
import sys

_INPUT = """\
6
6 4
5
2 3 1 2 6 5
4 1
100000000000000000000
2 3 4 1
8 1
1
2 3 4 5 3 2 4 5
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,a=map(int,input().split())
  a-=1
  k=int(input())
  B=list(map(int,input().split()))
  B=[B[i]-1 for i in range(N)]
  used=set()
  kk=a
  while kk not in used:
    used.add(kk)
    kk=B[kk]
  kk2=B[kk]
  cycle=[kk]
  while kk2!=kk:
    cycle.append(kk2)
    kk2=B[kk2]
  kk=a
  line=[]
  used=set(cycle)
  while kk not in used:
    line.append(kk)
    kk=B[kk]
  if k<len(line):
    print(line[k]+1)
  else:
    print(cycle[(k-len(line))%len(cycle)]+1)