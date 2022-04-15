# URL https://paiza.jp/works/mondai/stdout_primer/stdout_primer__2dim_array_step2
N = input().split()
for i in range(3):
    for j in range(2):
        print(N[i * 3 + j], end=' ')
    print(N[i * 3 + j + 1])