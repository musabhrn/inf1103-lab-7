from inventory_manager import InventoryManager

def display_menu():
    print("=" * 35)
    print("INVENTORY MANAGEMENT SYSTEM (OOP)")
    print("=" * 35)
    print()


def main():
    display_menu()
    manager = InventoryManager()

    while True:
        print("--------MENU--------")
        print("1. Display All Products")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Save Inventory")
        print("6. Exit")
        print("--------------------\n")

        option = input("Enter option: ").strip()
        print()

        if option == "1":
            manager.display_all()
        elif option == "2":
            manager.add_product()
        elif option == "3":
            manager.update_stock()
        elif option == "4":
            manager.search_product()
        elif option == "5":
            manager.save()
        elif option == "6":
            print("Saving inventory before exit...")
            manager.save()
            print("Thank you for using Inventory Management System.")
            print("Program terminated.")
            break
        else: 
            print("Invalid option. Please try again.\n")


if __name__ == "__main__":
    main()