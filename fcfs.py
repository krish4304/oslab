n = int(input("Enter the number of processes: "))
p = []
for i in range(n):
    at = int(input("Enter the arrival time of process " + str(i + 1) + ": "))
    bt = int(input("Enter the burst time of process " + str(i + 1) + ": "))
    p.append([at, bt])

p.sort(key=lambda x: x[0])

et = []
for i in range(len(p)):
    if i == 0:
        et.append(p[i][1])
    else:
        et.append(et[i - 1] + p[i][1])

tat = []
for i in range(len(p)):
    tat.append(et[i] - p[i][0])

wt = []
for i in range(len(p)):
    wt.append(tat[i] - p[i][1])
print("Average Waiting Time: ",sum(wt) / n)
