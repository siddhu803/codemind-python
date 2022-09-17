n=int(input())
s=0
while n>9:
    for i in str(n):
        s+=int(i)
    n=s
    s=0
print(n)
    