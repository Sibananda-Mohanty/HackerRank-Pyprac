import re
def minion_game(string):
    # your code goes here
    Kevin=0
    index=0
    regex="^[AEIOU]"
    slen=len(string)
    for i in string :
        if bool(re.match(regex,i)):
            Kevin=Kevin+ (slen-index)
        index=index+1                    
    Stuart= (((slen)*(slen+1))/2)  - Kevin
    if Stuart<Kevin:
        print("Kevin " + str(int(Kevin)))
    elif Stuart >  Kevin :
        print("Stuart " + str(int(Stuart))) 
    else:
        print("Draw") 

if __name__ == '__main__':
    s = input()
    minion_game(s)