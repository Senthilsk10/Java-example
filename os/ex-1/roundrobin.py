def get_processes_rr():
    processes = []
    n = int(input("Enter the number of processes: "))
    
    for i in range(n):
        arrival_time = int(input("Enter arrival time for process P{}: ".format(i + 1)))
        burst_time = int(input("Enter burst time for process P{}: ".format(i + 1)))
        processes.append([arrival_time, burst_time, burst_time, 0])  # [arrival, burst, remaining, completed]
    
    return processes

total_p_no = int(input("Enter Total Process Number: "))
total_time_counted = 0
wait_time = 0
turnaround_time = 0

proc = get_processes_rr()

# Calculate total burst time of all processes
total_time = sum(proc[i][1] for i in range(total_p_no))

# Input time quantum
time_quantum = int(input("Enter time quantum: "))

while any(proc[i][2] > 0 for i in range(total_p_no)):
    for i in range(total_p_no):
        if proc[i][2] <= time_quantum and proc[i][2] > 0:
            total_time_counted += proc[i][2]
            proc[i][2] = 0
        elif proc[i][2] > 0:
            proc[i][2] -= time_quantum
            total_time_counted += time_quantum

        if proc[i][2] == 0 and proc[i][3] != 1:
            wait_time += total_time_counted - proc[i][0] - proc[i][1]
            turnaround_time += total_time_counted - proc[i][0]
            proc[i][3] = 1
            total_time -= proc[i][1]

print("\nAvg Waiting Time is ", (wait_time * 1) / total_p_no)
print("Avg Turnaround Time is ", (turnaround_time * 1) / total_p_no)
