# T = int(input())

# for t in range(T):
#     N, M = map(int, input().split())
#     natural_list = list(map(int, input().split()))

#     for m in range(M):
#         natural_list = natural_list[::-1]
#         temp = natural_list.pop()
#         natural_list = natural_list[::-1]
#         natural_list.append(temp)
#     print(f'#{t+1} {natural_list[0]}')


def enQueue(item):
    global rear
    if isFull():
        print("Queue_Full")
    else:
        rear = rear + 1
        Q[rear] = item

def deQueue():
    global front
    if isEmpty():
        print("Queue_Empty")
    else:
        front += 1
        return Q[front]

def isEmpty():
    return front == rear

def isFull():
    return rear == len(Q)-1

T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    Q = list(map(int, input().split()))
    front = -1
    rear = N-1
    for _ in range(M):
        enQueue(deQueue())
    result = deQueue()
    print(result)
