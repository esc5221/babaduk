import random


class BababukGame:
    def __init__(self, map: list[list[int]]):
        self.map = map
        self.map_size = len(map)

    def action_1(self, x: int, y: int) -> None:
        """
        invert the value of the l, r, u, d cells
        """

        if x - 1 >= 0:
            self.map[x - 1][y] = 1 - self.map[x - 1][y]

        if x + 1 < self.map_size:
            self.map[x + 1][y] = 1 - self.map[x + 1][y]

        if y - 1 >= 0:
            self.map[x][y - 1] = 1 - self.map[x][y - 1]

        if y + 1 < self.map_size:
            self.map[x][y + 1] = 1 - self.map[x][y + 1]

    def action_2(self, x: int, y: int) -> None:
        """
        invert the value of the l, r, u, d cells and the cell itself
        """

        self.action_1(x, y)

        self.map[x][y] = 1 - self.map[x][y]

    def action_3(self, x: int, y: int) -> None:
        """
        Do nothing
        """
        pass

    def solve(self) -> None:

        original_map = [
            [self.map[i][j] for j in range(self.map_size)] for i in range(self.map_size)
        ]

        change_count_map = [
            [0 for _ in range(self.map_size)] for _ in range(self.map_size)
        ]

        for i in range(self.map_size):
            for j in range(self.map_size):
                # corner
                if (
                    (i, j) == (0, 0)
                    or (i, j) == (0, self.map_size - 1)
                    or (i, j) == (self.map_size - 1, 0)
                    or (i, j) == (self.map_size - 1, self.map_size - 1)
                ):
                    change_count_map[i][j] = 2

                # edge
                elif (
                    (i == 0 or i == self.map_size - 1)
                    and (j != 0 and j != self.map_size - 1)
                ) or (
                    (j == 0 or j == self.map_size - 1)
                    and (i != 0 and i != self.map_size - 1)
                ):
                    change_count_map[i][j] = 3

                # middle
                else:
                    change_count_map[i][j] = 4

        for i in range(self.map_size):
            for j in range(self.map_size):
                if change_count_map[i][j] % 2 == 0:
                    if original_map[i][j] == 0:
                        self.action_1(i, j)
                    else:
                        self.action_2(i, j)
                else:
                    if original_map[i][j] == 0:
                        self.action_2(i, j)
                    else:
                        self.action_1(i, j)


def random_map(size: int) -> list[list[int]]:
    """
    Generates a random map of the given size
    """
    return [[random.randint(0, 1) for _ in range(size)] for _ in range(size)]


def print_map(map: list[list[int]]) -> None:
    """
    Prints the map to the console
    """
    for row in map:
        print(row)


def main():
    map = random_map(10)

    game = BababukGame(map)

    print("=== original game ===")
    print_map(game.map)

    game.solve()

    print()
    print("=== solved game ===")
    print_map(game.map)


if __name__ == "__main__":
    main()
