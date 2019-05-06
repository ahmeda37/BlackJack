import helpers 

while True:
    # Print an opening statement
    print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
    Dealer hits until she reaches 17. Aces count as 1 or 11.')
    
    # Create & shuffle the deck, deal two cards to each player
    deck = helpers.Deck()
    deck.shuffle()
    
    player_hand = helpers.Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    dealer_hand = helpers.Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
            
    # Set up the Player's chips
    player_chips = helpers.Chips()  # remember the default value is 100    
    
    # Prompt the Player for their bet
    helpers.take_bet(player_chips)
    
    # Show cards (but keep one dealer card hidden)
    helpers.show_some(player_hand,dealer_hand)
    
    while helpers.playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        helpers.hit_or_stand(deck,player_hand) 
        
        # Show cards (but keep one dealer card hidden)
        helpers.show_some(player_hand,dealer_hand)  
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            helpers.player_busts(player_hand,dealer_hand,player_chips)
            break        


    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17 
    if player_hand.value <= 21:
        
        while dealer_hand.value < 17:
            helpers.hit(deck,dealer_hand)    
    
        # Show all cards
        helpers.show_all(player_hand,dealer_hand)
        
        # Run different winning scenarios
        if dealer_hand.value > 21:
            helpers.dealer_busts(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value > player_hand.value:
            helpers.dealer_wins(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value < player_hand.value:
            helpers.player_wins(player_hand,dealer_hand,player_chips)

        else:
            helpers.push(player_hand,dealer_hand)        
    
    # Inform Player of their chips total 
    print("\nPlayer's winnings stand at",player_chips.total)
    
    # Ask to play again
    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")
    
    if new_game[0].lower()=='y':
        helpers.playing=True
        continue
    else:
        print("Thanks for playing!")
        break