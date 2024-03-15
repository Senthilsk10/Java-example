def priority_scheduling(processes):
    # Sort the processes based on priority (the first element in each list)
    processes.sort(key=lambda x: x[0])

    n = len(processes)
    waiting_times = [0] * n
    turnaround_times = [0] * n

    # Calculate waiting time and turnaround time for each process
    for i in range(1, n):
        waiting_times[i] = waiting_times[i-1] + processes[i-1][1]

    for i in range(n):
        turnaround_times[i] = waiting_times[i] + processes[i][1]

    return waiting_times, turnaround_times

def get_processes_priority():
    processes = []
    n = int(input("Enter the number of processes: "))
    
    for i in range(n):
        priority = int(input("enter the priority for process P{}: ".format(i + 1)))
        burst_time = int(input("Enter burst time for process P{}: ".format(i + 1)))
        processes.append([priority, burst_time])
    
    return processes

# Sample Data for Priority Scheduling
processes = get_processes_priority()



waiting_times, turnaround_times = priority_scheduling(processes)

print("Process\tPriority\tBurst Time\tWaiting Time\tTurnaround Time")
for i in range(len(processes)):
    print(f"P{i+1}\t\t{processes[i][0]}\t\t{processes[i][1]}\t\t{waiting_times[i]}\t\t{turnaround_times[i]}")

# Calculate average waiting time and average turnaround time
avg_waiting_time = sum(waiting_times) / len(waiting_times)
avg_turnaround_time = sum(turnaround_times) / len(turnaround_times)

print("\nAverage Waiting Time:", avg_waiting_time)
print("Average Turnaround Time:", avg_turnaround_time)