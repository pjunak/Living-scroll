import re
import yaml
from pathlib import Path

# Match formulas like "8d6 Fire damage", "1d10 Fire damage"
DAMAGE_PATTERN = re.compile(r"(\d+)d(\d+)\s+([A-Za-z]+)\s+damage", re.IGNORECASE)
HEALING_PATTERN = re.compile(r"regains.*?(\d+)d(\d+)", re.IGNORECASE)

# Match scaling like "increases by 1d6", "increases by 1d10"
SCALING_PATTERN = re.compile(r"increases by (\d+)d(\d+)", re.IGNORECASE)

# Determine hit vs save based on keywords
SAVE_PATTERN = re.compile(r"([A-Za-z]+)\s+saving throw", re.IGNORECASE)
ATTACK_PATTERN = re.compile(r"spell attack", re.IGNORECASE)

def process_spell(filepath: Path):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    parts = content.split('---')
    if len(parts) < 3:
        return False

    frontmatter = parts[1]
    text = parts[2]

    try:
        data = yaml.safe_load(frontmatter)
    except yaml.YAMLError:
        return False

    # Skip if actions are already fully implemented with our new deep schema (containing 'base' dict)
    if 'actions' in data and data['actions']:
        if any('damage' in a and isinstance(a['damage'][0].get('base'), dict) for a in data['actions'] if 'damage' in a):
            return True # Already migrated
        if any('healing' in a and isinstance(a['healing'].get('base'), dict) for a in data['actions'] if 'healing' in a):
            return True

    migrated = False
    action_type = 'utility'
    ability = None
    on_pass = None
    on_fail = None

    save_match = SAVE_PATTERN.search(text)
    if save_match:
        action_type = 'save'
        ability = save_match.group(1).lower()[:3] # e.g. dex, str
        on_pass = 'half' if 'half as much' in text.lower() else 'none'
        on_fail = 'full'
    elif ATTACK_PATTERN.search(text):
        action_type = 'attack'

    action = {
        'type': action_type if action_type != 'utility' else 'heal'
    }

    if action_type == 'save':
        action['ability'] = ability
        action['on_pass'] = on_pass
        action['on_fail'] = on_fail

    # Try to find scaling
    scaling_match = SCALING_PATTERN.search(text)
    scaling = None
    if scaling_match:
        s_dice = int(scaling_match.group(1))
        s_die = int(scaling_match.group(2))
        mode = 'character_level' if data.get('level', 0) == 0 else 'spell_level'
        scaling = {
            'dice_per_slot': s_dice,
            'die': s_die,
            'mode': mode
        }

    damage_match = DAMAGE_PATTERN.search(text)
    if damage_match:
        migrated = True
        if action['type'] == 'heal': action['type'] = 'utility' # fallback if mixed
        num_dice = int(damage_match.group(1))
        die_size = int(damage_match.group(2))
        dmg_type = damage_match.group(3).lower()
        
        damage_block = {
            'type': dmg_type,
            'base': {
                'dice': num_dice,
                'die': die_size,
                'bonus': 0
            }
        }
        if scaling: damage_block['scaling'] = scaling
        action['damage'] = [damage_block]

    healing_match = HEALING_PATTERN.search(text)
    if healing_match and not damage_match:
        migrated = True
        action['type'] = 'heal'
        action['healing'] = {
            'base': {
                'dice': int(healing_match.group(1)),
                'die': int(healing_match.group(2)),
                'bonus': 'spellcasting_modifier' if 'spellcasting ability modifier' in text.lower() else 0
            }
        }

    if migrated:
        data['actions'] = [action]
        new_frontmatter = yaml.dump(data, sort_keys=False, default_flow_style=False)
        new_content = f"---{new_frontmatter}---{text}"
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Migrated: {filepath.name}")
        return True

    return False

if __name__ == '__main__':
    root = Path('modules/compendium/data/dnd_2024/players_handbook/spells')
    migrated_count = 0
    total_count = 0
    for f in root.rglob('*.md'):
        total_count += 1
        if process_spell(f):
            migrated_count += 1
    
    print(f"Successfully migrated {migrated_count} of {total_count} spells.")
