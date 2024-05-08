from operator import add

n = int(input("no of process:"))
m = int(input("no .of resources:"))

alloc = []
print("allocated resources:")
for _ in range(n):
    a = map(int, input().split())
    alloc.append(list(a))

max_req = []
print("maximum resources required")
for _ in range(n):
    b = map(int, input().split())
    max_req.append(list(b))

avail = list(map(int, input("available resources: ").split()))

need = [[max_req[i][j] - alloc[i][j] for j in range(m)] for i in range(n)]

final = []
c = n
while c != 0:
    found = False
    for i in range(n):
        if all(need[i][j] <= avail[j] for j in range(m)):
            avail = list(map(add, avail, alloc[i]))
            need[i] = [999] * m
            final.append(i)
            c -= 1
            found = True
            break
    if not found:
        break

if len(final) == n:
    print("SAFE Sequence:")
    print("P" + " -> P".join(str(p) for p in final))
else:
    print("NO SAFE Sequence:")
