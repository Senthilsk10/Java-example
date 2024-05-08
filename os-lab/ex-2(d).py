def near(l,n):
    ne = []
    for i in range(len(l)):
        ne.append(abs(i-l[i]))
        
    return l[ne.index(min(ne))]

dq = list(map(int,input().split()))
t = 0
s = int(input("enter the head"))
ll = [s]
for i in range(len(dq)):
    v = near(dq,ll[-1])
    dq.remove(v)
    ll.append(v)
    t+=abs(ll[-1]-ll[-2])
    
print("total head moments",t)
    