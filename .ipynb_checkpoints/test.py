class Strings():
    def __init__(self, strings):
        self.strings = strings

    def get(self):
        enter = input('\nWhat would you like to see? ')
        if len(self.strings) > 0:
            self.strings.pop(0)
        else:
            self.strings.append(enter)

    def print(self):
        print(''.join(self.strings).upper())

    def polly(self):
        print('Polly want a cracker')


words = Strings([])


def rerun():
    while True:
        echo = input(
            '\nEnter "repeat" for a chance to echo, or "quit" to exit. Enter "polly" for a surprise. ')

        if echo.lower() == 'polly':
            words.polly()
        elif echo.lower() == 'quit':
            break
        else:
            words.get()
            words.print()


rerun()
# class Cart():

#     def __init__(self, items):
#         self.items = items

#     def showCart(self):
#         print("You have the following items in your bag: ")
#         for item in self.items:
#             print(item)

#     def addCart(self):
#         products = input('What would you like to add? ')
#         self.items.append(products)

#     def removeCart(self):
#         remove = input('What would you like to remove? ')
#         self.items.remove(remove)


# bag = Cart([])


# def run():
#     while True:
#         response = input('What do you want to do? add/show/remove or quit: ')

#         if response.lower() == 'quit':
#             bag.showCart()
#             print('Thanks for shopping')
#             break
#         elif response.lower() == 'add':
#             bag.addCart()

#         elif response.lower() == 'show':
#             bag.showCart()

#         elif response.lower() == 'remove':
#             bag.removeCart()


# run()
