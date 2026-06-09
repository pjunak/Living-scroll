from modules.core.services.dices import combination_distribution


def test_combination_distribution_single_roll_with_modifier():
    distribution = combination_distribution([1, 2], 1, modifier=3)
    assert distribution[4] == 0.5
    assert distribution[5] == 0.5
    assert sum(distribution.values()) == 1.0

def test_combination_distribution_multiple_rolls():
    distribution = combination_distribution([1, 2], 2)
    expected = {2: 0.25, 3: 0.5, 4: 0.25}
    assert distribution == expected
    assert sum(distribution.values()) == 1.0
