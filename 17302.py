class BababukGame:
    def __init__(self, map: list[list[str]]):
        self.map = map
        self.n = len(map)
        self.m = len(map[0])

    def get_action_map(self) -> None:
        action_map = [[0 for _ in range(self.m)] for _ in range(self.n)]

        for i in range(self.n):
            for j in range(self.m):

                change_count = 0

                if i - 1 >= 0:
                    change_count += 1
                if i + 1 < self.n:
                    change_count += 1
                if j - 1 >= 0:
                    change_count += 1
                if j + 1 < self.m:
                    change_count += 1

                if change_count % 2 == 0:
                    if self.map[i][j] == "W":
                        action_map[i][j] = 2
                    else:
                        action_map[i][j] = 3
                else:
                    if self.map[i][j] == "W":
                        action_map[i][j] = 3
                    else:
                        action_map[i][j] = 2

        return action_map


N, M = map(int, input().split())
input_map = [list(input()) for _ in range(N)]

game = BababukGame(input_map)
action_map = game.get_action_map()

print(1)
for i in range(N):
    for j in range(M):
        print(action_map[i][j], end="")
    print()
