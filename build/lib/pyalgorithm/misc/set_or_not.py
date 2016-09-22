"""
To check whether the m'th bit in an integer is set or not
"""

def find(n,m):
    temp = 1 << (m-1)
    if ((n and temp) == 0):
      return False
    else:
      print True
