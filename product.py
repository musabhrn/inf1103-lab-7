class Product:
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
        print(f"ID: {self._product_id} | Name: {self._name} | Price: ${self._price:.2f} | Stock: {self._stock}")
    
    def to_dict(self):
        """Convert Product object back to a dictionary for JSON storage."""
        return {
            "id": self._product_id,
            "name": self._name,
            "price": self._price,
            "stock": self._stock
        }