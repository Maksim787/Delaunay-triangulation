import math


# все точки представлены в виде комплексного числа x + iy
class Circle:
    # получить окружность по трём точкам
    @staticmethod
    def get_circle(p1, p2, p3):
        # сороны треугольника на точках
        a = abs(p1 - p2)
        b = abs(p2 - p3)
        c = abs(p3 - p1)

        # угол напротив стороны c по т. косинусов
        alpha = math.acos((a ** 2 + b ** 2 - c ** 2) / (2 * a * b))

        # радиус окружности по т. синусов
        R = c / math.sin(alpha) / 2

        # half_c - вектор, половина c
        half_c = (p3 - p1) / 2

        # ser_per - серединный перпендикуляр к c единичной длины
        ser_per = half_c * 1j / abs(half_c)

        # удлиняем ser_per ровно до центра окружности (это расстояние выражено по теореме Пифагора)
        ser_per *= (R ** 2 - abs(half_c) ** 2) ** 0.5

        # r_vector - радиус описанной окружности треугольника из точки p1
        # Если alpha < pi/2, он смотрит в направлении точки p2, иначе в другом направлении
        if alpha < math.pi / 2:
            sign = 1
        else:
            sign = -1
        if abs(p1 + half_c + ser_per - p2) * sign < abs(p1 + half_c - ser_per - p2) * sign:
            r_vector = half_c + ser_per
        else:
            r_vector = half_c - ser_per
        # центр окружности = точка p1 + радиус описанной окружности из точки p1
        circle_center = p1 + r_vector
        # пара (центр окружности, радиус)
        return circle_center, R

    # проверка на принадлежность точка кругу
    @staticmethod
    def is_in_circle(circle, p):
        return abs(p - circle[0]) < circle[1]
