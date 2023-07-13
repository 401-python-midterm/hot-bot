import os
import sys
from rich.console import Console
from rich.prompt import Prompt
from modules.GPTtest30 import gpt_30
from modules.GPTtest60 import gpt_60
from modules.GPTtest90 import gpt_90
from modules.option import user_option
console = Console()
from modules.option_transfer import tranfer_option
# Read the API key from gpt_api.txt file
with open('gpt_api.txt', 'r') as file:
    gpt_api = file.read().strip()


# Define the menu function
def menu():
    while True:
        console.clear()
        os.system('clear')
        console.print(
            "\n1. Help\n2. Strategy\n3. Engage AI\n4. Historical Trends\n5. Sandbox\n6. Set It Loose\n7. Exit",
            soft_wrap=False,
        )
        choice = Prompt.ask('Choose a task (Enter the number)', choices=["1", "2", "3", "4", "5", "6", "7"], default='6')

        if choice == '1':
            help_menu()

        elif choice == '2':
            # Add your code for choice 2 here
           choice2()

        elif choice == '3':
            # Add your code for choice 3 here
            pass

        elif choice == '4':
            # Add your code for choice 4 here
            pass

        elif choice == '5':
            # Add your code for choice 5 here
            pass

        elif choice == '6':
            # set_it_loose(btc_data, eth_data)
            pass

        elif choice == '7':
            console.print('Exiting...')
            break

        else:
            console.print('Invalid choice. Please try again.')

# Define the help menu function
def help_menu():
    console.clear()
    console.print('This will offer an overview of the program')
    console.print('Press Enter to go back to the main menu...')
    input()  # Wait for user to press Enter

def choice2():
    day_choice = Prompt.ask('Choose 30, 60, or 90 days (Enter the number)', choices=["30", "60", "90"], default='30')
    option_choice = Prompt.ask('Choose a strategy Conservative (C), Risky (R), Beginner (B)', choices=["Conservative", "Risky", "Beginner", "C", "R", "B"], default='4')
    if option_choice.lower() == "Conservative" or option_choice.lower() == "C":
        option_choice_validated = "conservative"

    elif option_choice.lower() == "Risky".lower() or option_choice.lower() == "R":
        option_choice_validated = "risky"

    elif option_choice.lower() == "Beginner".lower() or option_choice.lower() == "B":
        option_choice_validated = "beginner"
    else:
        exit    

    console.print("Generating response...")
    call_gpttest(day_choice, option_choice_validated)
    
    if day_choice ==   '30':
        gpt_30(option_choice_validated)
        input()
    elif day_choice == '60':
        gpt_60(option_choice_validated)
        input()
    elif day_choice == '90':
        gpt_90(option_choice_validated)
        input()
    else:
        exit
    
def call_gpttest(days, option):
      pass


    

menu()