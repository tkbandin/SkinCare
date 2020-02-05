from InputMenu import InputMenu


name = raw_input("Good morning! What is your name?\n")

print("Welcome to SkinCare 101 " + name +
      "! \nWe'll help you to track your AM & PM skincare routine everyday. \nThat way you aren't missing a step and your on way to gorgeous skin!")

# def askYesNoQuestion(question):
#YesNoAnswer = ""
# while (YesNoAnswer!="YES" and YesNoAnswer!="NO"):
#YesNoAnswer = input(question).upper()
# return YesNoAnswer

# answer = askYesNoQuestion("Would you like to review your daily skincare tip? (Yes or No)")
# if answer == "YES":
#     print("Sleeping masks are SO much more than a skincare trend. When you sleep, your skin repairs and replenishes as your skin's metabolism improves, enabling your skin cells to reproduce more efficiently. By wearing a hydrating overnight mask, you'll enhance this regeneration process, as it'll act as a protective barrier against dirt or bacteria so that when you wake up your skin is at its best!")
# elif answer == "NO":
#     rint("Let's move on to your skincare tracker!")
# else:
#     print("Please enter yes or no.")


answer = raw_input("Would you like to review your daily skincare tip?\n")
if answer == "Yes":
    print("Sleeping masks are SO much more than a skincare trend. When you sleep, your skin repairs and replenishes as your skin's metabolism improves, enabling your skin cells to reproduce more efficiently. \nBy wear a hydrating overnight mask, you'll enhance this regeneration process, as it'll act as a protective barrier against dirt or bacteria so that when you wake up your skin is at its best!")
elif answer == "No":
    print("Let's move on to your skincare tracker!")
else:
    print("Please enter yes or no.")

print("\x1bc")
print("Now let's start off by tracking your morning routine!\n")


# morning routine
def morning_routine(morning):
    for x in morning:
        print(x)


am_routine = ["Cleanser", "Toner", "Vitaminc C", "Serums",
              "Acne products", "Eye cream", "Moisturizer", "SPF"]

morning_routine(am_routine)

# morning routine function


def main():
    choice = "0"
    while choice == "0":
        options = [
            "Cleanser", "Toner", "Vitamin C", "Serums", "Acne Products",
            "Eye Cream", "Moisturizer", "SPF", "Choose 9 to go to another menu."
        ]
        menu = InputMenu( "Main Choice: \nChoose 1 of 9 choices: ", options)
        choice = menu.build()

        if choice == "9":
            print("Go to another menu.")
            second_menu()
        elif choice == "8":
            print("Yay! You used your SPF")
        elif choice == "7":
            print("Yay! You used your Moisturizer!")
        elif choice == "6":
            print("Yay! You used your Eye cream!")
        elif choice == "5":
            print("Yay! You used your Acne products!")
        elif choice == "4":
            print("Yay! You used your Serums!")
        elif choice == "3":
            print("Yay! You used your Vitamin C!")
        elif choice == "2":
            print("Yay! You used your Toner!")
        elif choice == "1":
            print("Yay! You used your Cleanser!")
        else:
            print("I don't understand your choice. Please select a number 1 through 9.")


def second_menu():
    print("This is the second menu.\nChoose 1 of 3 choices: ")
    print("What would you like to do?\n")

    choice = "0"

    while choice != "5":
        print("\x1bc")
        print("Second Menu Options:")
        print("1. Go to Morning Routine Menu.")
        print("2. Go to Water Intake Menu.")
        print("3. Go to Evening Routine Menu")
        print("4. Go to Face Mask Tracker")

        choice = raw_input("Please make a choice: ")

        if choice == "1":
            main()
        elif choice == "2":
            water_intake()
        elif choice == "3":
            evening_routine()
        elif choice == "4":
            mask_tracker()
        else:
            print("I don't understand your choice. Please select a number 1 through 3.")


def water_intake():
    print("Let's log your water intake for the day!")
    water_goal = 72

    water_intake = raw_input(
        "Enter the amount of water (in ounces) you have had today.\n")
    # after this line does it need to be an "if statement"?? to make it work?

    print("You have had {} ounces of water today.".format(water_intake))
    total_water_intake = int(water_intake)

    if total_water_intake >= water_goal:
        # need to make this maybe += because if it is over 72 ounces, that means they still hit their goal water intake for the day
        print("Congratulations! You've hit your water goal for the day! Keep it going!")
    else:
        print("Remember to hit at least 72 ounces of water a day! You got this!")

    raw_input("Press enter to continue.")


def print_eventing_routine_menu():
    print("\x1bc")
    print("Evening Routine Menu: \n Choose 1 of 6 choices: ")
    i = 1
    for item in ["Cleanser", "Toner", "Retinol/Serums", "Acne treatment", "Moisturizer"]:
        print(str(i) + ". " + item)
        i += 1
    print(str(i) + ". Choose 6 to go to another menu.")


def evening_routine():
    choice = "0"
    while choice == "0":
        print_eventing_routine_menu()

        choice = raw_input("Please make a choice: ")

        if choice == "1":
            print("Yay! You've used your Cleanser!")
        elif choice == "2":
            print("Yay! You've used your Toner!")
        elif choice == "3":
            print("Yay! You've used your Retinol/Serums")
        elif choice == "4":
            print("Yay! You've used your Acne treatment!")
        elif choice == "5":
            print("Yay! You used your Moisturizer!")
        elif choice == "6":
            second_menu()
        else:
            print("I don't understand your choice. Please select a number 1 through 6.")

# def mask_tracker():
    # need to just have 2 days of these


main()

# water intake
# #print("Water is an important part of your skin health. Let's track your water intake to ensure your skin is hydrated throughout the day!")
# water_question = raw_input("How many ounces of water have you consumed today?\n")
# if


# night routine

# print("\nLooks like you're getting ready for some beauty sleep!\nLet's end the day with your night time routine.\n")

# def night_routine(evening):
#     for z in evening:
#         print(z)
# pm_routine = ["Cleanser", "Toner", "Retinol/Serums", "Acne Treatment", "Moisturizer"]

# night_routine(pm_routine)


print("\nAwesome! Look at you! You're well on your way to glowing and clearer skin for the next day!\nCheck back in tomorrow to track your day!")

end_day = raw_input("Would you like to end your day?\n")
if end_day == "Yes":
    print("See you tomorrow " + name + "!")
elif answer == "No":
    #print("Would you like to edit anything?\n")
    go_back = raw_input("Would you like to edit anything?\n")
    if go_back == "Yes":
        second_menu()
    elif answer == "No":
        print("See you tomorrow " + name + "!")
    else:
        print("Please enter yes or no.")
else:
    print("Please enter yes or no.")
