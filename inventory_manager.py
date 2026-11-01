import json
import os
from product import Product, PhysicalProduct, DigitalProduct

class InventoryManager:
    """Manages a collection of products based on the UML diagram."""
    def __init__(self, filename="inventory.json"):
        self._filename = filename
        self._products = []
        self.load()

    def add_product(self) -> None:
        prod_type = input("Enter product type (physical/digital): ").strip().lower()
        p_id = input("Enter Product ID: ")
        name = input("Enter Name: ")
        price = float(input("Enter Price: "))
        stock = int(input("Enter Stock: "))

        if prod_type == "physical":
            weight = float(input("Enter Weight (kg): "))
            product = PhysicalProduct(p_id, name, price, stock, weight)
        elif prod_type == "digital":
            download_size = float(input("Enter Download Size (MB): "))
            product = DigitalProduct(p_id, name, price, stock, download_size)
        else:
            print("Invalid type. Defaulting to physical product.")
            product = PhysicalProduct(p_id, name, price, stock, 0.0)

        self._products.append(product)
        print("Product added successfully!")

    def update_stock(self, product_id: str, quantity: int) -> bool:
        product = self.search_product(product_id)
        if product:
            product.update_stock(quantity)
            return True
        return False

    def search_product(self, product_id: str) -> Product | None:
        for product in self._products:
            if product.product_id.lower() == product_id.lower():
                return product
        return None

    def save(self) -> None:
        data = [p.to_dict() for p in self._products]
        with open(self._filename, "w") as f:
            json.dump(data, f, indent=4)

    def load(self) -> None:
        if os.path.exists(self._filename):
            try:
                with open(self._filename, "r") as f:
                    data = json.load(f)
                    self._products = []
                    for item in data:
                        if item.get("type") == "physical":
                            prod = PhysicalProduct(
                                item["id"], item["name"], item["price"], item["stock"], item["weight"]
                            )
                        elif item.get("type") == "digital":
                            prod = DigitalProduct(
                                item["id"], item["name"], item["price"], item["stock"], item["download_size"]
                            )
                        else:
                            prod = PhysicalProduct(
                                item["id"], item["name"], item["price"], item["stock"], 0.0
                            )
                        self._products.append(prod)
            except Exception as e:
                print(f"Error loading inventory: {e}")
                self._products = []
        else:
            self._products = []

    def display_all(self) -> None:
        if not self._products:
            print("No products in inventory.")
        else:
            for product in self._products:
                product.display_information()
            print()