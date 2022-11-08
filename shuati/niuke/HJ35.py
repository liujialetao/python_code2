n = '4'#input()
n = int(n)
a = [[0]*n for i in range(n)]

i, j = 0, 0
k = 0
count = 1
while True:
    a[i][j] = count
    if i==0 and j!=n-1:
        i = j+1
        j = 0
    else:
        j += 1
        i -= 1
    count += 1
    if i==0 and j==n-1:
        break
a[i][j] = count
print(a)