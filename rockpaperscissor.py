import random

l = ["rock","scissor","paper"]

# rock vs paper = paper wins
# rock vs scissor = rock wins
# scissor vs paper = scissor wins


while True:

    ccount = 0
    ucount = 0

    uc = int(input('''
    
    Game Start.....
    1 Yes
    2 No | Exit
    
    '''))

    if uc==1:
        for a in range(1,6):
            userInput= int(input('''
            
            1 Rock
            2 Scissor
            3 Paper
            
            '''))

            if userInput==1:
                uchoice = "rock"
            elif userInput==2:
                uchoice = "scissor"
            elif userInput==3:
                uchoice = "paper"
            
            Cchoice = random.choice(l)
            if Cchoice==uchoice:
                print("Computer Value",Cchoice)
                print("User Value",uchoice)
                print("Game Draw")
                ucount = ucount+1
                ccount = ccount+1 
            elif (uchoice=="rock" and Cchoice=="scissor") or (uchoice=="paper" and Cchoice=="rock") or (uchoice=="scissor" and Cchoice=="paper"):
                print("Computer Value",Cchoice)
                print("User Value",uchoice)
                print("You Win")
                ucount = ucount+1
            else:
                print("Computer Value",Cchoice)
                print("User Value",uchoice)
                print("Computer Wins")
                ccount = ccount+1

        if ucount==ccount:
            print("Series Draw.....")
            print("User Score",ucount)
            print("Computer Score",ccount)

        elif ucount > ccount:
            print("You Win The Series.........")
            print("User Score",ucount)
            print("Computer Score",ccount)
        else:
            print("Computer Win The Series")
            print("User Score",ucount)
            print("Computer Score",ccount)

    else:
        break
