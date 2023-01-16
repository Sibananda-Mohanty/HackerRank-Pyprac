t= int(input())
for i in range(t):
    a,b = map(str,input().split())
    try :
        print(int(a)//int(b))
    except ZeroDivisionError as e:
        print("Error Code: integer division or modulo by zero")
    except ValueError as e:
        print("Error Code: {}".format(e))