import random
l=["Rock","Scissor","Paper"]
while True:
    Ccount=0
    Ucount=0
    uc=int(input('''
Game start....
1 Yes
2 No|Exit
'''))
    if uc==1:
        for a in range(1,6):
            ui=int(input('''
1 Rock
2 Scissor
3 Paper
'''))
            if ui==1:
                         
                         uc="Rock"
            elif ui==2:
                uc="Scissor"
            elif ui==3:
                uc="Paper"
            Cc=random.choice(l)
            if(Cc==ui):
                print("Computer value",Cc)
                print("User value:",uc)
                print("Game Draw")
                Ucount=Ucount+1
                Ccount=Ccount+1
            elif (uc=="Rock" and Cc=="Scissor") or (uc=="Paper" and Cc=="Rock") or (uc=="Scissor" and Cc=="Paper"):
                print("Computer Choice",Cc)
                print("User choice:",uc)
                print("Your Win")
                Ucount=Ucount+1
            else:
                print("Computer Choice",Cc)
                print("User choice:",uc)
                print("Computer Win")
                Ccount=Ccount+1
        if Ucount==Ccount:
            print("Final Gamme Draw...")
            print("User Score",Ucount)
            print("Computer Count",Ccount)
        elif Ucount>Ccount:
            print("Final you win  Draw...")
            print("User Score",Ucount)
            print("Computer  score",Ccount)
        else:
            print("Final Win Computer Draw...")
            print("User Score",Ucount)
            print("Computer  Score",Ccount)

                
                

    else:
        break
