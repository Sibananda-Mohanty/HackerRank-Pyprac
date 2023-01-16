if __name__ == '__main__':
    i = input()
    
    res = [False, False, False, False, False]
    
    for s in i:
        
        if s.isalnum(): res[0] = True 
        
        if s.isalpha(): res[1] = True
        
        if s.isdigit(): res[2] = True
        
        if s.islower(): res[3] = True
        
        if s.isupper(): res[4] = True

    
    for i in res:
        print(i)