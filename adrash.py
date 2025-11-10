# Priority Scheduling (non-preemptive) with arrival times
arr = [1, 2, 3, 4, 5]
burst = [4, 7, 1, 5, 3]
prio = [8, 7, 1, 4, 3]

# Build (arrival, burst, priority, pid) and sort by arrival then priority
procs = sorted([(arr[i], burst[i], prio[i], i+1) for i in range(len(arr))],
               key=lambda x: (x[0], x[2]))

time = 0
rows = []
wt_sum = tat_sum = 0

for at, bt, p, pid in procs:
    start = max(time, at)        # wait if CPU is idle
    comp  = start + bt
    wt    = start - at
    tat   = comp - at
    rows.append((pid, start, comp, tat, wt))
    wt_sum += wt; tat_sum += tat
    time = comp

print("Process\tStart\tComplete\tTAT\tWT")
for pid, s, c, tat, wt in rows:
    print(f"P{pid}\t{s}\t{c}\t\t{tat}\t{wt}")

n = len(procs)
print("\nAverage WT :", wt_sum / n)
print("Average TAT:", tat_sum / n)
