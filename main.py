import random
import time
from generator import MazeGenerator
from renderer import Renderer


class MazeGame:
    """
    Главный управляющий класс игры.
    """

    def __init__(self):

        """
        Начальные настройки игры на 2025 год.
        """

        self.level = 1
        self.width = 5
        self.height = 3
        self.frame_counter = 0
        # Создаем экземпляры вспомогательных классов
        self.generator = MazeGenerator()
        self.renderer = Renderer()

    def start(self):

        """
        Запуск главного меню.
        """

        self.renderer.clear()
        print("╔══════════════════════════════╗")
        print(" ║           ЛАБИРИНТ           ║")
        print(" ╚══════════════════════════════╝")
        print("  1. Начать приключение")
        print("  2. Выйти")

        choice = input("\n  Выбор: ")
        if choice == '1':
            self._main_loop()

    def _get_random_positions(self):

        """
        Генерирует случайные точки старта и конца.
        """

        start = (random.randint(0, 1), random.randint(0, self.height - 1))
        finish = (random.randint(self.width - 2, self.width - 1),
                  random.randint(0, self.height - 1))
        return start, finish

    def _main_loop(self):

        """
        Бесконечный цикл уровней.
        """

        game_active = True
        while game_active:
            grid = self.generator.generate(self.width, self.height)
            s_pos, f_pos = self._get_random_positions()
            px, py = s_pos

            level_running = True
            while level_running:
                self.frame_counter += 1
                self.renderer.draw(grid, (px, py), f_pos, self.level, self.frame_counter)

                cmd = input("\n  Ход (WASD): ").lower()
                if cmd == 'q':
                    game_active = False
                    break
                if not cmd or cmd not in 'wasd':
                    continue

                cell = grid[py][px]
                is_dead = False

                # Проверка столкновения со стеной (смерть)
                if cmd == 'w':
                    if cell.walls['top']:
                        is_dead = True
                    else:
                        py -= 1
                elif cmd == 's':
                    if cell.walls['bottom']:
                        is_dead = True
                    else:
                        py += 1
                elif cmd == 'a':
                    if cell.walls['left']:
                        is_dead = True
                    else:
                        px -= 1
                elif cmd == 'd':
                    if cell.walls['right']:
                        is_dead = True
                    else:
                        px += 1

                if is_dead:
                    self.renderer.clear()
                    print("\n" * 3 + "Вы врезались в стену!")
                    print(f"   ИГРА ОКОНЧЕНА. Уровень: {self.level}")
                    time.sleep(2.5)
                    level_running = False
                    game_active = False

                elif (px, py) == f_pos:
                    print(f"🎉 ПОБЕДА! УРОВЕНЬ {self.level} ПРОЙДЕН!")
                    time.sleep(1.5)
                    self.level += 1
                    self.width += 2
                    self.height += 1
                    level_running = False


if __name__ == "__main__":
    game = MazeGame()
    game.start()
