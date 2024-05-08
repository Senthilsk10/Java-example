n = int(input("Enter number of processes: "))
d = dict()
avg_TAT = 0
avg_WT = 0

# Input burst times for each process
for i in range(n):
    key = "P" + str(i + 1)
    b = int(input("Enter burst time of process " + str(i + 1) + ": "))
    a = b  # Storing original burst time for later use
    l = [a, b]  # List to store original burst time and burst time
    d[key] = l

# Sorting processes based on burst time
d = sorted(d.items(), key=lambda item: item[1][0])

CT = []
TAT = []
WT = []

# Calculating completion time, turnaround time, and waiting time
for i in range(len(d)):
    if i == 0:
        CT.append(d[i][1][1])
        TAT.append(d[i][1][0])
        WT.append(TAT[i] - d[i][1][1])
    else:
        CT.append(CT[i - 1] + d[i][1][1])
        TAT.append(CT[i])
        WT.append(TAT[i] - d[i][1][1])

avg_TAT = sum(TAT) / n
avg_WT = sum(WT) / n

# Printing process details and average times
print("Process\t| Burst Time | Closing Time | Turnaround Time | Waiting Time |")
for i in range(n):
    print(d[i][0], "\t|", "\t", d[i][1][1], "\t|", CT[i], "\t |", TAT[i], "\t |", WT[i], "\t |")

print("Average Waiting Time:", avg_WT)
print("Average Turnaround Time:", avg_TAT)
