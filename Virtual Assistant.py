import random
import datetime
import time
import json

notes = dict()
userinfo=dict()

def set_user_profile():
    bot_name = input("I'm your virtual assistant, what do you wanna call me? ")
    print(bot_name,", I like it!")
    print("Before we start, I need to learn some things about you too")
    name = input("What's your name? ")
    userinfo["Name"]=name
    print("Cool, nice to meet you", (userinfo["Name"]))
    age = input("How old are you? ")
    userinfo["Age"]=age
    home = input("Where do you live? ")
    userinfo["Home"]=home
    hobbies = input("Do you have any hobby's? ")
    userinfo["Hobbies"]=hobbies
    game = input("What games do you play? ")
    userinfo["Game"]=game
    save_userinfo()
    print("Awesome, now I know that you're name is", (userinfo["Name"]), ", you're", (userinfo["Age"]),
          "years old, and you live in", (userinfo["Home"]), ". Your hobby is", (userinfo["Hobbies"]),
          ", and you love to play", (userinfo["Game"]))
def save_userinfo():
   with open("userinfo.json", "w") as file:
       json.dump(userinfo, file)
def update_userinfo():
    global userinfo
    with open("userinfo.json", "r") as file:
        userinfo = json.load(file)

def add_note(title, text):
    global notes
    notes[title] = text
def display_notes():
    update_notes()
    if len(notes) == 0:
        print("No notes yet")
    else:
        for title, text in notes.items():
            print(f"{title}: {text}")
def delete_note(title):
    if title in notes.keys():
        del notes[title]
        print(f'The {title} note has been deleted')
    else:
        print('The note does not exist')
def save_notes():
    with open("notes.json", "w") as file:
        json.dump(notes, file)
def update_notes():
    global notes
    with open("notes.json", "r") as file:
        notes = json.load(file)

def main_functions():
    print("0. Exit")
    print("1. Calculator")
    print("2. Multiplication tables")
    print("3. Fake News Generator")
    print("4. Date and Time")
    print("5. RPS game")
    print("6. Guess the number")
    print("7. Take a note")
    print("9. Open Settings")
def main():
    print("What will we be doing today", (userinfo["Name"]), "?")
    main_functions()

    task=int(input("Pick a task: "))
    print(" ")

    while task!=0:
#calculator
        if task==1:
            print("I will give you the sum, the difference, the product, the quotient, integer division and its remainder, and the exponent")
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            print("Sum:", num1 + num2)
            print("Difference:", num1 - num2)
            print("Product:", num1 * num2)
            print("Quotient:", num1/num2)
            print("Integer Division:", num1//num2,"and its remainder:", num1%num2)
            print("Exponent:", num1**num2)
            print(" ")
            task = int(input("What next? Pick a task: "))
#multiplications
        if task==2:
            print("1. General tables")
            print("2. Specific table")
            mode = int(input("Select a mode: "))
            if mode == 1:
                for num1 in range(1, 11):
                    for num2 in range(1, 11):
                        print(f" {num1} * {num2} = {num1 * num2}")
                    print("--------------")
            if mode == 2:
                num1 = int(input("Which multiplication table would you like? "))
                for x in range(1, 11):
                    print(f" {x} * {num1} = {x * num1}")
            print(" ")
            task = int(input("What next? Pick a task: "))
#fake news generator
        if task==3:
            print("Welcome to your personal Fake News Generator. What news shall we create today?")
            character = input("Who are we creating fake news about? ")
            fake_news = [f"{character.title()} is dead...",
                         f"Shocking discovery: {character.title()} isn't who you really think they are...",
                         f"Fans outraged as {character.title()} caught in massive scandal!",
                         f"{character.title()} spotted in public after months of disappearance!",
                         f"Internet divided over {character.title()}’s controversial statement last night!",
                         f"Fans outraged as {character.title()} announces retirement!",
                         f"You won’t believe what {character.title()} just said in a leaked video!",
                         f"The internet is furious after {character.title()}’s latest controversy!",
                         f"Heartbreaking news: {character.title()} diagnosed with a rare illness!",
                         f"Wild conspiracy theories emerge about {character.title()} – are they true?",
                         f"Shocking confession: {character.title()} admits to years of lying!"]
            chosen_news = random.randint(0, len(fake_news) - 1)
            print(fake_news[chosen_news])
            print(" ")
            task = int(input("What next? Pick a task: "))
#date/time
        if task==4:
            print("Type 'D' to find out the date or 'T' for the time")
            answer = input("I'm time_bot, how can I help? ")
            right_now = datetime.datetime.now()
            if answer == "T" or "t":
                print(f"The time right now is: {right_now.time().hour}:{right_now.time().minute}")
            if answer == "D" or "d":
                print("Today's date is:", right_now.date())
            print(" ")
            task = int(input("What next? Pick a task: "))
#rps
        if task==5:
            w = ['Rock', 'Paper', 'Scissors']
            print("Welcome to our newest game, Rock_Paper_Scissors!")
            print("Please select your weapon:")
            print(f"1.{w[0]}")
            print(f"2.{w[1]}")
            print(f"3.{w[2]}")
            rps_user = int(input("What weapon do you choose?(1-3)"))
            rps_user = w[rps_user - 1]
            time.sleep(0.5)
            print("You chose: " + rps_user, ",wish you luck!")

            bot = random.randint(1, 3)
            bot = w[bot - 1]
            time.sleep(1)
            print("Your opponent chose: " + bot)
            time.sleep(1)
            if user == bot:
                print("Draw")
                print("Better luck next time!")
            elif ((rps_user == "Rock" and bot == "Scissors") or
                  (rps_user == "Paper" and bot == "Rock") or
                  (rps_user == "Scissors" and bot == "Paper")):
                print("You won!!")
            else:
                print("You lost. Try your luck again")
            print(" ")
            task = int(input("What next? Pick a task: "))
#random number generator
        if task==6:
            print("Let's play a game! I pick a number, and you guess it")
            true_number = random.randint(1, 100)
            lives = int(input("How many lives do you want? "))
            while True:
                guess = int(input("Guess a number between 1-100: "))
                if guess > true_number:
                    lives -= 1
                    print("Go lower")
                    if lives == 1:
                        print("Last guess")
                    elif lives == 0:
                        print("The number was ", true_number)
                        break
                elif guess < true_number:
                    lives -= 1
                    print("Go Higher")
                    if lives == 1:
                        print("Last guess")
                    elif lives == 0:
                        print("The number was",true_number)
                        break
                else:
                    print("You guessed the number!!")
                    break
            print(" ")
            task = int(input("What next? Pick a task: "))
#notes
        if task==7:
            while True:
                print("1. Add a note")
                print("2. View all notes")
                print("3. Delete a note")
                print("0. Exit")
                notes_task=input("Choose an action: ")
                if notes_task == "1":
                    note_title = input("Enter a title: ")
                    note_text = input("Enter text: ")
                    add_note(note_title, note_text)
                    save_notes()
                    print(" ")
                elif notes_task == "2":
                    print(" ")
                    display_notes()
                    save_notes()
                    print(" ")
                elif notes_task == "3":
                    print(" ")
                    print("Current notes:")
                    update_notes()
                    for title in notes.keys():
                        print(title)
                    print(" ")
                    title_to_del = input('Enter the note title to delete: ')
                    delete_note(title_to_del)
                    save_notes()
                    print(" ")
                elif notes_task == "0":
                    print("Closing notes...")
                    print(" ")
                    break
                else:
                    print("Invalid input. Please try again.")
            print(" ")
            task = int(input("What next? Pick a task: "))
#settings
        if task==9:
            print("0. Exit App")
            print("1. Change name")
            print("2. Change age")
            print("3. Change home")
            print("4. Change hobbies")
            print("5. Change games played")
            settings_task=int(input("Enter a task: "))
            if settings_task==1:
                name = input("What should I call you from now on? ")
                userinfo["Name"] = name
            if settings_task==2:
                age = input("How old are you now? ")
                userinfo["Age"] = age
            if settings_task==3:
                home = input("What's your new address? ")
                userinfo["Home"] = home
            if settings_task==4:
                hobbies = input("What are your new hobbies? ")
                userinfo["Hobbies"] = hobbies
            if settings_task==5:
                game = input("What games do you play now? ")
                userinfo["Game"] = game
            if settings_task==0:
                print("Closing Settings...")
                time.sleep(random.randint(1,3))
                #print(userinfo)
                task = int(input("What next? Pick a task: "))
            save_userinfo()
            update_userinfo()

    if task==0:
        print("See you later!")

password="bot15"
user=input("Please enter your password: ")
while user!=password:
    print("Invalid, enter password again")
    print("-")
    user=input("Please enter your password: ")
else:
    print("Login successful. Welcome")
    update_userinfo()
print(" ")

intro_task=input("Welcome to your virtual assistant. Press 0 to skip intro, Press any key to proceed intro: ")
print(" ")
time.sleep(1)
if intro_task=="0":
    main()
else:
    print("Hello, wassup")
    set_user_profile()
    update_userinfo()
