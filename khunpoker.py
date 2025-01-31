import random

CARDS = ['K', 'Q', 'J']
RANK = {'K': 3, 'Q': 2, 'J': 1}

def deal_cards():
    """Deal two different cards to player and bot."""
    cards = CARDS.copy()
    random.shuffle(cards)
    return cards[0], cards[1]

def determine_winner(player_card, bot_card):
    """Return the winner based on card ranks."""
    if RANK[player_card] > RANK[bot_card]:
        return 'player'
    return 'bot'

def bot_action(bot_card, history):
    """Return the bot's action based on its card and the history."""
    if history == "":
        return 'bet' if bot_card == 'K' else ('check' if bot_card == 'J' else random.choice(['check', 'bet']))
    if history == "check":
        return 'bet' if bot_card == 'K' else ('check' if bot_card == 'J' else random.choice(['check', 'bet']))
    if history == "bet":
        return 'call' if bot_card == 'K' else ('fold' if bot_card == 'J' else random.choice(['call', 'fold']))
    if history == "checkbet":
        return 'call' if bot_card == 'K' else ('fold' if bot_card == 'J' else random.choice(['call', 'fold']))
    return 'check'

def update_pot_and_stacks(winner, pot, player_stack, bot_stack):
    """Update the stacks based on the winner of the hand."""
    if winner == 'player':
        player_stack += pot
    else:
        bot_stack += pot
    return player_stack, bot_stack

def handle_forced_check_check(player_card, bot_card, pot, player_stack, bot_stack):
    """Automatically check-check if a player has no chips left after ante."""
    if player_stack == 0 or bot_stack == 0:
        winner = determine_winner(player_card, bot_card)
        if player_stack > bot_stack:
            print("Bot is forced to ALLIN")
        else:
            print("Player is forced to ALLIN")
        print(f"\nYour card: {player_card}, Bot's card: {bot_card}")
        print(f"{winner.capitalize()} wins the pot!")
        return update_pot_and_stacks(winner, pot, player_stack, bot_stack)
    return None  # Normal game flow should continue

def play_kuhn_poker():
    """Main game loop for playing Kuhn Poker."""
    global player_stack, bot_stack, first_to_act

    while True:
        if player_stack <= 0:
            print("\nYou're out of chips! Game over.")
            break
        if bot_stack <= 0:
            print("\nBot is out of chips! You win!")
            break

        # Deal cards
        player_card, bot_card = deal_cards()
        print(f"\nYour card: {player_card}")
        print("Bot's card: Hidden")
        print(f"Your stack: {player_stack}, Bot's stack: {bot_stack}")

        # Deduct ante
        player_stack -= 1
        bot_stack -= 1
        pot = 2

        # Check for forced check-check scenario (if a player has no chips left)
        forced_result = handle_forced_check_check(player_card, bot_card, pot, player_stack, bot_stack)
        if forced_result:
            player_stack, bot_stack = forced_result
            print(f"\nYour stack: {player_stack}, Bot's stack: {bot_stack}")
            continue  # Start next round

        # Normal betting round
        player_stack, bot_stack = play_round(player_card, bot_card, first_to_act, pot)

        # Alternate first-to-act for the next round
        first_to_act = 'bot' if first_to_act == 'player' else 'player'

        # Display updated stacks
        print(f"\nYour stack: {player_stack}, Bot's stack: {bot_stack}")

        # Ask to play another hand
        play_again = input("\nPlay another hand? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break
def play_round(player_card, bot_card, first_to_act, pot):
    """Play a single round of Kuhn Poker and return updated stacks."""
    global player_stack, bot_stack

    history = ""

    if first_to_act == 'player':
        print("You act first this round.")
        player_action = input("Choose to 'check' or 'bet': ").strip().lower()
        while player_action not in ['check', 'bet']:
            player_action = input("Invalid choice. Choose 'check' or 'bet': ").strip().lower()
        history += player_action

        if player_action == 'bet':
            player_stack -= 1
            pot += 1

        # Bot action
        bot_action_result = bot_action(bot_card, history)
        print(f"Bot chooses to: {bot_action_result}")
        history += bot_action_result

        if bot_action_result == 'check':
            winner = determine_winner(player_card, bot_card)
        elif bot_action_result == 'bet':
            bot_stack -= 1
            pot += 1
            player_response = input("Choose to 'call' or 'fold': ").strip().lower()
            while player_response not in ['call', 'fold']:
                player_response = input("Invalid choice. Choose 'call' or 'fold': ").strip().lower()
            if player_response == 'call':
                player_stack -= 1
                pot += 1
                winner = determine_winner(player_card, bot_card)
            else:
                winner = 'bot'
        elif bot_action_result == 'call':
            bot_stack -= 1
            pot += 1
            winner = determine_winner(player_card, bot_card)
        else:  # bot folds
            winner = 'player'

    else:  # Bot acts first
        print("Bot acts first this round.")
        bot_action_result = bot_action(bot_card, history)
        print(f"Bot chooses to: {bot_action_result}")
        history += bot_action_result

        if bot_action_result == 'check':
            player_action = input("Choose to 'check' or 'bet': ").strip().lower()
            while player_action not in ['check', 'bet']:
                player_action = input("Invalid choice. Choose 'check' or 'bet': ").strip().lower()
            history += player_action
            if player_action == 'check':
                winner = determine_winner(player_card, bot_card)
            else:
                player_stack -= 1
                pot += 1
                bot_response = bot_action(bot_card, history)
                print(f"Bot chooses to: {bot_response}")
                if bot_response == 'call':
                    bot_stack -= 1
                    pot += 1
                    winner = determine_winner(player_card, bot_card)
                else:
                    winner = 'player'
        elif bot_action_result == 'bet':
            bot_stack -= 1
            pot += 1
            player_response = input("Choose to 'call' or 'fold': ").strip().lower()
            while player_response not in ['call', 'fold']:
                player_response = input("Invalid choice. Choose 'call' or 'fold': ").strip().lower()
            if player_response == 'call':
                player_stack -= 1
                pot += 1
                winner = determine_winner(player_card, bot_card)
            else:
                winner = 'bot'
        else:  # bot folds
            winner = 'player'

    # Update stacks based on winner
    player_stack, bot_stack = update_pot_and_stacks(winner, pot, player_stack, bot_stack)
    print(f"\nYour card: {player_card}, Bot's card: {bot_card}")
    print(f"{winner.capitalize()} wins the pot!")

    return player_stack, bot_stack

if __name__ == "__main__":
    player_stack = 10
    bot_stack = 10
    first_to_act = "player"  # Player acts first in the first round

    play_kuhn_poker()
