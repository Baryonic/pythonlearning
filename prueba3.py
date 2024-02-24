def get_favorite_color():
    """
    Asks the user for their favorite color and returns it.
    """
    return input("What's your favorite color? ")

def main():
    print("Welcome to the Favorite Color Program!")
    print("Type 'end program' to exit.")

    while True:
        user_input = get_favorite_color().lower()

        if user_input == "end program":
            print("Goodbye! Thanks for using the program.")
            break
        else:
            print(f"Your favorite color is {user_input.capitalize()}!")

if __name__ == "__main__":
    main()
