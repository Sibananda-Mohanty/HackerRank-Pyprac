size_set = int(input())
set_A = set(map(int, input().split()))
N = int(input())
for _ in range(N):
    operation, length = input().split()
    set_B = set(map(int, input().split()))
    exec(f"set_A.{operation}({set_B})")

print(sum(set_A))