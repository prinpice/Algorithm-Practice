import sys
sys.stdin = open("아이스크림.txt", "r")

N, M = map(int,input().split())

worse = {}
for _ in range(M):
   i , ii = map(int,input().split())
   if i not in worse: worse[i] = [ii]
   else: worse[i].append(ii)
   if ii not in worse: worse[ii] = [i]
   else: worse[ii].append(i)
print('worse',worse)

# --------------------------------------------------
combi = 0
def choice(selected, ino, cnt):
   global combi
   # print(selected,ino)
   # for a in range(N):
   #     # print(a)
   #     if selected[a] == 1 and ino in worse[a]:
   #         print(a, ino,worse[a])
   #         break
   if cnt == 3:
       print(selected)
       combi += 1
       return
   else:
       print("no", selected)
       for s in range(ino,N+1):
           if selected[s] == 0:
               temp = 1
               for te in range(len(selected)):
                   if selected[te] == 1:
                       if s in worse[te]:
                           temp = 0
                           break
               if temp == 1:
                   selected[s] = 1
                   choice(selected,s,cnt+1)
                   selected[s] = 0

choice([0]*(N+1),1,0)
print(combi)