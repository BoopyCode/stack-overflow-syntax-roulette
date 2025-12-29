#!/usr/bin/env python3
"""Stack Overflow Syntax Roulette - Because copy-pasting code you don't understand is basically gambling."""

import random
import re
import sys

def syntax_roulette(code_snippet):
    """
    Randomly 'improves' your copy-pasted code with Stack Overflow's finest syntax variations.
    Warning: May cause subtle bugs, existential dread, or both.
    """
    
    # The magic happens here - these are the 'features' you didn't know you needed
    transformations = [
        # Python 2 vs 3 classics
        (r'print\(([^)]+)\)', lambda m: f'print {m.group(1)}'),  # Python 2 style
        (r'xrange\(', 'range('),  # Someone's stuck in the past
        (r'raw_input\(', 'input('),  # Time traveler detected
        
        # Style wars
        (r'def ([a-zA-Z_][a-zA-Z0-9_]*)\(', lambda m: f'def {m.group(1).upper()}('),  # SHOUTY functions
        (r'\"([^\"]+)\"', lambda m: f"'{m.group(1)}'"),  # Single quote evangelist
        (r"'([^']+)'", lambda m: f'"{m.group(1)}"'),  # Double quote purist
        
        # 'Creative' variable naming
        (r'\bfor\b', '4'),  # Leet speak optimization
        (r'\bif\b', 'iff'),  # Extra safety
        (r'\bTrue\b', 'true'),  # JavaScript developer spotted
        (r'\bFalse\b', 'false'),  # They're among us
        
        # Random whitespace - the silent killer
        (r'    ', '\t'),  # Tab vs spaces: FIGHT!
        (r'\n\n', '\n'),  # Who needs readability?
    ]
    
    # Apply random transformations (because consistency is overrated)
    modified = code_snippet
    for pattern, replacement in random.sample(transformations, k=random.randint(1, 3)):
        if random.random() > 0.5:  # 50% chance to apply each - like Russian roulette!
            if callable(replacement):
                modified = re.sub(pattern, replacement, modified)
            else:
                modified = re.sub(pattern, replacement, modified)
    
    return modified


def main():
    """Main function - because every script needs one, apparently."""
    print("Stack Overflow Syntax Roulette")
    print("=" * 40)
    print("Paste your code (Ctrl+D when done):\n")
    
    try:
        code = sys.stdin.read()
        if not code.strip():
            print("No code? That's actually the safest approach!")
            return
            
        print("\nYour 'improved' code:\n")
        print(syntax_roulette(code))
        print("\nGood luck debugging that! 🎲")
        
    except KeyboardInterrupt:
        print("\n\nWise choice. Understanding code is for losers anyway.")

if __name__ == "__main__":
    main()