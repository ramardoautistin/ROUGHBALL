"""
Quick test to verify v10.3 implementations
"""

import sys
sys.path.insert(0, 'C:/Users/ramar/Documents/Code/GAME_DESIGN/roughball_v2')

from core.display import print_matrix, safe_input
from core.teams import TEAMS

print("=" * 60)
print("   ROUGHBALL v10.3 - VERIFICATION TEST")
print("=" * 60)

# Test 1: Neutral Formation Display
print("\n[TEST 1]: NEUTRAL FORMATION DISPLAY")
print("-" * 60)

u_team = TEAMS['1']
b_team = TEAMS['2']

print_matrix(u_team, b_team, 0, 0, 'D1 National Legends',
             True, 'Pandemical', 'Mountain LIONS', 'Greenland VIKINGS', 'neutral')

print("\n" + "=" * 60)
print("EXPECTED:")
print("  Row order should be: D, C, B, A, [SNAP], A, B, C, D")
print("  Top D row: WB at 1, RB at 4, TB at 8")
print("  Top A row: DE at 3, DT at 5")
print("  Bottom E row: DT at 4, DE at 6")
print("  Bottom H row: WB at 1, RG at 5, TB at 8")
print("=" * 60)

# Test 2: ESC Backdoor
print("\n[TEST 2]: ESC BACKDOOR TEST")
print("-" * 60)
print("Type 'ESC' to test the backdoor (or anything else to skip):")

try:
    result = safe_input("  > ")
    print(f"You entered: {result}")
    print("ESC NOT detected - test continues")
except Exception as e:
    print(f"ESC DETECTED! Exception: {e}")
    print("✓ ESC backdoor working!")

print("\n" + "=" * 60)
print("   TESTS COMPLETE")
print("=" * 60)
