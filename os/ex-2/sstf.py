def sstf(dq, s):
    t = 0
    ll = [s]
    
    while dq:
        v = min(dq, key=lambda x: abs(x - ll[-1]))
        dq.remove(v)
        ll.append(v)
        t += abs(ll[-1] - ll[-2])
    
    print(f"Total Head Movements: {t}")

# Driver code
dq = list(map(int, input("Disk queue: ").split()))
s = int(input("Initial head position: "))
sstf(dq, s)
