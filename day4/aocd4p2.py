with open("doc.txt") as doc:
     

    games = [game.strip().split(':')[1].split('|') for game in doc.readlines()]

    copies_of_cards = {}
    total = {}
    inc = 1

    final_total = 0

    for game in games:
        game[0] = game[0].strip().split()
        game[1] = game[1].strip().split()
    
    for idx,game in enumerate(games):
        game_number = idx+1
        cards_won = []
        win = 0
        for x in game[1]:
            if x in game[0]:
                win += 1
        
        for x in range(win):
            cards_won.append(idx+x+2)

        copies_of_cards.update({f"{game_number}" : {'will win': cards_won, 'copies' :1}})
    
    #print(copies_of_cards)

    for key, value in copies_of_cards.items():

        for copy in range(value['copies']): 
            for next_game in value['will win']:
                copies_of_cards[f'{next_game}']['copies'] +=1
                #print(copy)

                pass

    print(copies_of_cards)

    for copies in copies_of_cards.values():
        final_total += int(copies['copies'])
    print(final_total)



doc.closed