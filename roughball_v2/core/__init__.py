"""
ROUGHBALL: Core Package
"""

from .teams import TEAMS, LEAGUES, ERAS, SYMBOLS, SUITS, SUIT_NAMES
from .cards import Card, Deck, get_fresh_deck_dicts
from .dice import roll_d66, roll_d4, roll_d6, count_hits, get_success_window
from .display import clear, print_matrix, print_header, print_playbook_status, check_escape, EscapeToMenu
from .ai import smart_bot_logic
from .resolver import resolve_play
from .match import run_match

__all__ = [
    'TEAMS', 'LEAGUES', 'ERAS', 'SYMBOLS', 'SUITS', 'SUIT_NAMES',
    'Card', 'Deck', 'get_fresh_deck_dicts',
    'roll_d66', 'roll_d4', 'roll_d6', 'count_hits', 'get_success_window',
    'clear', 'print_matrix', 'print_header', 'print_playbook_status', 'check_escape', 'EscapeToMenu',
    'smart_bot_logic',
    'resolve_play',
    'run_match'
]
