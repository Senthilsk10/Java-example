dq=list(map(int,input("disk queue:").split()))
s=int(input("HEADER POINTER:"))
t=0
dq.sort()
t+=s
t+=max(dq)
print(f"Total Head movements:{t}")