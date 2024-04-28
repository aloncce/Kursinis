class Product:
  def __init__(self, name, quantity, price, discount):
      self._name = name
      self._quantity = quantity
      self._price = price
      self._discount = discount

  @property
  def name(self):
      return self._name

  @property
  def quantity(self):
      return self._quantity

  @quantity.setter
  def quantity(self, value):
      self._quantity = value

  @property
  def price(self):
      return self._price

  @property
  def discount(self):
      return self._discount


class ProductFactory:
  @staticmethod
  def create_product(name, quantity, price, discount):
      return Product(name, quantity, price, discount)


class ProductCatalog:
  _instance = None

  def __init__(self):
      self._products = []

  @classmethod
  def get_instance(cls):
      if cls._instance is None:
          cls._instance = cls()
      return cls._instance

  def add_product(self, product):
      self._products.append(product)

  def find_product(self, name):
      for product in self._products:
          if product.name == name:
              return product
      return None

  def update_product(self, product):
      for idx, p in enumerate(self._products):
          if p.name == product.name:
              self._products[idx] = product
              break

  def load_products_from_file(self, filename):
      with open(filename, 'r') as file:
          data = file.readlines()
          for line in data:
              name, quantity, price, discount = self._parse_product_line(line)
              product = ProductFactory.create_product(name, int(quantity), float(price), float(discount))
              self.add_product(product)

  def save_products_to_file(self, filename):
      with open(filename, 'w') as file:
          for product in self._products:
              file.write(f"{product.name}[Kiekis: {product.quantity}; Kaina: {product.price}; Nuolaida: {product.discount}]\n")

  def _parse_product_line(self, line):
      name = line.split("[")[0].strip()
      details = line.split("[")[1].split(";")
      quantity = details[0].split(":")[1].strip()
      price = details[1].split(":")[1].strip()
      discount = details[2].split(":")[1].strip()[:-1]
      return name, quantity, price, discount

  def calculate_total(self, items):
      total = 0
      for name, quantity in items.items():
          product = self.find_product(name)
          if product:
              total += product.price * quantity * (1 - product.discount / 100)
      return total

  def update_product_quantities(self, items):
      for name, quantity in items.items():
          product = self.find_product(name)
          if product:
              product.quantity -= quantity
              self.update_product(product)


class ShoppingList:
  def __init__(self):
      self._items = {}

  def load_items_from_file(self, filename):
      with open(filename, 'r') as file:
          data = file.readlines()
          for line in data:
              name, quantity = line.strip().split()
              self._items[name] = int(quantity)

  def get_items(self):
      return self._items

  def update_quantity(self, products):
      for name, quantity in products.items():
          if name in self._items:
              self._items[name] -= quantity


def main():
  product_catalog = ProductCatalog.get_instance()
  product_catalog.load_products_from_file('Produktai.txt')

  shopping_list = ShoppingList()
  shopping_list.load_items_from_file('Pirkiniai.txt')

  products_to_update = shopping_list.get_items()

  product_catalog.update_product_quantities(products_to_update)
  product_catalog.save_products_to_file('Produktai.txt')

  total_amount = product_catalog.calculate_total(products_to_update)

  with open("Suma.txt", "w") as file:
      file.write(f"Bendra suma: {total_amount:.2f} EUR\n")


if __name__ == "__main__":
  main()






