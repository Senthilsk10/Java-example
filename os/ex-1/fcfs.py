def fcfs(processes):
    print("FIRST COME FIRST SERVE SCHEDULING")
    n = len(processes)
    
    # Calculate Exit Time, Turnaround Time, Waiting Time
    exit_time = [0] * n
    turnaround_time = [0] * n
    waiting_time = [0] * n
    
    # Calculate Exit Time for each process
    for i in range(n):
        if i == 0:
            exit_time[i] = processes[i][1]
        else:
            exit_time[i] = exit_time[i - 1] + processes[i][1]
    
    # Calculate Turnaround Time for each process
    for i in range(n):
        turnaround_time[i] = exit_time[i] - processes[i][0]
    
    # Calculate Waiting Time for each process
    for i in range(n):
        waiting_time[i] = turnaround_time[i] - processes[i][1]
    
    # Print Table
    print("Process | Arrival | Burst | Exit | Turnaround | Waiting |")
    for i in range(n):
        print("   P" + str(i + 1) + "    |    " + str(processes[i][0]) + "     |    " +
              str(processes[i][1]) + "    |   " + str(exit_time[i]) + "   |      " +
              str(turnaround_time[i]) + "     |     " + str(waiting_time[i]) + "    |")
    
    # Calculate Average Waiting Time
    avg_waiting_time = sum(waiting_time) / n
    print("Average Waiting Time:", avg_waiting_time)


def get_processes_fcfs():
    processes = []
    n = int(input("Enter the number of processes: "))
    
    for i in range(n):
        arrival_time = int(input("Enter arrival time for process P{}: ".format(i + 1)))
        burst_time = int(input("Enter burst time for process P{}: ".format(i + 1)))
        processes.append([arrival_time, burst_time])
    
    return processes

# Sample Data for FCFS Scheduling
fcfs_processes = get_processes_fcfs()
sorted_processes = sorted(fcfs_processes,key=lambda item: item[0])
# Call FCFS Scheduling function
fcfs(sorted_processes)
