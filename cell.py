class Cell:
    """
    Класс-контейнер для данных ячейки.

    Хранит координаты и состояние четырех стен (True - стена стоит).
    """

    def __init__(self, x, y):
        """
        Инициализация координат и начальных стен.
        """

        self.x = x
        self.y = y
        self.walls = {
            'top': True,
            'right': True,
            'bottom': True,
            'left': True
        }
