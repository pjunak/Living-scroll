import yaml
import re
from pathlib import Path

def process_feat(filepath: Path):
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

    if 'repeatable' in data:
        return False

    is_repeatable = False
    
    # Check for the literal "Repeatable" keyword in the rules text
    if re.search(r'\*\*Repeatable\.\*\*', text, re.IGNORECASE) or 'can take this feat more than once' in text.lower():
        is_repeatable = True

    data['repeatable'] = is_repeatable

    new_frontmatter = yaml.dump(data, sort_keys=False, default_flow_style=False)
    new_content = f"---{new_frontmatter}---{text}"
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print(f"Migrated feat: {filepath.name} (Repeatable: {is_repeatable})")
    return True

if __name__ == '__main__':
    root = Path('modules/compendium/data/dnd_2024')
    migrated_count = 0
    total_count = 0
    
    for f in root.rglob('*.md'):
        if 'feats' in f.parts:
            total_count += 1
            if process_feat(f):
                migrated_count += 1
    
    print(f"Successfully migrated {migrated_count} of {total_count} feats.")
