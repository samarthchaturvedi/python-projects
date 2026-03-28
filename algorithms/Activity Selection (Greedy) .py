# Activity selection problem

n = int(input("Enter number of activities: "))

activities = []

for i in range(n):
    start = int(input("Start time: "))
    end = int(input("End time: "))
    activities.append((start, end))

# sort by end time
activities.sort(key=lambda x: x[1])

selected = []
last_end = -1

for act in activities:
    if act[0] >= last_end:
        selected.append(act)
        last_end = act[1]

print("Selected activities:", selected)