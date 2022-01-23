# class Human:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     def present(self):
#         print(self.name, self.surname)
#
#
# person_1 = Human("Mikayel", "Muradyan")
# print(person_1.name, person_1.surname)


# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def perimeter(self):
#         p = self.a + self.b + self.c
#         return p
#
#     def to_sorted_list(self):
#         return sorted((self.a, self.b, self.c))
#
#     def is_alike(self, other_triangle):
#         first_list = self.to_sorted_list()
#         second_list = other_triangle.to_sorted_list()
#         return first_list[0] / second_list[0] == first_list[1] / second_list[1] == first_list[2] / second_list[2]
#
#
# triangle_1 = Triangle(4, 5, 3)
# triangle_2 = Triangle(6, 10, 8)
# print(triangle_1.perimeter(), triangle_2.perimeter())
# print(triangle_1.to_sorted_list(), triangle_2.to_sorted_list())
# print(triangle_1.is_alike(triangle_2))


class Triangle:
    def __init__(self, a, b, c):
        if not isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float)):
            raise TypeError("Wrong type!")

        self.a = a
        self.b = b
        self.c = c
        self.height = None

    def to_sorted_list(self):
        return sorted((self.a, self.b, self.c))

    def is_in_second_triangle(self, other):
        # if type(other) is not Triangle:
        if not isinstance(other, Triangle):
            raise TypeError(f"{other} is not an instance of Triangle")

        list_1 = self.to_sorted_list()
        list_2 = other.to_sorted_list()
        return list_1[0] < list_2[0] and list_1[1] < list_2[1] and list_1[2] < list_2[2]

    def set_height(self, height):
        if not isinstance(height, (int, float)):
            raise  TypeError(f"{height} is not an instance of int or float")

        self.height = height


triangle_1 = Triangle(4, 3, 2)
triangle_2 = Triangle(5, 8, 7)

print(triangle_1.to_sorted_list(), triangle_2.to_sorted_list())
print(triangle_1.is_in_second_triangle(triangle_2))


# Jarangum
# class RectTriangle(Triangle):