queue = []

index = 0
while index < 5:
    queue.append(input("Enter your input: "))
    index += 1

print('Initial queue')
print(queue)

print('\nElements dequeued from queue')
while len(queue) > 0:
    queue.pop(0)

print('\nElements after removing elements')
print(queue)