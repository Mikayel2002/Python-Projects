# class Car:
#     car_type = "Sport"
#     model = "Nissan"
#     prod_year = 2016
#
#
# print(Car.car_type, Car.model, Car.prod_year)


class Car:
    NAME = "Class Car"

    def __init__(self, name, color, year):
        self.car_name = name
        self.color = color
        self.year = year

    def present(self):
        print(self.car_name, self.year, self.color)

    def change_year(self, new_year):
        if type(new_year) is int:
            self.year = new_year
        else:
            raise ValueError(f"{new_year} is not an integer!")
#
#
car_1 = Car("bmw x5", "white", 2022)
car_2 = Car("mercedes", "red", 2021)

# print(car_1, car_2)

# print(car_1.car_name, car_1.color, car_1.year)
# print(car_2.car_name, car_2.color, car_2.year)

print(car_1.__dict__)
print(car_2.__dict__)

# print(car_1.NAME)
# print(car_2.NAME)

# car_2.year = 2011
# print(car_2.__dict__)

# car_1.present()
# car_2.present()
# Car.present(car_1)

# car_3 = Car("audi", "black", 2013)
# Car.present((car_3))
# car_3.model = "a6"
# print(car_1.__dict__, car_3.__dict__, sep="\n")
#
# Car.type = "sport"
# print(car_1.type)
# car_1.type = "common"
# print(car_1.type)
# print(car_2.type)

# print(car_1.__dict__)
# car_1.change_year(2012)
# print(car_1.__dict__)
# car_1.change_year("2012")


