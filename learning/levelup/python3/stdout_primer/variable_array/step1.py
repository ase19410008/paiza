# URL https://paiza.jp/works/mondai/stdout_primer/stdout_primer__variable_array_step1
N = int(input())
stt, stp = 1, N // 2
for i in range(2):
    for j in range(stt, stp):
        print(j, end=' ')
    print(stp)
    stt = N // 2 + 1
    stp = N