def sum(a,b,c):
    return a+b+c

def printBorad(xstate,zstate):
    zero = 'x'if xstate[0] else('O' if zstate[0] else 0 )
    one = 'x'if xstate[1] else('O' if zstate[1] else 1)
    two = 'x'if xstate[2] else('O' if zstate[2] else 2)
    three = 'x'if xstate[3] else('O' if zstate[3] else 3)
    four = 'x'if xstate[4] else('O' if zstate[4] else 4)    
    five = 'x'if xstate[5] else('O' if zstate[5] else 5)
    six = 'x'if xstate[6] else('O' if zstate[6] else 6)
    seven = 'x'if xstate[7] else('O' if zstate[7] else 7)
    eight ='x'if xstate[8] else('O' if zstate[8] else 8)
    print(f"\t{zero} | {one} | {two}")
    print(f"\t--|---|-- ")
    print(f"\t{three } | {four} | {five}")
    print(f"\t--|---|--")
    print(f"\t{six} | {seven} | {eight}")
    
    
def checkWIn(xstate,zstate,x,y): 
    wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in wins:
        if(sum(xstate[win[0]], xstate[win[1]],xstate[win[2]]) == 3 ):
            print(x," Won the match \n")
            return 1
        if( sum(zstate[win[0]], zstate[win[1]],zstate[win[2]]) == 3):
            print(y,"y Won the match \n")
            return 0
    return -1       
    
zstate=[0,0,0,0,0,0,0,0,0]
xstate=[0,0,0,0,0,0,0,0,0]
print("\n                     *** Welocome to Tic Tac Toe *** \n")

x=input('Enter the first player(x) : ')
y=input('Enter the second player(O) : ')
x=x.upper()
y=y.upper()
print('')
turn = 1
k=1
while(True):
    printBorad(xstate,zstate)
    if(k==10):
        print(' \n ***Match over*** \n')
        break;
    k+=1
    if(turn==1):
        print('\n',x,"'s Chance (x)")
        value=int (input("Please enter a value : "))
        print()
        xstate[value]=1
    else:
        print('\n',y,"'s Chance (O)")
        value=int (input("Please enter a value : "))
        print()
        zstate[value]=1
        
    cwin = checkWIn(xstate,zstate,x,y)
    if(cwin !=-1):
        print("' \n ***Match over*** \n")
        break
    
    

    turn = 1 - turn 
    
