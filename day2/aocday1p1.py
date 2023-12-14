doc = open("games.txt")
import re
max_cubes = {
    'red':12,
    'blue':14,
    'green':13,
}

bad_game_total = 0
game_total = 0

for game in doc:
    game_var,game_log = game.split(": ")
    garb, game_num = game_var.split(" ")
    attempts = re.split('; |, ', game_log)
    game_total = game_total + int(game_num)
    for roll in attempts:
        count, roll_color = roll.split(' ')
        for color,max_roll in max_cubes.items():
            if roll_color == color and int(count) > max_roll:
                bad_game_total = bad_game_total + int(game_num)
                break
            else:
                pass     
        else:
            continue
        break   
print(f"bad: {bad_game_total}")       
print(f"good: {game_total-bad_game_total}") 
print(f"total: {game_total}") 