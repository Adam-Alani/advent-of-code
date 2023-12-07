with open("day02") as f:
    lines = f.readlines()
lines = [x.strip() for x in lines]

games = []
for line in lines:
    game = {}
    line = line.split(": ")[1]
    for i,game_part in enumerate(line.split("; ")):
        game_part = game_part.strip()
        game_balls = [ball.split(" ") for ball in game_part.split(", ")]
        colors, numbers = zip(*[(color, int(number)) for number, color in game_balls])
        for color, number in zip(colors, numbers):
            if color not in game:
                game[color] = number
            else:
                game[color] = max(game[color], number)
    games.append(game)

sum = 0
for i,game in enumerate(games):
    power = 1
    for color in ["red", "green", "blue"]:
        color_value = game[color]
        power *= color_value
    sum += power
print(sum)

