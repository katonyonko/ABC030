import io
import sys

_INPUT = """\
6
15 0
3 17
0 0
6 0
23 59
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  n,m=map(int,input().split())
  s,l=30*n+0.5*m,6*m
  x=(s-l)%360
  print(min(x,360-x))