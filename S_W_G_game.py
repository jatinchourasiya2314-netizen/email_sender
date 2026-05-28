import random 
while True:
    computer = random.choice([0,-1,1])
    youstr = input("enter your choice: ")
    youdict = {"s":1, "w":-1, "g":0}
    reversedict = {1:"snake",-1:"weter",0:"gan"}
    

    you = youdict[youstr]
    print(f"you chose {reversedict[you]} \n computer chose {reversedict[computer]}")

    if(computer == you):
        print("Its a draw")
    else:
        if(computer ==-1 and you ==1):
            print("you win!")
        elif(computer ==1 and you ==-1):
            print("you lose!")
        elif(computer ==1 and you ==0):
            print("you win!")
        elif(computer ==0 and you ==1):
            print("you lose!")
        elif(computer ==-1 and you ==0):
            print("you lose!")
        elif(computer ==0 and you ==-1):
            print("you win!")
