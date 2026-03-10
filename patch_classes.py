import os
import re

MULTICLASS = {
    "barbarian": {"STR": 13},
    "bard": {"CHA": 13},
    "cleric": {"WIS": 13},
    "druid": {"WIS": 13},
    "fighter": {"STR|DEX": 13},
    "monk": {"DEX": 13, "WIS": 13},
    "paladin": {"STR": 13, "CHA": 13},
    "ranger": {"DEX": 13, "WIS": 13},
    "rogue": {"DEX": 13},
    "sorcerer": {"CHA": 13},
    "warlock": {"CHA": 13},
    "wizard": {"INT": 13},
    "artificer": {"INT": 13}, 
}

AC_FORMULAS = {
    "barbarian": {"type": "unarmored_defense", "base": 10, "add": ["DEX", "CON"], "allow_shield": True},
    "monk": {"type": "unarmored_defense", "base": 10, "add": ["DEX", "WIS"], "allow_shield": False}
}

base_dir = "/home/pjunak/Documents/GitHub/Living-scroll/modules/compendium/data/dnd_2024/players_handbook/classes"

import yaml

for cls_name in os.listdir(base_dir):
    cls_path = os.path.join(base_dir, cls_name)
    if not os.path.isdir(cls_path):
        continue
        
    md_file = os.path.join(cls_path, "base.md")
    if not os.path.exists(md_file):
        continue
        
    with open(md_file, "r") as f:
        content = f.read()
        
    match = re.match(r"^---\n(.*?)\n---\n(.*)", content, re.DOTALL)
    if not match:
        print(f"No frontmatter in {md_file}")
        continue
        
    frontmatter = match.group(1)
    body = match.group(2)
    
    data = yaml.safe_load(frontmatter)
    
    # Inject data
    reqs = MULTICLASS.get(cls_name.lower())
    if reqs:
        data["multiclass_requirements"] = reqs
        
    ac = AC_FORMULAS.get(cls_name.lower())
    if ac:
        data["armor_class_formula"] = ac
    else:
        # remove it if it was added as a string
        if "armor_class_formula" in data:
            del data["armor_class_formula"]
        
    new_frontmatter = yaml.dump(data, default_flow_style=False, sort_keys=False)
    
    new_content = f"---\n{new_frontmatter}---\n{body}"
    with open(md_file, "w") as f:
        f.write(new_content)
        
    print(f"Updated {cls_name}")
