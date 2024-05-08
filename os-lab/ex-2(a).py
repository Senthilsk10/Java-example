disks = list(map(int,input().split()))
t = 0
s = int(input("enter the head"))
for i in range(len(disks)):
    if i == 0:
        t+=abs(s-disks[i])
    else:
        t+=abs(disks[i-1]-disks[i])
        
print("total ead move ment", t)