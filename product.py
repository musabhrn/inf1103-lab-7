from abc import ABC, abstractmethod

class CanBeShipped(ABC):
    """Interface for products that require physical shipping."""
    @abstractmethod
    def calculate_shipping_cost(self) -> float:
        pass

class Product(ABC):
    def __init__(self, product_id, name, price, stock):
        self._product_id = product_id
        self._name = name
        self._price = float(price)
        self._stock = int(stock)

    @property
    def product_id(self):
        return self._product_id

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @property
    def stock(self):
        return self._stock

    def update_stock(self, quantity: int) -> None:
        self._stock = quantity

    def display_information(self) -> None:
        """Displays formatted information for the product."""
        print(f"ID: {self._product_id} | Name: {self._name} | Price: ${self._price:.2f} | Stock: {self._stock}", end="")

    @abstractmethod
    def get_fulfilment_info(self) -> str:
        """Abstract method forcing subclasses to define fulfilment behavior."""
        pass
    
    def to_dict(self):
        """Convert Product object back to a dictionary for JSON storage."""
        return {
            "id": self._product_id,
            "name": self._name,
            "price": self._price,
            "stock": self._stock
        }

class PhysicalProduct(Product, CanBeShipped):
    """A physical product that has weight and can be shipped."""
    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        self._weight = float(weight)

    @property
    def weight(self):
        return self._weight

    def get_fulfilment_info(self) -> str:
        return "Requires physical shipping."

    def calculate_shipping_cost(self) -> float:
        return 5.00 + (2.00 * self._weight)

    def display_information(self) -> None:
        super().display_information()
        print(f" | Weight: {self._weight}kg | Shipping Cost: ${self.calculate_shipping_cost():.2f} | Fulfilment: {self.get_fulfilment_info()}")

    def to_dict(self) -> dict:
        base = super().to_dict()
        base["type"] = "physical"
        base["weight"] = self._weight
        return base

class DigitalProduct(Product):
    """A digital product delivered via download size."""
    def __init__(self, product_id, name, price, stock, download_size):
        super().__init__(product_id, name, price, stock)
        self._download_size = float(download_size)

    @property
    def download_size(self):
        return self._download_size

    def get_fulfilment_info(self) -> str:
        return "Delivered digitally via download link."

    def display_information(self) -> None:
        super().display_information()
        print(f" | Download Size: {self._download_size}MB | Fulfilment: {self.get_fulfilment_info()}")

    def to_dict(self) -> dict:
        base = super().to_dict()
        base["type"] = "digital"
        base["download_size"] = self._download_size
        return base