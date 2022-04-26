import io
import sys

_INPUT = """\
6
5 2 6 3
100 80 100 73
66 30 55 25
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  A,B,C,D=map(int,input().split())
  if A*D<B*C: print('TAKAHASHI')
  elif A*D>B*C: print('AOKI')
  else: print('DRAW')