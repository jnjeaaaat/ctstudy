# 최대공약수와 최소공배수
import sys
sys.stdin = open("00.txt")

n, m = map(int,input().split())

def gcd(n, m):
    while m > 0:
        n, m = m, n%m
    return n

def lcm(n, m):
    return n*m//gcd(n,m)

print(gcd(n,m))
print(lcm(n,m))