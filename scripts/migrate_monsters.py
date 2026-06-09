import re
import yaml
from pathlib import Path

# Match "+17 to hit", reach, etc.
ATTACK_PATTERN = re.compile(r"(Melee|Ranged)\s+(?:Spell |Weapon )?Attack(?: Roll)?: \+?(\d+) to hit", re.IGNORECASE)
REACH_PATTERN = re.compile(r"reach (\d+) ft", re.IGNORECASE)

# Match "Hit: 19 (2d8 + 10) Slashing damage plus 9 (2d8) Fire damage"
# We'll use finditer to catch all damages in a row
DAMAGE_PATTERN = re.compile(r"\((\d+)d(\d+)(?:\s*\+\s*(\d+))?\)\s+([A-Za-z]+)\s+damage", re.IGNORECASE)

# Match "Dexterity Saving Throw: DC 24"
SAVE_PATTERN = re.compile(r"([A-Za-z]+)\s+Saving Throw:\s+DC\s+(\d+)", re.IGNORECASE)

def process_monster(filepath: Path):
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

    migrated = False
    
    # We will build a text block to append to the markdown portion
    plaintext_actions = []

    if 'actions' in data and isinstance(data['actions'], list):
        for act in data['actions']:
            if not isinstance(act, dict): continue
            
            # Check if already migrated
            if act.get('type') in ['attack', 'save', 'utility'] and 'damage' in act and isinstance(act['damage'], list) and act['damage']:
                if isinstance(act['damage'][0].get('base'), dict):
                    continue # Already migrated
            
            desc = act.get('description', '')
            if not isinstance(desc, str) or not desc:
                continue
                
            original_desc = desc
            migrated_this_action = False
                
            # Try parsing Attack Roll
            attack_match = ATTACK_PATTERN.search(desc)
            save_match = SAVE_PATTERN.search(desc)

            if attack_match:
                act['type'] = 'attack'
                act['attack_type'] = 'melee_weapon' if attack_match.group(1).lower() == 'melee' else 'ranged_weapon'
                act['hit_bonus'] = int(attack_match.group(2))
                
                reach_match = REACH_PATTERN.search(desc)
                if reach_match:
                    act['reach'] = int(reach_match.group(1))
                    
                migrated_this_action = True
                
            elif save_match:
                act['type'] = 'save'
                act['ability'] = save_match.group(1).lower()[:3]
                act['dc'] = int(save_match.group(2))
                act['on_pass'] = 'half' if 'half damage' in desc.lower() else 'none'
                act['on_fail'] = 'full'
                migrated_this_action = True

            # Try parsing damages
            damages = []
            for d_match in DAMAGE_PATTERN.finditer(desc):
                migrated_this_action = True
                d_dict = {
                    'type': d_match.group(4).lower(),
                    'base': {
                        'dice': int(d_match.group(1)),
                        'die': int(d_match.group(2)),
                        'bonus': int(d_match.group(3)) if d_match.group(3) else 0
                    }
                }
                damages.append(d_dict)
                
            if damages:
                act['damage'] = damages
                
            if migrated_this_action:
                migrated = True
                if act.get('type') not in ['attack', 'save']:
                     act['type'] = 'utility'
                     
                # Clear description from YAML to avoid massive bloat
                if 'description' in act:
                    del act['description']
                
                # Format plaintext block
                plaintext_actions.append(f"**{act['name']}.** {original_desc}\n")

    if migrated:
        new_frontmatter = yaml.dump(data, sort_keys=False, default_flow_style=False)
        new_text = text.strip()
        if plaintext_actions and "### Actions" not in new_text:
            new_text += "\n\n### Actions\n\n" + "\n".join(plaintext_actions)
        elif plaintext_actions:
            new_text += "\n\n" + "\n".join(plaintext_actions)
            
        new_content = f"---{new_frontmatter}\n---{new_text}\n"
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Migrated: {filepath.name}")
        return True

    return False

if __name__ == '__main__':
    root = Path('modules/compendium/data/dnd_2024')
    migrated_count = 0
    total_count = 0
    
    # Process both Monster Manual and any other places monsters might exist
    for f in root.rglob('*.md'):
        if 'monsters' in f.parts or 'monster_manual' in f.parts:
            total_count += 1
            if process_monster(f):
                migrated_count += 1
    
    print(f"Successfully migrated {migrated_count} of {total_count} monsters.")
