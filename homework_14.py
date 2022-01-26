# 1
class Country:
    def __init__(self, country_name, continent):
        self.country_name = country_name
        self.continent = continent

    def present(self):
        return "Country name is {} and Continent is {}".format(self.country_name, self.continent)


class Brand:
    def __init__(self, brand_name, start_date):
        self.brand_name = brand_name
        self.start_date = start_date

    def present(self):
        return "Brand name is {} and Business start date is: {}".format(self.brand_name, self.start_date)


class Season:
    def __init__(self, season_name, average_temp):
        self.season_name = season_name
        self.average_temp = average_temp

    def present(self):
        return "Season name is {} and average temperature is {}".format(self.season_name, self.average_temp)


class Product(Season, Brand, Country):
    def __init__(self, prod_type, prod_price, prod_quantity, *args, **kwargs):
        self.prod_type = prod_type
        self.prod_price = prod_price
        self.prod_quantity = prod_quantity
        print("in class Product", args, kwargs)
        super().__init__(*args, **kwargs)

    def present(self):
        return "The type of product is {}, the price of product is {} dollars, " \
               "the quantity of product is {}".format(self.prod_type, self.prod_price, self.prod_quantity)

    def discount_price(self):
        percent = 20
        discount = (self.prod_price * percent) / 100
        new_price = self.prod_price - discount

        return new_price

    def increase_the_quantity(self):
        if self.prod_quantity <= 3:
            self.prod_quantity += 2
            return self.prod_quantity
        else:
            self.prod_quantity -= 2
            return self.prod_quantity


print(Product.__mro__)
a = Product("Car", 10000, 6, "Summer", 30)
print(a.discount_price())
print(a.increase_the_quantity())
