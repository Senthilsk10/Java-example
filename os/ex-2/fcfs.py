disk_queue=list(map(int,input("disk queue:").split()))
s=int(input("HEADER POINTER:"))
t=0
for i in range(len(disk_queue)):
    if i==0:
        t=abs(s-disk_queue[i])
    else:
        t+=abs(disk_queue[i-1]-disk_queue[i])
print(f"Total Head Movements:{t}")
