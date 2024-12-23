import random

def game():
    prv = []
    print("You are playing the game..")
    score = random.randint(1,64)
    # fetch the hiscore

    with open("File - PS/hiscore.txt") as f:
        hiscore = f.read()
        if(hiscore!=""):
            hiscore = int(hiscore)
        else:
            hiscore =0
    
    print(f"Your score: {score}")
    if(score>hiscore):
        #write this hiscore to the file
        with open("File - PS/hiscore.txt","w") as f:
            f.write(str(score))
    return score
game()