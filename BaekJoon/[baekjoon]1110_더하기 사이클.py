
start = int(input())
count = 0
bef = start
end = 0
while True:
    count+=1
    end = int(str(bef%10)+str((bef//10 + bef%10)%10))
    if end == start:
        break
    else:
        bef = end

print(count)

