cube = lambda x:pow(x, 3) # complete the lambda function 

def feb(n):
    # return a list of fibonacci numbers
    if n == 0:
        return 0
    if n <= 2:
        return 1 
    return feb(n-2) + feb(n-1)

def fibonacci(n):
    ls = [feb(i) for i in range(n)]

    return ls

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))