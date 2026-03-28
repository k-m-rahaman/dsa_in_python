queue = []

# Enqueue
queue.append(10)
queue.append(20)
queue.append(30)
print("Queue after enqueue:", queue)

# Dequeue
queue.pop(0)
print("Queue after dequeue:", queue)

# Front (Peek)
print("Front element:", queue[0])

# Display
print("Final queue:", queue)