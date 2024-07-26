# Blackjack Game
# By Yang Yang

import random
import output

LIMIT = 21
DECK_OF_CARDS = {
  'AH': 'A ♥',
  '2H': '2 ♥',
  '3H': '3 ♥',
  '4H': '4 ♥',
  '5H': '5 ♥',
  '6H': '6 ♥',
  '7H': '7 ♥',
  '8H': '8 ♥',
  '9H': '9 ♥',
  'XH': '10 ♥',
  'JH': 'J ♥',
  'QH': 'Q ♥',
  'KH': 'K ♥',
  'AD': 'A ♦',
  '2D': '2 ♦',
  '3D': '3 ♦',
  '4D': '4 ♦',
  '5D': '5 ♦',
  '6D': '6 ♦',
  '7D': '7 ♦',
  '8D': '8 ♦',
  '9D': '9 ♦',
  'XD': '10 ♦',
  'JD': 'J ♦',
  'QD': 'Q ♦',
  'KD': 'K ♦',
  'AC': 'A ♣',
  '2C': '2 ♣',
  '3C': '3 ♣',
  '4C': '4 ♣',
  '5C': '5 ♣',
  '6C': '6 ♣',
  '7C': '7 ♣',
  '8C': '8 ♣',
  '9C': '9 ♣',
  'XC': '10 ♣',
  'JC': 'J ♣',
  'QC': 'Q ♣',
  'KC': 'K ♣',
  'AS': 'A ♠',
  '2S': '2 ♠',
  '3S': '3 ♠',
  '4S': '4 ♠',
  '5S': '5 ♠',
  '6S': '6 ♠',
  '7S': '7 ♠',
  '8S': '8 ♠',
  '9S': '9 ♠',
  'XS': '10 ♠',
  'JS': 'J ♠',
  'QS': 'Q ♠',
  'KS': 'K ♠'
}
VALUES_OF_CARDS = {
  'A': 1,
  '2': 2,
  '3': 3,
  '4': 4,
  '5': 5,
  '6': 6,
  '7': 7,
  '8': 8,
  '9': 9,
  'X': 10,
  'J': 10,
  'Q': 10,
  'K': 10
}

ACE = ['AH', 'AC', 'AS', 'AD']

# Global variable for deck of cards
deck = list(DECK_OF_CARDS.keys())

def instructions():
  print("""How to Play Blackjack
—————————————————————
Rules:
1) The goal of the game is to beat the dealer with a hand value of 21 or as close to 21 as possible without exceeding it.
2) The game is played with one or more decks of standard playing cards, and each card has a point value. It is up to each individual player if an ace is worth 1 or 11. Face cards are 10 and any other card is its card value.
3) Before the deal begins, the player places a bet. There are usually betting limits, but for this game, we won't add any.
3) The player is dealt two cards, and the dealer is dealt two cards, with one card face up and one card face down. 
4) The player can choose to "hit" and take additional cards to try and get closer to 21, or "stand" and keep their current hand. 
5) If the player exceeds 21, they lose the game, regardless of the dealer's hand. 
6) If the player has a hand value of 21, they have a "blackjack" and automatically win the game, unless the dealer also has a blackjack.
7) If the player chooses to stand, the dealer will reveal their face-down card and hit until they have at least 17 points. If the dealer exceeds 21, the player wins the game. 
8) If the dealer has a higher hand value than the player, the dealer wins.
9) If the player has a higher hand value than the dealer, the player wins. 
10) If the player and dealer have the same hand value, the game is a "push" and the player's bet is returned.

Cards:
- Number cards (2-10) are worth their face value.
- Face cards (Jack, Queen, King) are worth 10 points each.
- An Ace can be worth either 1 or 11 points, depending on which value would be more beneficial for the hand.

Extra:
Double Down:
In the game of blackjack, "doubling down" refers to the option for a player to double their initial bet in exchange for receiving exactly one more card from the dealer. Only possible if the original 2 cards dealt sum to a 9,10, or 11

Split:
If the user has two cards of the same value, they can “split” their hand, which means the 2 cards that were in their hand are treated as separate hands both belonging to the user. They have to double their bet in order to do this. 

Insurance:
"Insurance" is a side bet that a player can make when the dealer's up card is an Ace. The insurance bet pays 2-to-1 if the dealer has a blackjack an Ace as their face-up card.

Betting:
You will be asked to bet a certain number of coins before each hand. You can add "k" to the end of your bet to indicate you mean that many thousand coins. You can also type "all" and "max" to bet all your coins. You can type "half" to bet half of all your coins.

""")
  
  

def shuffle_deck():
  global deck
  deck = list(DECK_OF_CARDS.keys())
  randomize()


def randomize():
  global deck
  random.shuffle(deck)


def print_cards(cards_list: list):
  return_string = '\n'
  # top

  for i in range(len(cards_list)):
    return_string += '┌─────┐'
  return_string += '\n'
  #middle
  for i in range(len(cards_list)):
    return_string += '│     │'
  return_string += '\n'
  for i in cards_list:
    if i[0] == 'X':
      return_string += f'│{DECK_OF_CARDS[i]} │'
    else:
      return_string += f'│ {DECK_OF_CARDS[i]} │'
  return_string += '\n'
  #bottom
  for i in range(len(cards_list)):
    return_string += '│     │'
  return_string += '\n'
  for i in range(len(cards_list)):
    return_string += '└─────┘'
  return_string += '\n'
  total = 0
  ace_count = 0
  for i in cards_list:
    total += VALUES_OF_CARDS[i[0]]
    if i[0] == 'A':
      if total <= 11:
        total += 10
        ace_count += 1
      else:
        pass
    if total > 21:
      for e in cards_list:
        if e in ACE and ace_count > 0:
          total -= 10
          break
  return_string += f'Total: {total}'
  return return_string


def dealer_cards(cards: list):
  return_string = '\n'
  # top
  for i in range(len(cards)):
    return_string += '┌─────┐'
  return_string += '\n'
  #middle
  for i in range(len(cards)):
    return_string += '│     │'
  return_string += '\n'
  return_string += f'│  ?  │'
  if cards[1][0] == 'X':
    return_string += f'│{DECK_OF_CARDS[cards[1]]} │'
  else:
    return_string += f'│ {DECK_OF_CARDS[cards[1]]} │'
  return_string += '\n'
  #bottom
  for i in range(len(cards)):
    return_string += '│     │'
  return_string += '\n'
  for i in range(len(cards)):
    return_string += '└─────┘'
  return_string += '\n'
  return return_string


def insurance(bank: int,
              amount: int) -> int:  #amount is the original bet amount
  answers = ['y', 'n']
  answer = input('Would you like to make an insurance bet? (y/n) ')
  while answer not in answers:
    print('Invalid input.')
    answer = input('Would you like to make an insurance bet? (y/n) ')
  if answer == 'y':
    if (round(amount / 2)) > bank:
      print(
        f"You can't make an insurance bet of {round(amount/2)} because you only have {bank}."
      )
    else:
      decision = input(
        f"You're about to make an insurance bet of {round(amount/2)}. You have {bank} coins remaining, are you sure you want to do this? (y/n)"
      )
      while decision not in answers:
        print('Invalid input.')
        decision = input(
          f"You're about to make an insurance bet of {round(amount/2)}. You have {bank} coins remaining, are you sure you want to do this? (y/n)"
        )
      if decision == 'y':
        return bank - (round(amount / 2))
  return bank


def hit_or_stand(cards_list: list, dealer_hand: list):
  total = 0
  ace_count = 0
  for i in cards_list:
    total += VALUES_OF_CARDS[i[0]]
    if i[0] == 'A':
      if total <= 11:
        total += 10
        ace_count += 1
      else:
        pass
    if total > 21:
      for e in cards_list:
        if e in ACE and ace_count > 0:
          total -= 10
          break
  hit = True
  while (hit == True) and total < 21:
    action = input("Would you like to hit or stand? (h/s) ")
    while action not in ['h', 's']:
      print('Invalid input. Try again!')
      action = input("Would you like to hit or stand? (h/s) ")
    if action == "h":
      hit = True
      cards_list.append(deck.pop())
      #output.clear()
      print("Dealer's Hand:")
      print(dealer_cards(dealer_hand))
      print("Your Hand:")
      print(print_cards(cards_list))
    if action == "s":
      hit = False
    total = 0
    ace_count = 0
    for i in cards_list:
      total += VALUES_OF_CARDS[i[0]]
      if i[0] == 'A':
        if total <= 11:
          total += 10
          ace_count += 1
        else:
          pass
      if total > 21:
        for e in cards_list:
          if e in ACE and ace_count > 0:
            total -= 10
            break


def split(
  player_hand, dealer_hand, amount, bank
):  # make it so that you hit or stand both your hands before the dealer gets more cards
  for i in range(2):
    player_new_hand = [player_hand[i], deck.pop()]
    dealer_new_hand = [dealer_hand[0], dealer_hand[1]]
    print(f"\nHand #{i+1}")
    print("\nDealer's Hand:")
    print(dealer_cards(dealer_new_hand))
    print('\nYour Hand:')
    print(print_cards(player_new_hand))
    hit_or_stand(player_new_hand, dealer_new_hand)
    player_total = 0
    ace_count = 0
    for i in player_hand:
      player_total += VALUES_OF_CARDS[i[0]]
      if i[0] == 'A':
        if player_total <= 11:
          player_total += 10
          ace_count += 1
        else:
          pass
      if player_total > 21:
        for e in player_hand:
          if e in ACE and ace_count > 0:
            player_total -= 10
    dealer_total = 0
    ace_count = 0
    for i in dealer_hand:
      dealer_total += VALUES_OF_CARDS[i[0]]
      if i[0] == 'A':
        if dealer_total <= 11:
          dealer_total += 10
          ace_count += 1
        else:
          pass
      if dealer_total > 21:
        for e in dealer_hand:
          if e in ACE and ace_count > 0:
            dealer_total -= 10
            break
    if dealer_total >= 17:
      print("\nDealer's Hand:")
      print(print_cards(dealer_new_hand))
      print('\nYour Hand:')
      print(print_cards(player_new_hand))
    while dealer_total < 17:
      dealer_new_hand.append(deck.pop())
      print("\nDealer's Hand:")
      print(print_cards(dealer_new_hand))
      print('\nYour Hand:')
      print(print_cards(player_new_hand))
      dealer_total = 0
      ace_count = 0
      for i in dealer_new_hand:
        dealer_total += VALUES_OF_CARDS[i[0]]
        if i[0] == 'A':
          if dealer_total <= 11:
            dealer_total += 10
            ace_count += 1
          else:
            pass
        if dealer_total > 21:
          for e in dealer_new_hand:
            if e in ACE and ace_count > 0:
              dealer_total -= 10
              break
    if player_total > 21:
      print(f"You busted (hand over 21). You have {bank} coins.")
    elif dealer_total > 21:
      bank += amount * 2
      print(
        f"The dealer busted. You won {amount} coins! You have {bank} coins.")
    elif player_total == dealer_total:
      bank += amount
      print(f"You push with the dealer. You have {bank} coins.")
    elif player_total < dealer_total:
      print(f"You lost to the dealer. You have {bank} coins.")
    elif player_total > dealer_total:
      bank += amount * 2
      print(
        f"You beat the dealer. You won {amount} coins! You have {bank} coins.")
  return bank


def yes_or_no(question: str) -> bool:
  answers = ['y', 'n']
  answer = input(f"{question} (y/n) ")  #there's something wrong with this line
  if answer not in answers:
    print('Invalid input. Try again.')
    answer = input(f"{question} (y/n) ")
  if answer == 'y':
    return True
  elif answer == 'n':
    return False

def double_down(player_hand, dealer_hand, amount, bank):
  player_hand.append(deck.pop())
  player_total = 0
  ace_count = 0
  for i in player_hand:
    player_total += VALUES_OF_CARDS[i[0]]
    if i[0] == 'A':
      if player_total <= 11:
        player_total += 10
        ace_count += 1
      else:
        pass
    if player_total > 21:
      for e in player_hand:
        if e in ACE and ace_count > 0:
          player_total -= 10

  dealer_total = 0
  ace_count = 0
  for i in dealer_hand:
    dealer_total += VALUES_OF_CARDS[i[0]]
    if i[0] == 'A':
      if dealer_total <= 11:
        dealer_total += 10
        ace_count += 1
      else:
        pass
    if dealer_total > 21:
      for e in dealer_hand:
        if e in ACE and ace_count > 0:
          dealer_total -= 10
          break
  if dealer_total >= 17:
    print("\nDealer's Hand:")
    print(print_cards(dealer_hand))
    print('\nYour Hand:')
    print(print_cards(player_hand))
  while dealer_total < 17:
    dealer_hand.append(deck.pop())
    print("\nDealer's Hand:")
    print(print_cards(dealer_hand))
    print('\nYour Hand:')
    print(print_cards(player_hand))
    dealer_total = 0
    ace_count = 0
    for i in dealer_hand:
      dealer_total += VALUES_OF_CARDS[i[0]]
      if i[0] == 'A':
        if dealer_total <= 11:
          dealer_total += 10
          ace_count += 1
        else:
          pass
      if dealer_total > 21:
        for e in dealer_hand:
          if e in ACE and ace_count > 0:
            dealer_total -= 10
            break
  if player_total > 21:
    print(f"You busted (hand over 21). You have {bank} coins.")
  elif dealer_total > 21:
    bank += amount * 4
    print(
      f"The dealer busted. You won {amount*2} coins! You have {bank} coins.")
  elif player_total == dealer_total:
    bank += amount * 4
    print(f"You push with the dealer. You have {bank} coins.")
  elif player_total < dealer_total:
    print(f"You lost to the dealer. You have {bank} coins.")
  elif player_total > dealer_total:
    bank += amount * 4 
    print(
      f"You beat the dealer. You won {amount*2} coins! You have {bank} coins.")
  return bank

  
def reset_game():
  global bank, deck
  bank = 1000
  deck = list(DECK_OF_CARDS.keys())
  randomize()


def main():
  shuffle_deck()
  bank = 1000
  play = True
  while play and bank > 0:
    print(f'You have {bank} coins in your bank.')
    invalid = True
    while invalid:
      try:
        amount = input('How many coins would you like to bet? ')
        if amount[-1] == 'k':
          amount = float(amount[0:-1]) * 1000
          round(amount, 3)
          invalid = False
        elif amount == "max" or amount == "all":
          amount = bank
          invalid = False
        elif amount == "half":
          amount = round(bank/2)
          invalid = False
        amount = int(amount)
        if amount < 0:
          print("You can't bet negative coins.")
          invalid = True
        elif amount == 0:
          print("You can't bet 0 coins.")
          invalid = True
        elif amount > bank:
          print("You can't bet more coins than you have.")
          invalid = True
        else:
          invalid = False
      except:
        print('Invalid input, try again.')
    bank -= amount
    dealer_hand = [deck.pop(), deck.pop()]
    print("\nDealer's Hand:")
    print(dealer_cards(dealer_hand))
    if dealer_hand[1][0] == 'A':
      bank = insurance(bank, amount)
    print('\nYour Hand:')
    player_hand = [deck.pop(), deck.pop()]
    print(print_cards(player_hand))
    player_total = 0
    ace_count = 0
    for i in player_hand:
      player_total += VALUES_OF_CARDS[i[0]]
      if i[0] == 'A':
        if player_total <= 11:
          player_total += 10
          ace_count += 1
        else:
          pass
      if player_total > 21:
        for e in player_hand:
          if e in ACE and ace_count > 0:
            player_total -= 10

    dealer_total = 0
    ace_count = 0
    for i in dealer_hand:
      dealer_total += VALUES_OF_CARDS[i[0]]
      if i[0] == 'A':
        if dealer_total <= 11:
          dealer_total += 10
          ace_count += 1
        else:
          pass
      if dealer_total > 21:
        for e in dealer_hand:
          if e in ACE and ace_count > 0:
            dealer_total -= 10
            break
    if player_total == 21:
      bank += round(amount * 2.5)
      print("\nDealer's Hand:")
      print(print_cards(dealer_hand))
      print('\nYour Hand:')
      print(print_cards(player_hand))
      print(
        f"You beat the dealer with a blackjack. You won {round(amount*1.5)} coins! You have {bank} coins."
      )
    else:
      if (
          VALUES_OF_CARDS[player_hand[0][0]]
          == VALUES_OF_CARDS[player_hand[1][0]]
      ) and (bank - amount >= 0) and yes_or_no(
          'Would you like to split?'
      ):  #this checks if the cards are the same value and if you have enough money to split
        bank -= amount
        bank = split(player_hand, dealer_hand, amount, bank)
      elif player_total in [9, 10, 11] and (bank - amount >= 0) and yes_or_no('Would you like to double down?'):
        bank -= amount
        bank = double_down(player_hand, dealer_hand, amount, bank)
      else:
        hit_or_stand(player_hand, dealer_hand)
        dealer_total = 0
        player_total = 0
        for i in dealer_hand:
          dealer_total += VALUES_OF_CARDS[i[0]]
        for i in player_hand:
          player_total += VALUES_OF_CARDS[i[0]]
        if dealer_total >= 17:
          print("\nDealer's Hand:")
          print(print_cards(dealer_hand))
          print('\nYour Hand:')
          print(print_cards(player_hand))
        if dealer_total >= 17:
          print("\nDealer's Hand:")
          print(print_cards(dealer_hand))
          print('\nYour Hand:')
          print(print_cards(player_hand))
        while dealer_total < 17:
          dealer_hand.append(deck.pop())
          print("\nDealer's Hand:")
          print(print_cards(dealer_hand))
          print('\nYour Hand:')
          print(print_cards(player_hand))
          dealer_total = 0
          ace_count = 0
          for i in dealer_hand:
            dealer_total += VALUES_OF_CARDS[i[0]]
            if i[0] == 'A':
              if dealer_total <= 11:
                dealer_total += 10
                ace_count += 1
              else:
                pass
            if dealer_total > 21:
              for e in dealer_hand:
                if e in ACE and ace_count > 0:
                  dealer_total -= 10
                  break
        if player_total > 21:
          print(f"You busted (hand over 21). You have {bank} coins.")
        elif dealer_total > 21:
          bank += amount * 2
          print(
            f"The dealer busted. You won {amount} coins! You have {bank} coins."
          )
        elif player_total == dealer_total:
          bank += amount
          print(f"You push with the dealer. You have {bank} coins.")
        elif player_total < dealer_total:
          print(f"You lost to the dealer. You have {bank} coins.")
        elif player_total > dealer_total:
          bank += amount * 2
          print(
            f"You beat the dealer. You won {amount} coins! You have {bank} coins."
          )
    # Restarting the game:
    if bank > 0:
      if yes_or_no("Do you want to continue playing?"):
        if len(deck) < 20:
          shuffle_deck()
      else:
        play = False
    if bank <= 0:
      print('You lost all your coins!')
      if yes_or_no("Do you want to play again?"):
        bank = 1000
        shuffle_deck()
      else:
        play = False


main()
