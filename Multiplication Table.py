n, x = map(int, input().split())
k = 0
k = 0
for i in range(1,n+1):
    z = x/i
    if x%i==0 and x//i<=n:
        k+=1
print(k)



# n, x = map(int, input().split())
# k = 0
# k = 0
# for i in range(1,n+1):
#     z = x/i
#     if z==int(z) and z<=n:
#         k+=1
# print(k)
