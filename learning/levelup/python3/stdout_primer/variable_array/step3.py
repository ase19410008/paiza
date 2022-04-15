# URL https://paiza.jp/works/mondai/stdout_primer/stdout_primer__variable_array_step3
N = int(input()) + 1
for i in range(1, N):
    for j in range(1, i):
        print(j, end=' ')
    print(i)