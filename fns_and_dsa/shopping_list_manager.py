
def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            user_entry = input("Enter the item to add: ")
            shopping_list.append(user_entry)
            
        elif choice == '2':
            # Prompt for and remove an item
            user_entry = input("Enter the item you want to remove: ")
            
            if user_entry in shopping_list:
                shopping_list.remove(user_entry)
            else:
                print(f"Item '{user_entry}' not found in the list.")
            
        elif choice == '3':
            # Display the shopping list
            print("Displaying your entire list of items .....")
            print(shopping_list)
            
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
