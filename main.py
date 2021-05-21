from delaunay import *


# обработка ввода треугольника в комплексные точки
def get_triangle():
    s = input().split(';')
    points = []
    for p in s:
        x, y = map(int, p.split())
        points.append(complex(x, y))
    return points


# обработка ввода точки в комплексную точку
def get_point():
    s = input()
    if not s:
        return
    return complex(*map(int, s.split()))


print("Введите граничный треугольник (внутри которого будет строиться триангуляция).")
print("Введите координаты трёх точек через ';' в формате: a b; c d; e f")
print("Например: 0 0; 1000 0; 500 866")
start_points = get_triangle()
delaunay = Delaunay(start_points)
delaunay.plot()
while True:
    print("\nВводите координаты новых точек через пробел в формате: a, b")
    print("Можно вводить только те точки, которые помещаются в начальный треугольник")
    print("Например: 10 10")
    print("Для выхода в любой момент нажмите Enter.")
    point = get_point()
    if not point:
        break
    delaunay.add_point(point)
    delaunay.plot()
