import math


class Triangle:
    eps = 1e-5

    def __init__(self, neighbours, id=0):
        # 3 соседа - пары [ребро на границе, треугольник]
        # None - внешний мир
        self.neighbours = neighbours
        # id - место треугольника в triangle_list
        self.id = id

    # возвращает точки треугольника
    def points(self):
        triangle_points = set()
        for edge, triangle in self.neighbours:
            triangle_points.add(edge[0])
            triangle_points.add(edge[1])
        return list(triangle_points)

    # проверка, есть ли точка в треугольнике
    def is_point_in(self, point):
        # метод площадей
        # считаем сумму трёх площадей, образованных рёбрами треугольника и данной точкой
        # сравниваем её с площадью треугольника; если равны, то точка внутри
        p1, p2, p3 = self.points()
        S1 = Triangle.S(p1, p2, point)
        S2 = Triangle.S(p2, p3, point)
        S3 = Triangle.S(p1, p3, point)
        S = Triangle.S(p1, p2, p3)
        return S - Triangle.eps <= S1 + S2 + S3 <= S + Triangle.eps

    # возвращает соседний треугольник по данному ребру
    def get_neigh(self, edge):
        edge = set(edge)
        for triangle_edge, triangle in self.neighbours:
            if set(triangle_edge) == edge:
                return triangle

    # устанавливает соседа треугольника по данному ребру
    def set_neigh(self, edge, new_triangle):
        edge = set(edge)
        for i, (triangle_edge, triangle) in enumerate(self.neighbours):
            if set(triangle_edge) == edge:
                self.neighbours[i][1] = new_triangle
                return

    # найти противоположную ребру точку в треугольнике
    def get_opposite(self, edge):
        for p in self.points():
            if p not in edge:
                return p

    # сделать треугольник из точек
    @staticmethod
    def make_from_points(p1, p2, p3, id=0):
        return Triangle([[(p1, p2), None],
                         [(p1, p3), None],
                         [(p2, p3), None]],
                        id)

    # площадь по формуле Герона
    @staticmethod
    def S(p1, p2, p3):
        a = abs(p1 - p2)
        b = abs(p1 - p3)
        c = abs(p2 - p3)
        p = (a + b + c) / 2
        return math.sqrt(p * (p - a) * (p - b) * (p - c))
