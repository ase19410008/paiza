# URL https://paiza.jp/works/mondai/stdout_primer/stdout_primer__2dim_array_boss
N = int(input()) + 1
for i in range(1, N):
    for j in range(1, N - 1):
        print(i * j, end=' ')
    print(i * (N - 1))