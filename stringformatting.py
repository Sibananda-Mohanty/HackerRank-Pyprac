def print_formatted(number):
    # your code goes here
    d=number
    bin_d = len(bin(d)[2:])
    for x in range(1,d+1):
        print(repr(x).rjust(bin_d), oct(x)[2:].rjust(bin_d) , hex(x).upper()[2:].rjust(bin_d) , bin(x)[2:].rjust(bin_d))
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)