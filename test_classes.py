import pytest
from .classes import Card


_all_valid_combinations = [
    (value, suit) 
    for value in ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
    for suit in ('C', 'D', 'H', 'S')
]


def test_card_bad_suit():
    with pytest.raises(AssertionError):
        Card(5, 'J')


def test_card_bad_value():
    with pytest.raises(AssertionError):
        Card('B', 'D')


@pytest.mark.parametrize("value, suit", _all_valid_combinations)
def test_card_good(value, suit):
    card = Card(value, suit)
    assert card.value == value
    assert card.suit == suit


@pytest.mark.parametrize("value, suit", _all_valid_combinations)
def test_card_from_str(value, suit):
    string = f'{value}{suit}'
    card = Card.from_str(string)
    assert isinstance(card, Card)
    assert card.value == value
    assert card.suit == suit


def test_card_str():
    assert str(Card('2', 'S')) == '2S'
    assert str(Card('A', 'H')) == 'AH'
    assert str(Card('10', 'D')) == '10D'
    assert str(Card('K', 'C')) == 'KC'
