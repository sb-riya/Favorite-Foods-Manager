def display_menu():
    """Displays the menu options."""
    print("\nFavorite Foods Manager")
    print("======================")
    print("0. Exit")
    print("1. Add a favorite food")
    print("2. Remove a favorite food")
    print("3. View all favorite foods")
    print("======================")

def add_food(favorite_foods):
    """Adds a food to the favorite foods list."""
    food = input("Enter the name of the food to add: ").strip()
    if food:
        favorite_foods.append(food)
        print(f"'{food}' has been added to your favorite foods.")
    else:
        print("Invalid input! Food name cannot be empty.")

def remove_food(favorite_foods):
    """Removes a food from the favorite foods list."""
    if favorite_foods:
        print("\nSelect a food to remove:")
        for idx, food in enumerate(favorite_foods, start=1):
            print(f"{idx}. {food}")
        try:
            choice = int(input("Enter the number of the food to remove: "))
            if 1 <= choice <= len(favorite_foods):
                removed_food = favorite_foods.pop(choice - 1)
                print(f"'{removed_food}' has been removed from your favorite foods.")
            else:
                print("Invalid number. Please try again.")
        except ValueError:
            print("Invalid input! Please enter a number.")
    else:
        print("Your favorite foods list is empty. Nothing to remove.")

def view_foods(favorite_foods):
    """Displays all the favorite foods."""
    if favorite_foods:
        print("\nYour Favorite Foods:")
        for idx, food in enumerate(favorite_foods, start=1):
            print(f"{idx}. {food}")
    else:
        print("\nYour favorite foods list is empty.")

def main():
    """Main function to run the Favorite Foods Manager."""
    favorite_foods = []  # List to store favorite foods

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '0':
            print("Exiting the Favorite Foods Manager. Goodbye!")
            break
        elif choice == '1':
            add_food(favorite_foods)
        elif choice == '2':
            remove_food(favorite_foods)
        elif choice == '3':
            view_foods(favorite_foods)
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
