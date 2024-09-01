class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        n = 0
        if new_floor > self.number_of_floors or new_floor > 1:
            for i in range(new_floor):
                n += 1
                print(n)
        else:
            print("Такого этажа не существует")

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"


Home1 = House('Дом', 10)
Home2 = House('Высотка', 17)
# Home1.go_to(0)
# Home2.go_to(3)

print(Home1)
print(Home2)

print(len(Home1))
print(len(Home2))