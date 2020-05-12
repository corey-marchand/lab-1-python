from textwrap import dedent

items = {
    "wings" : 0
}

def welcome():
    message = """
    **************************************
    **    Welcome to the Snakes Cafe!   **
    **    Please see our menu below.    **
    **
    ** To quit at any time, type "quit" **
    **************************************
"""
    print(dedent(message))

def show_menu():
        menu = """
        Appetizers
        ----------
        Wings
        Cookies
        Spring Rolls

        Entrees
        -------
        Salmon
        Steak
        Meat Tornado
        A Literal Garden

        Desserts
        --------
        Ice Cream
        Cake
        Pie

        Drinks
        ------
        Coffee
        Tea
        Unicorn Tears
"""

        print(dedent(menu))

def take_order():
    
    while True:

        prompt = input("""
            ***********************************
            ** What would you like to order? **
            ***********************************
    """)

        if prompt == 'quit':
            break
        
        if prompt in items: 
            # pre_amount = items[order]
            print()
            print(f"** 1 order of {prompt} have been added to your meal **")
        
        if prompt in items > 1:
            print(f"** 1 order of {prompt} have been added to your meal **")

        print(dedent(prompt))


def main():
    welcome()
    show_menu()
    take_order()

if __name__ == "__main__":
    main()
