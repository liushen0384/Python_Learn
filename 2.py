import collections

n = int(input())
m = int(input())

items = [0 for i in range(n)]

dictretions = collections.defaultdict(list)
for i in range(m):
    up, down, time = [*map(int, input().split())]
    dictretions[up].append((down, time))

start = int(input())

times = 0
items[start - 1] = 1

queue = collections.deque()
queue.append(start)

while queue:
     s = queue.popleft()
     if dictretions[s]:
        for i in dictretions[s]:
            queue.append(i[0])
            items[i[0] - 1] = 1
            times += i[1]

if 0 in items:
    print(-1)
else:
    print(times)