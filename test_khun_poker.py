import pytest
from khunpoker import deal_cards, determine_winner, bot_action, update_pot_and_stacks, handle_forced_check_check

def test_card_distribution():
    """Ensure the deal_cards function returns valid cards without duplicates."""
    seen_cards = set()
    for _ in range(100):  # Run multiple times for randomness
        player_card, bot_card = deal_cards()
        assert player_card in ['K', 'Q', 'J']
        assert bot_card in ['K', 'Q', 'J']
        assert player_card != bot_card
        seen_cards.update([player_card, bot_card])

    assert seen_cards == {'K', 'Q', 'J'}  # Ensure all cards are being dealt

def test_winner_determination():
    """Test the determine_winner function."""
    assert determine_winner('K', 'Q') == 'player'
    assert determine_winner('K', 'J') == 'player'
    assert determine_winner('Q', 'J') == 'player'
    assert determine_winner('J', 'K') == 'bot'
    assert determine_winner('J', 'Q') == 'bot'
    assert determine_winner('Q', 'K') == 'bot'

def test_bot_action():
    """Test bot's decision-making in different scenarios."""

    # Bot acts first
    assert bot_action('K', "") == 'bet'
    assert bot_action('Q', "") in ['check', 'bet']
    assert bot_action('J', "") == 'check'

    # Bot responds after player checks
    assert bot_action('K', "check") == 'bet'
    assert bot_action('Q', "check") in ['check', 'bet']
    assert bot_action('J', "check") == 'check'

    # Bot reacts to a player bet
    assert bot_action('K', "bet") == 'call'
    assert bot_action('Q', "bet") in ['call', 'fold']
    assert bot_action('J', "bet") == 'fold'

    # Bot reacts after "check bet"
    assert bot_action('K', "check bet") == 'call'
    assert bot_action('Q', "check bet") in ['call', 'fold']
    assert bot_action('J', "check bet") == 'fold'

def test_pot_distribution():
    """Test that the correct winner gets the pot."""
    assert update_pot_and_stacks('player', 4, 10, 10) == (14, 10)
    assert update_pot_and_stacks('bot', 6, 8, 12) == (8, 18)

def test_forced_check_check():
    """Ensure check-check happens when a player has no chips left after ante."""
    # Scenario where player has no chips left after ante
    assert handle_forced_check_check('K', 'Q', 2, 0, 5) == (2, 5)  # Player wins with K
    assert handle_forced_check_check('J', 'K', 2, 5, 0) == (5, 2)  # Bot wins with K
    # If both players have chips, function should return None (normal game continues)
    assert handle_forced_check_check('K', 'J', 2, 5, 5) is None
