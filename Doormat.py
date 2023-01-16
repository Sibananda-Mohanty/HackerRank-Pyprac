N, M = map(int, input().split())
result = []
for i in range(1, N + 1):
    if i == int(N / 2) + 1:
        result.append('WELCOME')
    elif i < int(N / 2) + 1:
        result.append('.|.' * (i * 2 - 1))
    else:
        result.append('.|.' * ((N + 1 - i) * 2 - 1))
print('\n'.join(list(map(lambda x: x.center(M, '-'), result))))