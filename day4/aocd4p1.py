with open("doc.txt") as doc:
    games = [game.strip().split(':')[1].split('|') for game in doc.readlines()]

    print(games)

doc.closed