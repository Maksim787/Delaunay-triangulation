import math


class Utility:
    @staticmethod
    def get_circle(p1, p2, p3):
        a = abs(p1 - p2)
        b = abs(p2 - p3)
        c = abs(p3 - p1)

        alpha = math.acos((a ** 2 + b ** 2 - c ** 2) / (2 * a * b))

        # Радиус окружности
        R = c / math.sin(alpha) / 2

        # half_c - вектор, половина a
        half_c = (p3 - p1) / 2
        # print(half_c)

        # ser_per - серединный перпендикуляр единичной длины
        ser_per = half_c * 1j / abs(half_c)

        # удлиняем его ровно до центра окружности
        ser_per *= (R ** 2 - abs(half_c) ** 2) ** 0.5
        # print(ser_per)

        # r_vector - радиус из точки p1
        # Если alpha < pi/2, он смотрит в направлении точки p2, иначе в другом направлении
        if alpha < math.pi / 2:
            sign = 1
        else:
            sign = -1
        if abs(p1 + half_c + ser_per - p2) * sign < abs(p1 + half_c - ser_per - p2) * sign:
            r_vector = half_c + ser_per
        else:
            r_vector = half_c - ser_per
        circle_center = p1 + r_vector
        return [circle_center, R]

    @staticmethod
    def is_in_circle(circle, p):
        return abs(p - circle[0]) < circle[1]
