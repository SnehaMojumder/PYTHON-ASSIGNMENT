def main():
    n=int(input())
    magic=[int(input()) for _ in range(n)]
    dist = [int(input()) for _ in range(n)]
    result=optimalPoint(n,magic,dist)
    print(result)
def optimalPoint(magic,dist):
    n=len(magic)
    for i in range(n):
        remaining_magic=0
        for j in range(n):
            k=(i+j)%n
            remaining_magic+=magic[k]-dist[k]
            if remaining_magic<0:
                break
        else:
            return 1
    return -1