with open("doc.txt") as doc:
    games = [game.strip().split(':')[1].split('|') for game in doc.readlines()]

    print(games)
    total = 0

    for game in games:
        winning_nums = game[0].strip().split()
        current_nums = game[1].strip().split()
        #print(winning_nums)
        #print(current_nums)
        win = -1
        for x in current_nums:
            if x in winning_nums:
                print(x)
                win += 1

        if win != -1:
            total += 2 ** (win)
        print(win)
        print(total)

doc.closed