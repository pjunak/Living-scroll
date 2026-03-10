def test_pb():
    from modules.compendium.service import Compendium
    c = Compendium.load()
    rules = c.payload.get("rules", {})
    print("RULES KEYS:", list(rules.keys()))
    print("PB:", rules.get("character/point_buy"))
    assert False
