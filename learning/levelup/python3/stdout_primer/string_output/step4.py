# URL https://paiza.jp/works/mondai/stdout_primer/stdout_primer__string_output_step4
S = []
for i in range(10):
    S.append(input())

for i in range(len(S) - 1):
    print(S[i], end=' ')
print(S[i + 1])