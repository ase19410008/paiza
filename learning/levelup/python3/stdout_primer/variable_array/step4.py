# URL https://paiza.jp/works/mondai/stdout_primer/stdout_primer__variable_array_step4
N = int(input()) + 1
M = [int(i) for i in input().split()]
for i in range(1, N):
    for j in range(1, M[i - 1]):
        print(j, end=' ')
    print(M[i - 1])