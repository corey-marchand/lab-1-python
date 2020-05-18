from textwrap import dedent

items = {
    "Wings" : 0,
    "Cookies" : 0,
    "Spring Rolls" : 0,
    "Salmon" : 0,
    "Steak" : 0,
    "Meat Tornado" : 0,
    "A Literal Garden" : 0,
    "Ice Cream" : 0,
    "Cake" : 0,
    "Pie" : 0,
    "Coffee" : 0,
    "Tea" : 0,
    "Unicorn Tears" : 0
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
        user_prompt = """ 
            ***********************************
            ** What would you like to order? **
            ***********************************
"""
        dedent_prompt = dedent(user_prompt)
        
        prompt = input(dedent_prompt)

        quantity = items["Wings"]

        if prompt == 'quit':
            break
        
        elif prompt in items: 
            print(f"** 1 order of {prompt} have been added to your meal **")
        
            items[prompt] += 1

        if quantity >= 1 in items:
            print("hello")
            print(f"** 2 order of {prompt} have been added to your meal **")

        print(dedent(prompt))


def main():
    welcome()
    show_menu()
    take_order()

if __name__ == "__main__":
    main()
