n = int(input("enter the number of process\n"))

d = {}
et = []
wt = []
tat = []

for i in range(n):
    p = f"P{i+1}"
    a = int(input(f"enter the arrival time for {p}"))
    b = int(input(f"enter the exit time for {p}"))
    l = [a,b]
    d[p] = l

d = sorted(d.items(),key=lambda item:item[1][0])
#print(d)
for i in range(len(d)):
    if i==0:
        et.append(d[i][1][1])
        
    else:
        et.append(et[i-1]+d[i][1][1])
 
for i in range(len(d)):    
    tat.append(et[i]-d[i][1][0])
    
for i in range(len(d)):
    wt.append(tat[i]-d[i][1][1])
        
        
wt_avg = sum(wt)/len(wt)
print("Process | Arrival | Burst | Exit | Turn Around | Wait |")
for i in range(len(d)):
    print(f"{d[i][0]}\t{d[i][1][0]}\t{d[i][1][1]}\t{et[i]}\t{tat[i]}\t{wt[i]}")

#print(et)
#print(wt)
#print(tat)