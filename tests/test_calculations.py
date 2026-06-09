import pytest
from modules.core.services.calculations import chain_spell_distribution


def test_chain_spell_distribution_constant_per_die_applies_shift():
    distribution = chain_spell_distribution(
        start_rolls=1,
        add_rolls=0,
        initial_dice_value=4,
        additional_dice_value=4,
        modifier=0,
        levels=1,
        constant_per_die=2,
    )
    assert sorted(distribution.keys()) == [3, 4, 5, 6]
    assert distribution[3] == pytest.approx(0.25)


def test_chain_spell_distribution_normalized_and_levels_stack():
    distribution = chain_spell_distribution(
        start_rolls=1,
        add_rolls=1,
        initial_dice_value=4,
        additional_dice_value=6,
        modifier=2,
        levels=2,
        constant_per_die=1,
    )
    assert sum(distribution.values()) == pytest.approx(1.0)
    
    min_total = min(distribution.keys())
    max_total = max(distribution.keys())
    assert min_total >= 4
    assert max_total > min_total
