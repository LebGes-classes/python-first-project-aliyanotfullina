import random
from cell import Cell


class MazeGenerator:
    """
    Класс для автоматической генерации лабиринта.
    """

    def generate(self, width, height):

        """
        Мгновенно строит сетку лабиринта и прокладывает пути.
        """

        grid = [[Cell(x, y) for x in range(width)] for y in range(height)]
        stack = []
        visited = set()

        # Начинаем генерацию со случайной клетки
        start_x = random.randint(0, width - 1)
        start_y = random.randint(0, height - 1)
        current = grid[start_y][start_x]

        visited.add((current.x, current.y))

        while len(visited) < (width * height):
            neighbors = self._get_neighbors(current, grid, visited, width, height)
            if neighbors:
                next_cell = random.choice(neighbors)
                self._remove_walls(current, next_cell)
                stack.append(current)
                current = next_cell
                visited.add((current.x, current.y))
            elif stack:
                current = stack.pop()
        return grid

    def _get_neighbors(self, cell, grid, visited, w, h):

        """
        Ищет соседей, координаты которых еще не в списке посещенных.
        """

        ns = []
        directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        for dx, dy in directions:
            nx, ny = cell.x + dx, cell.y + dy
            if 0 <= nx < w and 0 <= ny < h and (nx, ny) not in visited:
                ns.append(grid[ny][nx])
        return ns

    def _remove_walls(self, c1, c2):

        """
        Убирает общую стену между двумя ячейками.
        """

        dx, dy = c1.x - c2.x, c1.y - c2.y
        if dx == 1:
            c1.walls['left'] = c2.walls['right'] = False
        elif dx == -1:
            c1.walls['right'] = c2.walls['left'] = False
        if dy == 1:
            c1.walls['top'] = c2.walls['bottom'] = False
        elif dy == -1:
            c1.walls['bottom'] = c2.walls['top'] = False
