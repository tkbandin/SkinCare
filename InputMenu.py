class InputMenu:
    title = ""
    options = []



    def __init__(self, title, options):
        # body of the constructor
        self.title = title
        self.options = options

    def build(self):
        print("\x1bc")
        print(self.title)
        i = 0
        for option in self.options:
            i += 1
            print("{}. {}".format(i, option))
        result = raw_input("Select an option 1-{}: ".format(i))
        return result
    


# menu = InputMenu("Main Choice", ["Cleanser", "Toner", "Retinol/Serums", "Acne treatment", "Moisturizer"])
# print(menu.build())