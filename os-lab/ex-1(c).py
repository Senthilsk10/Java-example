total_time_counted = 0
total_time = 0
proc= []
waiting_time =0
tat =0
n = int(input("enter the number of process"))

for i in range(n):
    print("enter the process arrival and burst time")
    
    input_info = list(map(int,input().split()))
    arrival,burst,remaining = input_info[0],input_info[1],input_info[1]
    proc.append([arrival,burst,remaining,0])
    total_time+=burst
    
print(total_time)
    
time_quantam = int(input("enter a time quantum"))
while(total_time != 0):
    for i in range(n):
        if proc[i][2]<=time_quantam or proc[i][2]>=0:
            total_time_counted += proc[i][2]
            total_time -= proc[i][2]
            proc[i][2] = 0
        elif proc[i][2]>0:
            proc[i][2]-=time_quantam
            total_time -= time_quantam
            total_time_counted += total_time
        if proc[i][2]==0 and proc[i][3] != 1:
            waiting_time += total_time_counted - proc[i][0] - proc[i][1]
            tat += total_time_counted - proc[i][0]
            proc[i][3] = 1
         
#print(waiting_time,tat)

print("avg waiting time " , waiting_time/n)
print("avg turnaround time " , tat/n)