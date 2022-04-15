# URL https://paiza.jp/works/mondai/stdout_primer/stdout_primer__variable_array_step2
N, M = [int(i) for i in input().split()]
for i in range(1, N):
    print(i, end=' ')
print(N)

for i in range(1, M):
    print(i, end=' ')
print(M)