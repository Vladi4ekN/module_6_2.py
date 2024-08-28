class Vehicle:
    __COLOR_VARIANTS = ["red", "blue", "green", "black", "white"]

    def __init__(self, owner, model, engine_power, color):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color if color.lower() in self.__COLOR_VARIANTS else None

        if self.__color is None:
            raise ValueError(f"Цвет '{color}' не допустим. Допустимые цвета: {self.__COLOR_VARIANTS}")

    def get_model(self):
        return f"Модель: {self.__model}"

    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self):
        return f"Цвет: {self.__color}" if self.__color else "Цвет не установлен"

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}")

    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
            print(f"Цвет изменен на {new_color}")
        else:
            print(f"Нельзя сменить цвет на {new_color}")


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

    def __init__(self, owner, model, engine_power, color):
        super().__init__(owner, model, engine_power, color)

    @classmethod
    def get_passengers_limit(cls):
        return cls.__PASSENGERS_LIMIT


# Пример использования классов
try:
    my_vehicle = Vehicle("Иван", "Toyota Camry", 200, "red")
    my_vehicle.print_info()
    my_vehicle.set_color("blue")
    my_vehicle.print_info()
    my_vehicle.set_color("yellow")  # Неправильный цвет

    my_sedan = Sedan("Петр", "Honda Accord", 220, "black")
    my_sedan.print_info()
    print(f"Максимальное количество пассажиров: {Sedan.get_passengers_limit()}")

except ValueError as e:
    print(e)