class GarageInventoryManager:
  def __init__(self):
      self.inventory = []

  def add_item(self, name, quantity, category, notes):
      item = {"name": name, "quantity": quantity, "category": category, "notes": notes}
      self.inventory.append(item)
      print(f"{name} added to the inventory successfully.")

  def update_quantity(self, name, new_quantity):
      for item in self.inventory:
          if item["name"] == name:
              item["quantity"] = new_quantity
              print(f"Quantity of {name} updated to {new_quantity} successfully.")
              return
      print(f"Item {name} not found in the inventory.")

  def remove_item(self, name):
      for item in self.inventory:
          if item["name"] == name:
              self.inventory.remove(item)
              print(f"{name} removed from the inventory successfully.")
              return
      print(f"Item {name} not found in the inventory.")

  def display_inventory(self):
      if not self.inventory:
          print("Inventory is empty.")
      else:
          print("Current Inventory:")
          for i, item in enumerate(self.inventory):
              if i % 2 == 0:
                  print(f"\033[1;32mName: \033[0m{item['name']}, \033[1;32mQuantity: \033[0m{item['quantity']}, \033[1;32mCategory: \033[0m{item['category']}, \033[1;32mNotes: \033[0m{item['notes']}")
              else:
                  print(f"\033[1;34mName: \033[0m{item['name']}, \033[1;34mQuantity: \033[0m{item['quantity']}, \033[1;34mCategory: \033[0m{item['category']}, \033[1;34mNotes: \033[0m{item['notes']}")

def main():
  garage_inventory = GarageInventoryManager()

  while True:
      print("\nGarage Inventory Manager")
      print("1. Add Item")
      print("2. Update Quantity")
      print("3. Remove Item")
      print("4. Display Inventory")
      print("5. Exit")

      choice = input("Enter your choice: ")

      if choice == "1":
          name = input("Enter item name: ")
          quantity = input("Enter quantity: ")  # No need to convert to int here
          category = input("Enter category: ")
          notes = input("Enter notes: ")
          garage_inventory.add_item(name, quantity, category, notes)

      elif choice == "2":
          name = input("Enter item name: ")
          new_quantity = input("Enter new quantity: ")  # No need to convert to int here
          garage_inventory.update_quantity(name, new_quantity)

      elif choice == "3":
          name = input("Enter item name: ")
          garage_inventory.remove_item(name)

      elif choice == "4":
          garage_inventory.display_inventory()

      elif choice == "5":
          print("Exiting Garage Inventory Manager.")
          break

      else:
          print("Invalid choice. Please try again.")

if __name__ == "__main__":
  main()
