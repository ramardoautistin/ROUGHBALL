"""
ROUGHBALL: Cards Module
Handles card deck creation, shuffling, and drawing
"""

import random


class Card:
    """Represents a single playing card"""
    
    def __init__(self, suit, value):
        self.suit = suit  # 'C', 'H', 'S', 'D', or 'JKR'
        self.value = value  # 2-14 (J=11, Q=12, K=13, A=14), JKR=15
    
    def __repr__(self):
        from .teams import SYMBOLS
        
        if self.suit == 'JKR':
            return "[JKR]"
        
        VALUE_NAMES = {11: 'J', 12: 'Q', 13: 'K', 14: 'A'}
        val_str = VALUE_NAMES.get(self.value, str(self.value))
        suit_sym = SYMBOLS[self.suit]
        
        return f"[{suit_sym} {val_str}]"
    
    def is_offensive(self):
        """Check if card is offensive (red suits)"""
        return self.suit in ['H', 'D']
    
    def is_defensive(self):
        """Check if card is defensive (black suits)"""
        return self.suit in ['C', 'S']
    
    def to_dict(self):
        """Convert to dictionary for compatibility"""
        return {"suit": self.suit, "val": self.value}


class Deck:
    """Represents a 54-card deck"""
    
    def __init__(self):
        self.cards = []
        self.discard = []
        self.reset()
    
    def reset(self):
        """Create fresh 54-card deck"""
        self.cards = []
        
        # Standard 52 cards
        for suit in ['C', 'H', 'S', 'D']:
            for value in range(2, 15):  # 2-14 (A)
                self.cards.append(Card(suit, value))
        
        # 2 Jokers
        self.cards.append(Card('JKR', 15))
        self.cards.append(Card('JKR', 15))
        
        self.shuffle()
    
    def shuffle(self):
        """Shuffle the deck"""
        random.shuffle(self.cards)
    
    def draw(self, num=1):
        """
        Draw cards from deck
        
        Args:
            num: Number of cards to draw
        
        Returns:
            Single Card if num=1, list of Cards if num>1
        """
        drawn = []
        
        for _ in range(num):
            if not self.cards:
                # Deck empty, reshuffle discard pile
                if self.discard:
                    self.cards = self.discard
                    self.discard = []
                    self.shuffle()
                else:
                    # No cards left at all
                    break
            
            if self.cards:
                card = self.cards.pop()
                drawn.append(card)
        
        if num == 1:
            return drawn[0] if drawn else None
        return drawn
    
    def discard_cards(self, cards):
        """Add cards to discard pile"""
        if isinstance(cards, list):
            self.discard.extend(cards)
        else:
            self.discard.append(cards)
    
    def size(self):
        """Get number of cards remaining in deck"""
        return len(self.cards)


def get_fresh_deck_dicts():
    """
    Create fresh deck as list of dicts (for compatibility with old code)
    
    Returns:
        List of card dictionaries
    """
    deck = []
    for suit in ['C', 'H', 'S', 'D']:
        for value in range(2, 15):
            deck.append({"suit": suit, "val": value})
    
    # 2 Jokers
    deck.append({"suit": "JKR", "val": 15})
    deck.append({"suit": "JKR", "val": 15})
    
    random.shuffle(deck)
    return deck
