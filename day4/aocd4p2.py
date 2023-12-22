with open("doc.txt") as doc:
     

    games = [game.strip().split(':')[1].split('|') for game in doc.readlines()]

    copies_of_cards = {}
  
    
    total = 0

    for game in games:
        game[0] = game[0].strip().split()
        game[1] = game[1].strip().split()
        #print(winning_nums)
        #print(current_nums)
        #print(win)
        #print(total)
    
    for idx,game in enumerate(games):
        game_number = idx+1
        cards_won = []
        #print(idx)
        win = 0
        for x in game[1]:
            if x in game[0]:
                #print(x)
                win += 1
        for x in range(win):
            cards_won.append(idx+x+2)
        
            #print(x)
        copies_of_cards.update({f"{game_number}":cards_won})
        print(win)
        
        print(copies_of_cards)
        print(len(copies_of_cards))
        


doc.closed