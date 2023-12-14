doc = open("games.txt")
import re
max_cubes = {
    'red':12,
    'blue':14,
    'green':13,
}

bad_game_total = 0
game_total = 0
sum_of_powers = 0

for game in doc:
    game_var,game_log = game.split(": ")
    garb, game_num = game_var.split(" ")
    attempts = re.split('; |, ', game_log)
    game_total = game_total + int(game_num)
    max_colors={
            'red':0,
            'blue':0,
            'green':0,
        }
    temp = 1
    for roll in attempts:
        print(roll)
        count, roll_color = roll.split(' ')
        roll_color = roll_color.strip()
        if int(count) > max_colors[roll_color]:
            max_colors[roll_color] = int(count)
            print(max_colors[roll_color])    
    
    print(max_colors)

    for color, num in max_colors.items():
        temp = int(temp * num)

    sum_of_powers = sum_of_powers + temp
        
print(f"sum_of_powers: {sum_of_powers}")