# URL https://paiza.jp/works/mondai/stdout_primer/stdout_primer__specific_split_step4
l = [i for i in input().split()]
c = 0
for i in l:
    if c == 9:
        print(i)
    else:
        print(i, end=',')
    c += 1