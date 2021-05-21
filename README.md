# Delaunay-triangulation

Динамический алгоритм. Рисует изначально треугольник по трём точкам, а затем добавляет в него по точке из вользовательского ввода.

1. Поиск треугольника, в который попадает точка.
2. Вставка трёх новых треугольников, образованных точкой.
3. Добавление новых проблемных треугольников в очередь для возможного корректирования.
4. Пока очередь не пуста:
4. Достаём проблемный треугольник из очереди. Проверяем условие триангуляции для возможно проблемного ребра. В случае проблемы флипаем его и добавляем в очередь новые потенциально опасные треугольники.
