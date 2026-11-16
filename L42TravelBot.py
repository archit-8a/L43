import re,random
from colorama import Fore, init

#Initialize colorama (autoreset ensure each print resets after use)
init(autoreset=True)

#Destination & Joke Data
destination= {
    "Cities":["Tokyo","Paris","Mumbai"],
    "Picnic":["Park","Beaches","Indoor Court"],
    "Restaurant":["India Gate","Golden London","Mc'Donald"]
}

jokes={
    "Why don't programmers like nature? Too many bug!!"
    "Why did the computer go to the doctor? Because It Had Virus!!"
    "Why do travelers always feel warm? Because of all their hot spots!!"
}

#Helper function to normalize  user input (remove extra spaces,make lowercase)
def normalize_input(text):
    return re.sub(r"\s+"," ",text.strip().lower())

#Provide travel recommendation
def recommend():
    print(Fore.CYAN +"TravelBot: Cities,Picnic,Restaurant?")
    preference=input(Fore.BLUE +"You: ")
    preference= normalize_input(preference)

    if preference in destination:
        suggestion= random.choice(destination[preference])
        print(Fore.CYAN + f"TravelBot: How about {suggestion}?")
        print(Fore.CYAN + "TravelBot: Do you like it? (Yes/No)")
        answer=input(Fore.RED + "You: ").lower()

        if answer == "yes":
            print(Fore.LIGHTBLUE_EX + f"TravelBot: Awesome! Enjoy {suggestion}!")
        elif answer == "no":
            print(Fore.LIGHTMAGENTA_EX + "TravelBot: Let's try another.")
        else:
            print(Fore.LIGHTGREEN_EX + "TravelBot: I'll suggest again.")
    else:
        print(Fore.LIGHTBLACK_EX + "TravelBot: Sorry,I don't have that type of destination")
        recommend()

#0ffer packing tips based on user's destination and duration
def packing_tips():
    print(Fore.LIGHTRED_EX + "TravelBot: Where to?")
    location= normalize_input(input(Fore.LIGHTGREEN_EX + "You: "))
    print(Fore.CYAN +"TravelBot: How many days?")
    days= input(Fore.LIGHTBLACK_EX + "You:")

    print(Fore.GREEN +f"TravelBot: Packing Tips for {days} days in {location}")
    print(Fore.GREEN + "-> Pack versatile clothes")
    print(Fore.GREEN + "-> Bring Chargers/Adapters")
    print(Fore.GREEN + "-> Check the weather forecast")

#Tell a random joke

def tell_joke():
    print(Fore.LIGHTBLUE_EX + f"TravelBot: {random.choice(jokes)}")


#Display help menu
def show_help():
    print(Fore.MAGENTA + "\nI can:")
    print(Fore.GREEN + "-> Suggest travel spots (Say 'recommendation')")
    print(Fore.GREEN + "-> Offer packing tips (Say 'packing')")
    print(Fore.GREEN + "-> Tell a joke (Say 'joke')")
    print(Fore.CYAN + "Type 'exit' or 'bye' to end.\n")

#Main Chat Loop
def chat():
    print(Fore.LIGHTRED_EX + "Hello! I'm TravelBot.")
    name= input(Fore.LIGHTBLACK_EX + "Your name? ")
    print(Fore.LIGHTGREEN_EX + f"Nice to meet you,{name}!")

    show_help()

    while True:
        user_input= input(Fore.YELLOW+ f"{name}: ")
        user_input=normalize_input(user_input )

        if "recommend" in user_input or "suggest" in user_input:
            recommend()
        elif "pack" in user_input or "packing" in user_input:
            packing_tips()
        elif "joke" in user_input or "funny" in user_input:
            tell_joke()
        elif "help" in user_input:
            show_help()
        elif "exit" in user_input or "bye" in user_input:
            print(Fore.CYAN + "TravelBot: Safe Travels! Goodbye!")
            break
        else:
            print(Fore.LIGHTBLUE_EX + "TravelBot: Could you rephrase?")

#Run the chatbot
if __name__ == "__main__":
    chat()















































