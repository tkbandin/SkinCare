from datastore import DataStore
from InputMenu import InputMenu

class Application:
    user_id = None
    datastore = None
    name = "Terra"


    def start(self):
        self.createDataStore()
        self.login()
        print("Welcome to SkinCare 101 " + self.name +
         "! \nWe'll help you to track your AM & PM skincare routine everyday. \nThat way you aren't missing a step and your on way to gorgeous skin!")
        self.promptDailyTip()
        self.fetchOrCreateTodaysActivityLog()
        self.enterMainMenu()

    
    def createDataStore(self):
        self.datastore = DataStore()
        self.datastore.connect()

    def login(self):
        #todo: create login process
        self.user_id = 1
        
    def fetchOrCreateTodaysActivityLog(self):
        today_log = self.datastore.fetchTodayActivityLog(self.user_id)
        if today_log == None:
            self.datastore.createActivityLog(self.user_id)
            today_log = self.datastore.fetchTodayActivityLog(self.user_id)

    def promptDailyTip(self):
        answer = input("Would you like to review your daily skincare tip?\n")
        if answer.lower() == "yes":
            print("Sleeping masks are SO much more than a skincare trend. When you sleep, your skin repairs and replenishes as your skin's metabolism improves, enabling your skin cells to reproduce more efficiently. \nBy wear a hydrating overnight mask, you'll enhance this regeneration process, as it'll act as a protective barrier against dirt or bacteria so that when you wake up your skin is at its best!")
        elif answer.lower() == "no":
            print("Let's move on to your skincare tracker!")
        else:
            print("Please enter yes or no.")

        input("Press enter to continue.")


    def enterMainMenu(self):
        print("\x1bc")
        print("This is the Main Menu:\n ")
        print("What would you like to do?\n")
        choice = "0"
        while choice != "6":
            options = ["Go to Morning Routine Menu.", 
            "Go to Water Intake Menu.", 
            "Go to Evening Routine Menu.", 
            "Go to Face Mask Tracker Menu.", 
            "Go to Exfoliator Tracker.",
            "Exit program."
            ]
            menu = InputMenu("Main Menu Options: \n", options)
            choice = menu.build()

            if choice == "1":
                self.enterMorningRoutine()
            elif choice == "2":
                self.enterWaterIntake()
            elif choice == "3":
                self.enterNightRoutine()
            elif choice == "4":
                self.enterMaskTracker()
            elif choice == "5":
                self.enterExfoliationTracker()
            elif choice == "6":
                continue
            else:
                print("I don't understand your choice. Please select a number 1 through 3.")

    def enterMorningRoutine(self):
        choice = "0"
        while choice == "0":
            options = []
            for product in self.datastore.fetchProductCategories(True):
                options.append(product.name)

            menu = InputMenu("Morning Routine: \n ", options)

            choice = menu.build()

            if choice == "8":
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

    def enterWaterIntake(self):
        print("Water is an important part of your skin health. Let's log your water intake for the day!")
        water_goal = 72

        water_intake = input(
            "Enter the amount of water (in ounces) you have had today.\n")

        print("You have had {} ounces of water today.".format(water_intake))
        total_water_intake = int(water_intake)

        if total_water_intake >= water_goal:
            print("Congratulations! You've hit your water goal for the day! Keep it going!")
        else:
            print("Remember to hit at least 72 ounces of water a day! You got this!")

        input("Press enter to continue.")
    
    def enterNightRoutine(self):
        choice = "0"
        while choice == "0":
            options = []
            for product in self.datastore.fetchProductCategories(False):
                options.append(product.name)

            menu = InputMenu("Evening Routine Menu: \n ", options)

            choice = menu.build()

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
                self.enterMainMenu()
            else:
                print("I don't understand your choice. Please select a number 1 through 6.")

    def enterMaskTracker(self):
        print("Let's track how many face masks you have done this week. It is recommended to do a face mask twice a week!")
        choice = "0"
        while choice == "0":
            options = ["One Mask", "Two Masks"]
            menu = InputMenu("Masks for the Week: \n", options)
            choice = menu.build()

            if choice == "2":
                print("You have completed the recommended number of face masks a week!")
            elif choice == "1":
                print("Awesome! You just need to do one more face mask this week.")
            else:
                print("I don't understand your choice. Please select a number 1 through 2.")

        input("Press enter to continue.")

    def enterExfoliationTracker(self):
        print("Let's track how many times you've exfoliated this week. It is recommended to exfoliate twice a week.")
        choice = "0"
        while choice == "0":
            options = ["Once", "Twice"]
            menu = InputMenu("Times I've exfoliated this week: \n", options)
            choice = menu.build()

            if choice == "2":
                print("Way to go! You've completed teh recommended number of times you should exfoliate for the week.")
            elif choice == "1":
                print("Awesome! You just need to exfoliate one more time this week. We'd recommend waiting two more days until you exfoliate again to give your skin a rest.")
            else:
                print("I don't understand your choice. Please select a number 1 through 2.")

        input("Press enter to continue.")

    def enterEndOfDay(self):
        print("\nAwesome! Look at you! You're well on your way to glowing and clear skin for the next day!\n")
        end_day = input("Would you like to end your day?\n")
        if end_day.lower() == "yes":
            print("See you tomorrow " + self.name + "! Check back in tomorrow to track your day!")
        elif end_day.lower() == "no":
            go_back = input("Would you like to edit anything?\n")
            if go_back.lower() == "yes":
                self.enterMainMenu()
            elif go_back.lower() == "no":
                print("See you tomorrow " + self.name + "!")
            else:
                print("Please enter yes or no.")
        else:
            print("Please enter yes or no.")



#start the program
app = Application()
app.start()
