# URL https://paiza.jp/works/mondai/stdout_primer/stdout_primer__variable_array_boss
N, M = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]

AB = []
stt, stp = 0, 0
for i in B:
    stp += i
    AB.append(A[stt:stp])
    stt += i
    
for i in range(M):
    for j in range(B[i] - 1):
        print(AB[i][j], end=' ')
    print(AB[i][B[i] - 1])