import os


class Renderer:
    """
    Класс для отрисовки графики и анимации в консоли.
    """

    def clear(self):

        """
        Очищает экран консоли.
        """

        os.system('cls' if os.name == 'nt' else 'clear')

    def draw(self, grid, p_pos, t_pos, level, frame):

        """
        Рисует карту с анимированным флажком на выходе.
        """

        self.clear()
        h, w = len(grid), len(grid[0])

        # Анимация финиша: чередуем два символа
        target_icon = "🏁"

        print(f"--- УРОВЕНЬ {level} ---")
        print(f"Игрок: ☺  Цель: {target_icon} (Стены УБИВАЮТ!)\n")

        for y in range(h):
            top = ""
            for x in range(w):
                top += "╬" + ("═══" if grid[y][x].walls['top'] else "   ")
            print(top + "╬")

            mid = ""
            for x in range(w):
                wall = "║" if grid[y][x].walls['left'] else " "
                if (x, y) == p_pos:
                    char = " ☺ "
                elif (x, y) == t_pos:
                    char = f" {target_icon}"
                else:
                    char = "   "
                mid += wall + char
            print(mid + "║")

        print("╬" + "═══╬" * w)
