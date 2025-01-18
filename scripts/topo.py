from collections import deque
import queue



q = deque()
q.append(10)
q.append(11)
q.append(12)

print(q.popleft())
print(q.popleft())