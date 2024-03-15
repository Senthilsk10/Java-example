def sjf(processes):
    print("SHORTEST JOB FIRST SCHEDULING")
    n = len(processes)
    
    CT = []
    TAT = []
    WT = []
    
    for i in range(n):
        if i == 0:
            CT.append(processes[i][1])
            TAT.append(processes[i][1])
            WT.append(TAT[i] - processes[i][1])
        else:
            CT.append(CT[i-1] + processes[i][1])
            TAT.append(CT[i])
            WT.append(TAT[i] - processes[i][1])
    
    avg_TAT = sum(TAT) / n
    avg_WT = sum(WT) / n
    
    # Print Table
    print("Process | Burst Time | Closing Time | Turn Around Time | Waiting Time |")
    for i in range(n):
        print("   " + str(processes[i][0]) + "    |     " + str(processes[i][1]) + "     |      " +
              str(CT[i]) + "      |       " + str(TAT[i]) + "        |      " + str(WT[i]) + "      |")
    
    print("Average Waiting Time:", avg_WT)
    print("Average Turnaround Time:", avg_TAT)


def get_processes_sjf():
    processes = []
    n = int(input("Enter the number of processes: "))
    
    for i in range(n):
        burst_time = int(input("Enter burst time for process P{}: ".format(i + 1)))
        processes.append([i + 1, burst_time])  # [Process ID, Burst Time]
    
    # Sort processes by burst time (Shortest Job First)
    processes.sort(key=lambda x: x[1])
    
    return processes


# Sample Data for SJF Scheduling
sjf_processes = get_processes_sjf()

# Call SJF Scheduling function
sjf(sjf_processes)
