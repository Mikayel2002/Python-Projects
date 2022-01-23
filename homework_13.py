# 1
# class Circle:
#     def __init__(self, pi, r):
#         self.pi = pi
#         self.r = r
#
#     def perimeter(self):
#         per = 2 * self.pi * self.r
#         return per
#
#     def area(self):
#         area = self.pi * self.r ** 2
#         return area
#
#
# circle_1 = Circle(3.14, 6)
# print(f"Perimeter of circle is {circle_1.perimeter()}, Area of circle is {circle_1.area()}")


# 2
class Human:
    def __init__(self, name, surname, age, weight, height):
        self.name = name
        self.surname = surname
        self.age = age
        self.weight = weight
        self.height = height

    def age_is_100(self):
        year = 2022 + (100 - self.age)
        return f"You will be 100 years old in {year}"

    def optimal_weight(self):
        weight = 50 + (0.91 * self.height) - 152.4
        return f"Your optimal weight is {weight}kg"

    def present_human(self):
        return f"The person's name is: {human_1.name}, surname is: {human_1.surname}, age is: {human_1.age}, weight is: {human_1.weight} height is: {human_1.height}"


human_1 = Human("Mikayel", "Muradyan", 19, 100, 173)
print(human_1.age_is_100())
print(human_1.optimal_weight())
print(human_1.present_human())
