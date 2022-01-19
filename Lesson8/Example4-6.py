class Warehouse:
    name: str
    capacity: int = 10
    current_number: int = 0

    storage: dict = {}

    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def get(self, name, quantity):
        if self.capacity - self.current_number > quantity:
            if name not in self.storage:
                self.storage[name] = quantity
            else:
                self.storage[name] += quantity
            self.current_number += quantity
        print(f"{name} размещен в {self.name}")

    def move(self, name, quantity, place):
        if name not in self.storage:
            print("Этого оборудования нет!")
        elif self.storage[name] < quantity:
            print(f"Недостаточно оборудования на {self.name}")
        else:
            print(f"Перевезти {name} из {self.name} в {place.name}")
            self.storage[name] -= quantity
            place.get(name, quantity)
            self.current_number -= quantity

    @property
    def show_storage(self):
        return print(f"На {self.name} {self.storage}")


class Office(Warehouse):
    storage: dict = {}

    def __init__(self, name, capacity=5):
        super().__init__(name, capacity)
        self.name = name
        self.capacity = capacity


class OfficeEquipment:
    title: str
    model: str
    formats: list
    price: int

    count = 0

    def __init__(self, title, model, price):
        self.title = title
        self.model = model
        self.price = price
        self.name = f"{model} {title}"
        self.count += 1
        warehouse.get(self.name, 1)


class Printer(OfficeEquipment):
    ciss: bool
    color_printing: bool

    def __init__(self, title, model, price, ciss, color_printing):
        super().__init__(title, model, price)
        self.title = title
        self.model = model
        self.price = price
        self.name = f"{model} {title}"
        self.ciss = ciss
        self.color_printing = color_printing
        self.count += 1
        warehouse.get(self.name, 1)


class Scanner(OfficeEquipment):
    color_scanning: bool
    resolution: int


class Xerox(OfficeEquipment):
    scanning_speed: int
    xerox_capacity: int


warehouse = Warehouse("Склад", 10)
Pobedy = Office("Офис")
printer = Printer("printer", "samsung", "4000", True, True)
warehouse.show_storage
warehouse.move("samsung printer", 1, Pobedy)
warehouse.show_storage
Pobedy.show_storage