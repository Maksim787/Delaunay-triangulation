from circle import Circle
from triangle import Triangle
from collections import deque
import matplotlib.pyplot as plt


class Delaunay:
    def __init__(self, points):
        # список треугольников
        self.triangles_list = [Triangle.make_from_points(*points)]

    def add_point(self, p):
        # получаем новые образованные рёбра и треугольники в виде очереди
        flip_list = self.make_triangles(p)
        # флипаем некоторые рёбра, добавляем их соседей в очередь
        while flip_list:
            t1, e = flip_list.popleft()
            if t1 is None:
                continue
            t2 = t1.get_neigh(e)
            if t2 is None:
                continue
            p1, p2 = e
            p3 = t1.get_opposite(e)
            p4 = t2.get_opposite(e)
            # получаем окружность по трём точкам
            circle = Circle.get_circle(p1, p2, p3)
            # если четвертая точка в окружности, то делаем флип
            if Circle.is_in_circle(circle, p4):
                id1 = t1.id
                id2 = t2.id
                e13 = (p1, p3)
                e14 = (p1, p4)
                e23 = (p2, p3)
                e24 = (p2, p4)
                e34 = (p3, p4)

                t13 = t1.get_neigh(e13)
                t23 = t1.get_neigh(e23)
                t14 = t2.get_neigh(e14)
                t24 = t2.get_neigh(e24)

                t1_new = Triangle([[e13, t13],
                                   [e14, t14],
                                   [e34, None]],
                                  id1)
                t2_new = Triangle([[e23, t23],
                                   [e24, t24],
                                   [e34, t1_new]],
                                  id2)
                t1_new.set_neigh(e34, t2_new)

                # заменяем старые треугольники на новые
                self.triangles_list[id1] = t1_new
                self.triangles_list[id2] = t2_new

                if t13 is not None:
                    t13.set_neigh(e13, t1_new)
                if t14 is not None:
                    t14.set_neigh(e14, t1_new)
                if t23 is not None:
                    t23.set_neigh(e23, t2_new)
                if t24 is not None:
                    t24.set_neigh(e24, t2_new)
                # добавляем новые потенциально опасные ребра в виде пар [треугольник, проблемное ребро]
                flip_list.append([t14, e14])
                flip_list.append([t24, e24])
                flip_list.append([t13, e13])
                flip_list.append([t23, e23])

    def make_triangles(self, p):
        # ищем треугольник для вставки внутрь него точки
        for index in range(len(self.triangles_list)):
            if self.triangles_list[index].is_point_in(p):
                insert_index = index
                break
        else:
            print("Точка должна лежать по крайней мере в одном из треугольников.")
            return None
        # треугольник, в который вставляем точку
        insert_triangle = self.triangles_list[insert_index]

        # создаём 3 новых треугольника
        p1, p2, p3 = insert_triangle.points()

        e1 = (p1, p2)
        e2 = (p2, p3)
        e3 = (p1, p3)

        e4 = (p1, p)
        e5 = (p2, p)
        e6 = (p3, p)

        t1 = insert_triangle.get_neigh(e1)
        t2 = insert_triangle.get_neigh(e2)
        t3 = insert_triangle.get_neigh(e3)

        new_t1 = Triangle([[e1, t1],
                           [e4, None],
                           [e5, None]],
                          insert_index)
        new_t2 = Triangle([[e2, t2],
                           [e5, new_t1],
                           [e6, None]],
                          len(self.triangles_list))
        new_t3 = Triangle([[e3, t3],
                           [e4, new_t1],
                           [e6, new_t2]],
                          len(self.triangles_list) + 1)

        new_t1.set_neigh(e5, new_t2)
        new_t1.set_neigh(e4, new_t3)
        new_t2.set_neigh(e6, new_t3)

        # обновляем соседей треугольника, в который вставили точку
        if t1 is not None:
            t1.set_neigh(e1, new_t1)
        if t2 is not None:
            t2.set_neigh(e2, new_t2)
        if t3 is not None:
            t3.set_neigh(e3, new_t3)

        # заменяем старый треугольник и добавляем новые
        self.triangles_list[insert_index] = new_t1
        self.triangles_list.append(new_t2)
        self.triangles_list.append(new_t3)

        # рёбра для возможного flip - пары [треугольник, проблемное ребро]
        return deque([[new_t1, e1], [new_t2, e2], [new_t3, e3]])

    # отрисовка триангуляции
    def plot(self):
        for triangle in self.triangles_list:
            for edge, triangle_neigh in triangle.neighbours:
                plt.plot([edge[0].real, edge[1].real],
                         [edge[0].imag, edge[1].imag])
        plt.axis('equal')
        plt.show()
