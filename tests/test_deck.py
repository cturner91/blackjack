import pytest
import random

from ..classes import Deck, Card


def test_deck_full_52():
    deck = Deck()
    assert len(deck.cards) == 52

    strings = set([str(card) for card in deck.cards])
    for value in ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'):
        for suit in ('C', 'D', 'H', 'S'):
            assert f'{value}{suit}' in strings


def test_deck_selected_cards():
    deck = Deck([
        Card('A', 'S'),
        Card('A', 'C'),
        Card('A', 'D'),
        Card('A', 'H'),
    ])
    assert len(deck.cards) == 4

    strings = set([str(card) for card in deck.cards])
    for suit in ('C', 'D', 'H', 'S'):
        assert f'A{suit}' in strings


def test_shuffle():
    deck = Deck([
        Card('A', 'S'),
        Card('A', 'C'),
        Card('A', 'D'),
        Card('A', 'H'),
    ])
    assert len(deck.cards) == 4
    assert str(deck.cards[0]) == 'AS'
    assert str(deck.cards[1]) == 'AC'
    assert str(deck.cards[2]) == 'AD'
    assert str(deck.cards[3]) == 'AH'

    random.seed(33)
    deck.shuffle()

    assert str(deck.cards[0]) == 'AH'
    assert str(deck.cards[1]) == 'AS'
    assert str(deck.cards[2]) == 'AC'
    assert str(deck.cards[3]) == 'AD'


def test_draw_no_cards_left():
    deck = Deck([Card('A', 'S')])
    card = deck.draw()

    assert str(card) == 'AS'
    assert len(deck.cards) == 0

    with pytest.raises(ValueError):
        deck.draw()


def test_draw_random():
    deck = Deck([
        Card('A', 'S'),
        Card('A', 'C'),
        Card('A', 'D'),
        Card('A', 'H'),
    ])
    cards_seen = set()

    card = deck.draw()
    assert len(deck.cards) == 3
    assert str(card) not in cards_seen
    cards_seen.add(str(card))

    card = deck.draw()
    assert len(deck.cards) == 2
    assert str(card) not in cards_seen
    cards_seen.add(str(card))

    card = deck.draw()
    assert len(deck.cards) == 1
    assert str(card) not in cards_seen
    cards_seen.add(str(card))

    card = deck.draw()
    assert len(deck.cards) == 0
    assert str(card) not in cards_seen
    cards_seen.add(str(card))


def test_draw_with_index():
    deck = Deck([
        Card('A', 'S'),
        Card('A', 'C'),
        Card('A', 'D'),
        Card('A', 'H'),
    ])

    card = deck.draw(1)
    assert str(card) == 'AC'

    strings = set([str(x) for x in deck.cards])
    for remaining in ('AS', 'AD', 'AH'):
        assert remaining in strings

    # draw another
    card = deck.draw(-1)
    assert str(card) == 'AH'

    strings = set([str(x) for x in deck.cards])
    for remaining in ('AS', 'AD'):
        assert remaining in strings

    # draw another
    card = deck.draw(0)
    assert str(card) == 'AS'

    strings = set([str(x) for x in deck.cards])
    for remaining in ('AD',):
        assert remaining in strings


