"""
Lightweight formula evaluator for management `max_formula` fields.

Supports expressions like:
  - "INT + level"
  - "WIS + level"
  - "CHA + level / 2"

Uses simple token parsing instead of eval() for safety.
"""

from __future__ import annotations

import math
import re
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from modules.character_sheet.model.model import CharacterSheet

_ABILITY_NAMES = {"STR", "DEX", "CON", "INT", "WIS", "CHA"}


def evaluate_formula(formula: str, sheet: "CharacterSheet") -> int:
    """
    Evaluate a simple arithmetic formula against a CharacterSheet.

    Tokens:
    - Ability abbreviation (STR, DEX, CON, INT, WIS, CHA)
          → resolves to the ability's modifier ((score - 10) // 2)
    - ``level`` → total character level (sum of all class levels)
    - Integer literals
    - Operators: ``+``, ``-``, ``*``, ``/``

    Returns the integer result (floor rounded).
    """
    # Tokenise
    tokens = re.findall(r"[A-Za-z]+|\d+|[+\-*/]", formula)

    # Resolve tokens to numeric values
    resolved: list[float] = []
    ops: list[str] = []

    for tok in tokens:
        upper = tok.upper()
        if upper in _ABILITY_NAMES:
            ability = sheet.abilities.get(upper)
            if ability:
                resolved.append((ability.score - 10) // 2)
            else:
                resolved.append(0)
        elif upper == "LEVEL":
            total_level = sum(
                c.level for c in getattr(sheet.identity, "classes", [])
            )
            resolved.append(max(total_level, 1))
        elif tok.isdigit():
            resolved.append(int(tok))
        elif tok in "+-*/":
            ops.append(tok)
        # Ignore unknown tokens

    if not resolved:
        return 0

    # Simple left-to-right evaluation (no operator precedence needed
    # for the formulas we support).
    result = resolved[0]
    for i, op in enumerate(ops):
        if i + 1 >= len(resolved):
            break
        rhs = resolved[i + 1]
        if op == "+":
            result += rhs
        elif op == "-":
            result -= rhs
        elif op == "*":
            result *= rhs
        elif op == "/":
            result = result / rhs if rhs != 0 else result

    return int(math.floor(result))
