def priority(priorities,burst_time):
    empty1 = []
    empty2 = []
    wt = 0
    tat = 0
    i = 0
    print("process\t burst \t wt \t tat")
    while(i<len(burst_time)):
        k = min(priorities)
        tat += burst_time[priorities.index(k)]
        print(priorities.index(k),"\t",burst_time[priorities.index(k)],"\t",wt,"\t",tat)
        empty1.append(wt)
        empty2.append(tat)
        wt+=burst_time[priorities.index(k)]
        priorities[priorities.index(k)] = max(priorities)+1
        i+=1
        #print(empty1,empty2)


n = int(input("enter the total no of process\n"))
priorities = []
burst_time = []
for i in range(n):
    priorities.append(int(input("enter the priority id")))
    
for i in range(len(priorities)):
    burst_time.append(int(input(f"enter the burst time for process {i+1}")))
    
priority(priorities,burst_time)

