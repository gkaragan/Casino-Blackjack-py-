from card_deck import *
from project import game, hand_counter, bet, option, deposit_money


def test_hand_counter_high():
    assert hand_counter(['|J♣|', '|J♠|', '|9♦|', '|10♣|']) == 39

def test_hand_counter_ace_high():
    assert hand_counter(['|J♣|', '|K♠|', '|A♣|']) == 21

def test_hand_counter_ace_low():
    assert hand_counter(['|A♠|', '|A♣|']) == 12

def test_hand_counter_low():
    assert hand_counter(['|2♠|', '|0♣|']) == 2

def test_option(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "play")
    start = option()
    assert start == "play"

def test_game_standard(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "stand")
    result = game()
    assert result in ["WIN", "LOSS", "DRAW"]

def test_game_hit(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "hit")
    result = game()
    assert result in ["WIN", "LOSS", "DRAW"]

def test_deposit_money_standard(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "1000")
    balance = deposit_money()
    assert balance == 1000

def test_deposit_money_high(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "1000000")
    balance = deposit_money()
    assert balance == 1000000

def test_deposit_money_low(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "1")
    balance = deposit_money()
    assert balance == 1

def test_deposit_money_decimal(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "270.87693")
    balance = deposit_money()
    assert balance == 270.88

def test_bet_equality(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "375.856")
    stake = bet(375.86)
    assert stake == 375.86

def test_bet_lower(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "409.8")
    stake = bet(573.6)
    assert stake == 409.80

