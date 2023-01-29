import random

def getResult(user, comp):
    if(abs(21 - sum(user)) < abs(21 - sum(comp))):
        print("\n-------You Won-------\n")
    else:
        print("\n-------Computer won-------\n")

def choiceAdd(user, comp):
    user.append(random.choice(list))
    comp.append(random.choice(list))
    print(f"\nYour Cards : {user}")
    print(f"\nComputer's First Card : {comp}")
    getResult(user, comp)

def getScore(user, comp):
    userTotal = sum(user)
    compTotal = sum(comp)
    print(f"\nYour Cards : {user}")
    print(f"\nComputer's First Card : {comp}")
    if(userTotal < 17):
        user.append(random.choice(list))
        getScore(user, comp)

    elif(compTotal < 17):
        comp.append(random.choice(list))
        getScore(user, comp)

    else:
        if(sum(user) >= 21):
            getResult(user, comp)
        elif(sum(comp) >= 21):
            getResult(user, comp)
        else:
            choice = input("Type 'y' to get another card, type 'n' to pass : ")
            if(choice == 'y'):
                choiceAdd(user, comp)
            else:
                getResult()

list = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10 ,10 ,10]
user = []
comp = []
print("\n---------Welcome To The Black Jack Game ----------\n")

choice = input("Do you want to play a game(type y for yes and n for no) : ");

if choice == 'y':

    user.append(random.choice(list))
    user.append(random.choice(list))
    comp.append(random.choice(list))
    comp.append(random.choice(list))

    print(f"Your Cards : {user}")
    print(f"Computer's First Card : {comp}")
    
    choice = input("Type 'y' to get another card, type 'n' to pass : ")

    
    getScore(user, comp)

    

# while(user < 21 or comp < 21):