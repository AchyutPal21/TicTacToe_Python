bag=[1, 2, 3, 4, 5, 6, 7, 8, 9]

# blank_list.pop(0)
# i=5
# blank_list.insert(i, "1")
# print(blank_list)

print()
print("-: Welcome To the Tic-Tac-Toe Game :-")
print("\n")

#   Tic Tac Toe Presentation
print("  ", bag[0],"  |  ",bag[1],"  |  ",bag[2],"   ")
print("-------|-------|-------")
print("  ", bag[3],"  |  ",bag[4],"  |  ",bag[5],"   ")
print("-------|-------|-------")
print("  ", bag[6],"  |  ",bag[7],"  |  ",bag[8],"   ")





def vertical_check(v, vcheck):
    if(v[0]==vcheck and v[3]==vcheck and v[6]==vcheck):
        return 1    
    if(v[1]==vcheck and v[4]==vcheck and v[7]==vcheck):
        return 1
    if(v[2]==vcheck and v[5]==vcheck and v[8]==vcheck):
        return 1

        

def horizontal_check(h, hcheck):
    if(h[0]==hcheck and h[1]==hcheck and h[2]==hcheck):
        return 1    
    if(h[3]==hcheck and h[4]==hcheck and h[5]==hcheck):
        return 1
    if(h[6]==hcheck and h[7]==hcheck and h[8]==hcheck):
        return 1

def digonal_check(c, ccheck):
    if(c[0]==ccheck and c[4]==ccheck and c[8]==ccheck):
        return 1
    if(c[2]==ccheck and c[4]==ccheck and c[6]==ccheck):
        return 1
        


print("Choose Your Option (X / O): ")

player1=input("Player1 choice: ").upper()
player2=input("Player2 choice: ").upper()


for i in range(1, 10):
    if(i%2!=0):
        print("Player1 Choose Your Place:")
        player1choice=int(input())
        bag.pop(player1choice-1)
        bag.insert(player1choice-1, player1)
        
        # Calling the function
        vres=vertical_check(bag, player1)
        hres=horizontal_check(bag, player1)
        dres=digonal_check(bag, player1)

        print("  ", bag[0],"  |  ",bag[1],"  |  ",bag[2],"   ")
        print("-------|-------|-------")
        print("  ", bag[3],"  |  ",bag[4],"  |  ",bag[5],"   ")
        print("-------|-------|-------")
        print("  ", bag[6],"  |  ",bag[7],"  |  ",bag[8],"   ")

        if(vres==1 or hres==1 or dres==1):
            print("Player1-",player1,"\nWINNER WINNER Tic Tac Toe WINNER!!!")
            break

    if(i%2==0):
        print("Player2 Choose Your Place:")
        player2choice=int(input())
        bag.pop(player2choice-1)
        bag.insert(player2choice-1, player2)
        
        # Calling the function
        vres=vertical_check(bag, player2)
        hres=horizontal_check(bag, player2)
        dres=digonal_check(bag, player2)

        print("  ", bag[0],"  |  ",bag[1],"  |  ",bag[2],"   ")
        print("-------|-------|-------")
        print("  ", bag[3],"  |  ",bag[4],"  |  ",bag[5],"   ")
        print("-------|-------|-------")
        print("  ", bag[6],"  |  ",bag[7],"  |  ",bag[8],"   ")

        if(vars==1 or hres==1 or dres==1):
            print("Player2-",player2,"\nWINNER WINNER Tic Tac Toe WINNER!!!")
            break


    if(i==9):
        print("GAME DRAW!!!")






