x = input()
y = []
y = x.split(" ")
N = int(y[0])
unknown = y[1]

for i in range(1,1001):
    if 2 * i * i - 1 > N:
        m = i -1
        break
for i in range(1,m + 1):
    h = unknown*(2 * (m + 1) - 2 * i - 1)
    print(h.center(2 * m - 1," "))
for i in range(1,m):
    h = unknown*(2 * i + 1)
    print(h.center(2 * m - 1," "))
print(str(N - 2 * m * m + 1))
