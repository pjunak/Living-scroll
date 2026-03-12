import os
import re
import yaml
from pathlib import Path

bg_dir = Path("modules/compendium/data/dnd_2024/players_handbook/backgrounds")

for filepath in bg_dir.glob("*.md"):
    content = filepath.read_text(encoding="utf-8")
    
    # Parse existing frontmatter and markdown
    parts = content.split("---", 2)
    if len(parts) >= 3:
        frontmatter_str = parts[1]
        markdown_body = parts[2]
        
        frontmatter = yaml.safe_load(frontmatter_str) or {}
        
        # Look for Ability Scores
        ability_match = re.search(r'\*\*Ability Scores:\*\*\s*(.+)', markdown_body)
        if ability_match:
            abilities = [a.strip()[:3].upper() for a in ability_match.group(1).replace("and", ",").split(",")]
            abilities = [a for a in abilities if a in ["STR", "DEX", "CON", "INT", "WIS", "CHA"]]
            if abilities:
                # D&D 2024 backgrounds always give a choice of +2/+1 or +1/+1/+1 among 3 stats
                frontmatter['ability_bonus_options'] = {
                    "choose": 3, # Usually choose 3 for +1 or pick 2 for +2/+1. The UI handles +2/+1 vs +1/+1/+1 logic.
                    # Wait, background ASI in D&D 2024 is +2/+1 or +1/+1/+1.
                    # The ASIWidget handles this! So we just need to provide the 'allowed' list!
                    "abilities": abilities
                }
                
        # Look for Feat
        feat_match = re.search(r'\*\*Feat:\*\*\s*([^\n]+)', markdown_body)
        if feat_match:
            feat_name = feat_match.group(1).strip()
            # E.g. "Magic Initiate (Cleric)" -> "Magic Initiate"
            if "(" in feat_name:
                feat_name = feat_name.split("(")[0].strip()
            frontmatter['starting_feat'] = feat_name
            
        # Write back
        new_frontmatter_str = yaml.dump(frontmatter, sort_keys=False)
        new_content = f"---\n{new_frontmatter_str}...\n---\n{markdown_body}"
        filepath.write_text(new_content, encoding="utf-8")
        print(f"Updated {filepath.name}")
