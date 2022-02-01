class Triangle:
    def __init__(self, a: int, b: int, c: int):
        self.a = a
        self.b = b
        self.c = c

    def triangle_perimeter(self):
        return self.a + self.b + self.c

    def triangle_area(self):
        semi_per = self.triangle_perimeter() / 2
        area = (semi_per * (semi_per - self.a) * (semi_per - self.b) * (semi_per - self.c)) ** 0.5
        return area

    def to_sorted_list(self):
        return sorted((self.a, self.b, self.c))

    def is_alike(self, other_triangle):
        list_1 = self.to_sorted_list()
        list_2 = other_triangle.to_sorted_list()
        return list_1[0] / list_2[0] == list_1[1] / list_2[1] == list_1[2] / list_2[2]

    def __eq__(self, other):
        list_1 = self.to_sorted_list()
        list_2 = other.to_sorted_list()
        return list_1[0] == list_2[0] and list_1[1] == list_2[1] and list_1[2] == list_2[2]

    def __lt__(self, other):
        list_1 = self.to_sorted_list()
        list_2 = other.to_sorted_list()
        return list_1[0] < list_2[0] and list_1[1] < list_2[1] and list_1[2] < list_2[2]


class Rectangular:
    def __init__(self, x, y, h):
        self.x = x
        self.y = y
        self.h = h

    def rect_area(self):
        return 2 * ((self.x * self.y) + (self.x * self.h) + (self.y * self.h))

    def to_sorted_list_for_rectangular(self):
        return sorted((self.x, self.y, self.h))

    def __eq__(self, other):
        list_3 = self.to_sorted_list_for_rectangular()
        list_4 = other.to_sorted_list_for_rectangular()
        return list_3[0] == list_4[0] and list_3[1] == list_4[1] and list_3[2] == list_4[2]

    def __lt__(self, other):
        list_3 = self.to_sorted_list_for_rectangular()
        list_4 = other.to_sorted_list_for_rectangular()
        return list_3[0] < list_4[0] and list_3[1] < list_4[1] and list_3[2] < list_4[2]


triangle_1 = Triangle(1, 2, 3)
triangle_2 = Triangle(3, 1, 2)
rectangular_1 = Rectangular(4, 5, 6)
rectangular_2 = Rectangular(8, 9, 10)

print(triangle_1.to_sorted_list(), triangle_2.to_sorted_list())
print(triangle_1.__eq__(triangle_2))
print(triangle_1.__lt__(triangle_2))

print(rectangular_1.to_sorted_list_for_rectangular(), rectangular_2.to_sorted_list_for_rectangular())
print(rectangular_1.__eq__(rectangular_2))
print(rectangular_1.__lt__(rectangular_2))
