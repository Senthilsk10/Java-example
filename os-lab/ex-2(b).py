disks = list(map(int,input().split()))
t = 0
s = int(input("enter the head"))
t+=s
t+=max(disks)

print("total ead move ment", t)