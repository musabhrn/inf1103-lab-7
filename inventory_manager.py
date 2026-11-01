import json
import os

from product import Product

class InventoryManager:
    def __init__(self, filename="inventory.json"):
        self._filename = filename
        self._products = []
        self.load()

    def load(self):
        if os.path.exists(self._filename):
            with open(self._filename, "r") as file:
                print(f"{self._filename} found.")
                print("Inventory loaded successfully.\n")
                data = json.load(file)
                self._products = [
                    Product(item["id"], item["name"], item["price"], item["stock"]) 
                    for item in data
                ]
        else:
            print(f"{self._filename} not found. Starting with empty inventory.\n")
            self._products = []

    def save(self):
        print("Saving inventory...")
        data = [product.to_dict() for product in self._products]
        with open(self._filename, "w") as file:
            json.dump(data, file, indent=4)
        print(f"Inventory saved successfully to {self._filename}.\n")

    def display_all(self):
        print("Current Inventory")
        print("-" * 45)
        if not self._products:
            print("No products in inventory.")
        else:
            for item in self._products:
                item.display_information()
        print("-" * 45)
        print()

    def add_product(self):
        print("Add new product")
        product_id = input("Product ID: ").strip()
        name = input("Product Name: ").strip()

        try:
            price = float(input("Price: "))
            stock = int(input("Stock Quantity: "))
        except ValueError:
            print("Invalid price or stock input. Product not added.\n")
            return

        new_product = Product(product_id, name, price, stock)
        self._products.append(new_product)
        print("\nProduct added successfully!\n")

    def update_stock(self):
        print("Update Stock")
        product_id = input("Enter Product ID: ").strip()
        print()

        for item in self._products:
            if item.product_id.lower() == product_id.lower():
                print("Product Found:")
                print(f"Name: {item.name}")
                print(f"Current Stock: {item.stock}\n")
                try:
                    new_stock = int(input("New Stock Quantity: "))
                    item.update_stock(new_stock)
                    print("\nStock updated successfully!\n")
                    return
                except ValueError:
                    print("Invalid stock quantity input\n")
                    return

        print("Product not found.\n")

    def search_product(self):
        print("Search Product")
        query = input("Enter Product ID: ").strip()
        print()

        for item in self._products:
            if item.product_id.lower() == query.lower():
                print("Product Found")
                print("-" * 45)
                item.display_information()
                print("-" * 45 + "\n")
                return

        print("Product not found.\n")