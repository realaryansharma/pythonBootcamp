import random 

list = ["aryan", "arayana", "shailja", "ankush", "shashwat"]

print("\n\n-------------- Welcome to the HANGMAN GAME --------------\n\n")

word = random.choice(list)

lenOfWord = len(word)
noOfChoices = 2 * lenOfWord

print(f"\n\nYou have {noOfChoices} choices\n\n")

ans = []

for k in range(0, lenOfWord):
    ans += "-"

print(ans)

count = 0
stop  = 0

while(noOfChoices >= 0 and stop == 0):

    select = input("\nEnter any character : ")

    for i in word:
    
        if i == select:
            ans[count] = i
        count += 1

    if ans.count("-") == 0:
        stop = 1
        print("------------------------------------------")
        print("\n\nCongratualtions🥳🥳🥳, You Won!\n\n")
        print("------------------------------------------")
    else:
        count = 0
        print(f"\nNo Of Choices {noOfChoices}")
        print(f"\n{ans}")

    noOfChoices -= 1

if noOfChoices == -1:
    print("------------------------------------------")
    print("\n\nNo Chance Left\n\n")
    print("------------------------------------------")