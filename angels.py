"""

    Angels v1.0.0
    Created by Jordan Newland
    Published May 2017

    Copyright (c) 2020 Jordan Newland

"""

# Imports
import random
import time

# Global Variable Declaration
alive = True


# Main Function - All code contained within the main function
def main():
    global alive

    # Logging Function - creates a logger util to print messages to console with timestamp and type of log message
    # (error, debug etc.)
    def log(level="INFO", value=""):
        debug = False
        timestamp = time.strftime("%H:%M:%S")
        if level == "":
            level = "INFO"
        else:
            level = level.upper()
        message = value
        concat_log_msg = "[" + timestamp + "][" + level + "] " + message
        print(concat_log_msg)

    # Print Initial Info
    def print_info():
        print("\n" + "Welcome to Angels")
        print("Angels is The Python Text-Based Adventure Game")
        print("The game is simple, survive the Weeping Angels and return the Tardis to The Doctor.")
        print("Should you fail, you'll be sent back in time by the angels and used to fuel the time energy "
              "they use to thrive this world killing anyone that they encounter.")
        print()

    def print_story():
        print("\nHello, ")
        print("My name is The Doctor, I'm a time lord and I need your help.")
        print("I'm currently stuck in 1969. Without my time machine.")
        print("I was brought here by the touch of the Weeping Angels and now it's up to you to return my "
              "time machine to me")
        print("However, there's a slight problem. The Tardis, my time machine, is guarded by the angels.")
        print("You must reach the Tardis without being touched by an angel. It's the only way.")
        print("Before you go...\n")
        time.sleep(1.5)
        print("Remember...")
        time.sleep(1.25)
        print("Don't blink. Don't even blink. Blink and you're dead. They are fast, faster than you "
              "can believe. Don't turn your back, don't look away, and don't blink. Good luck.")
        time.sleep(4)
        print()

    def print_scenario():
        print("> The Tardis is not more than 5 steps from me.")
        print("> However, it's surrounded by Angels")
        print("> What do I do?")
        print()

    def print_choices():
        print("I've got limited options. I could... ")
        print()
        print(
            "#1 - Blink"
            "\n" "#2 - Resist Blinking and ease your way towards the Tardis"
            "\n" "#3 - Run for the Tardis"
            "\n" "#4 - Attempt to escape the area"
        )

    # Positive Outcomes
    outcome_01 = "You're successfully able to move closer to the Tardis (+1 Step)"
    outcome_02 = "It seems you got lucky, you've moved even closer (+2 Steps)"
    outcome_03 = "So close, I can feel it. (+3 Steps)"

    # Negative Outcomes
    n_outcome_01 = "Dead!"  # TODO: Replace values with something more realistic
    n_outcome_02 = "Still Dead!"  # TODO: Replace values with something more realistic
    n_outcome_03 = "Probably still dead"  # TODO: Replace values with something more realistic

    def option_chosen(value):
        global alive
        steps = 0
        steps_to_finish = 5  # Configure the maximum amount of steps the game has. Increases / decreases difficulty.

        try:
            value = int(value)
        except ValueError as error:
            log("ERROR", "Error Converting Type to Integer."
                         "\n\t StackTrace:"
                         "\n\t\t" + str(error) + "\n")

        if steps <= steps_to_finish and alive:
            if value == 1:
                rand_response = random.randint(1, 2)
                if rand_response == 1:
                    steps += 1
                    print(outcome_01, "- ( " + str(steps) + " remaining )")
                elif rand_response == 2:
                    steps = 0
                    print(n_outcome_01)
                    alive = False
                else:
                    log("ERROR", "An exception occurred. Please report this bug on GitHub. "
                                 "(https://github.com/jenewland1999/angels/issues)")
            elif value == 2:
                rand_response_2 = random.randint(1, 9)
                if rand_response_2 == 1:
                    steps += 1
                    print(outcome_01, "- ( " + str(steps) + " remaining )")
                elif rand_response_2 == 2:
                    steps += 2
                    print(outcome_02, "- ( " + str(steps) + " remaining )")
                elif rand_response_2 == 3:
                    steps += 3
                    print(outcome_03, "- ( " + str(steps) + " remaining )")
                elif rand_response_2 != 1 or rand_response_2 != 2 or rand_response_2 != 3:
                    steps = 0
                    print(n_outcome_01)
                    alive = False
            elif value == 3:
                rand_response_3 = random.randint(1, 10)
                if rand_response_3 == 1:
                    steps = steps_to_finish
                    print(outcome_01, "- ( " + str(steps) + " remaining )")
                elif rand_response_3 != 1:
                    steps = 0
                    print(n_outcome_01)
                    alive = False
            elif value == 4:
                steps = 0
                print(n_outcome_01)
                alive = False
            else:
                log("ERROR", "An exception occurred. Please report this bug on GitHub. "
                             "(https://github.com/jenewland1999/angels/issues)")

    def ask_for_help():
        print("Before we start, do you wish to activate the additional help?")
        while True:
            response = input("Do you require additional help? Please type [yes] or [y] "
                             "for yes and [no] or [n] for no. ")
            response = str(response.strip().lower().replace("[", "").replace("]", ""))
            if response == "yes" or response == "y":
                return True
            elif response == "no" or response == "n":
                return False

    # On-Screen Help Function - Gives additional help to the user that requests it.
    def print_tutorial():
        print("\nOn-Screen Help")
        print("==============")
        print("In this game, you're playing against the computer.")
        print("When the game starts, you'll be given an introduction to the story.")
        print("Following this you'll get 4 options to choose from.")
        print("These options do various things:\n")
        print("#1 - Blink: This option gives you a 50/50 chance to progress a single step into the game. "
              "Once the choice is picked the game will generate a random number between 1 and 2. "
              "The outcome of this randomly generated number will decide whether you proceed or die (ending the game)\n")
        print("#2 - Resist Blinking and ease your way towards the Tardis: "
              "If you choose this option one of four outcomes will occur. "
              "The first being the same as above, you move forward one step. "
              "The second and third move you 2 or 3 steps closer. "
              "However, this comes with a consequence of being twice as likely to die (ending the game)\n")
        print("#3 - Run for the Tardis: This option is rather risky. "
              "You have a 1 in 10 chance to successfully make it to the Tardis in a single move. "
              "However, since it's only a 1 in 10 chance it's a risky choice.\n")
        print("#4 - Attempt to escape the area: In doing this, you may experience side effects. "
              "The true result of this choice is unknown.\n")
        print("Once you've made your choice the computer will generate the random number between the range specified"
              " for the choice that you picked. Then will either return a message saying you successfully moved an x"
              " amount of steps closer or that you died (ending the game).")
        print("Once the game has ended, you are asked whether you'd like to play again. "
              "So, you're able to replay as many times as you want.")
        print("\n==============")
        print("End of On-Screen Help\n")

    cont = True
    # Game Loop - The loop that the game relies on.
    while cont:
        print_info()
        tutorial = ask_for_help()
        if tutorial:
            print_tutorial()
        print_story()
        print_scenario()
        while alive:
            print_choices()
            option_chosen(input("Enter your choice (1 - 4) "))
        # TODO: Create function for stripping text and formatting it for validation or comparisons
        play_again = str(input("Do you wish to play again? ").strip().lower())
        if play_again == "yes" or play_again == "y":
            cont = True
            alive = True
        elif play_again == "no" or play_again == "n":
            cont = False
            print("Goodbye")
        else:
            log("ERROR", "An exception occurred. Please report this bug on GitHub. "
                         "(https://github.com/jenewland1999/angels/issues)")
            cont = False
            alive = True

# Invoke the main function
main()
