import re
import yaml
from pathlib import Path

# ===========================================
CHALLENGES_DIR = "./challenges"  # Path to challenges directory
AUTHOR = 'CSSA' 
FLAG_PREFIX = 'cssactf'  # Flag format prefix

# Categories that appear in READMEs
CATEGORIES = [
    'Binary Exploitation',
    'Web Exploitation',
    'Cryptography',
    'Forensics',
    'Reverse Engineering',
    'Misc',
    'OSINT',
    'Pwn',
    'Steganography',
    'General Skills'
]
# ===========================================

def parse_readme(readme_path):
    """Parse README and extract challenge metadata"""
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    lines = content.strip().split('\n')
    name = lines[0].strip()  # From first line of README
    
    # Category from README (using the categories list)
    category_pattern = '|'.join(CATEGORIES)
    category = re.search(rf'^\s*[-*]\s*({category_pattern})', content, re.MULTILINE)
    
    # Difficulty from README
    difficulty = re.search(r'^\s*[-*]\s*(Easy|Medium|Hard)', content, re.MULTILINE)
    
    # Points from "XXX Points" in README
    points = re.search(r'(\d+)\s+Points', content)
    
    # Type from README (optional: standard or dynamic)
    type_match = re.search(r'^\s*[-*]\s*Type:\s*(standard|dynamic)', content, re.MULTILINE | re.IGNORECASE)
    challenge_type = type_match.group(1).lower() if type_match else 'standard'
    
    # State from README (optional: visible or hidden)
    state_match = re.search(r'^\s*[-*]\s*State:\s*(visible|hidden)', content, re.MULTILINE | re.IGNORECASE)
    state = state_match.group(1).lower() if state_match else 'visible'
    
    # Flag Type from README (optional: static, regex, case_insensitive)
    flag_type_match = re.search(r'^\s*[-*]\s*Flag Type:\s*(static|regex|case_insensitive)', content, re.MULTILINE | re.IGNORECASE)
    flag_type = flag_type_match.group(1).lower() if flag_type_match else 'static'
    
    # Description section from README
    desc_match = re.search(r'##\s*Description\s*\n(.*?)(?=\n##\s*(?:Hints?|Solution|Flag)|$)', content, re.DOTALL)
    
    # Hints section from README
    hints_match = re.search(r'##\s*Hints?\s*\n(.*?)(?=\n##\s*(?:Solution|Flag)|$)', content, re.DOTALL)
    
    # Flag from Flag section
    flag_section_match = re.search(r'##\s*Flag\s*\n`([^`]+)`', content)
    if flag_section_match:
        flag = flag_section_match.group(1).strip()
    else:
        # Fallback to searching for flag pattern anywhere
        flag_match = re.search(rf'{FLAG_PREFIX}\{{[^}}]+\}}', content)
        flag = flag_match.group(0) if flag_match else ''
    
    description = desc_match.group(1).strip() if desc_match else ''
    if hints_match:
        description += f"\n\nHints:\n{hints_match.group(1).strip()}"
    
    return {
        'name': name,
        'category': category.group(1) if category else 'Misc',
        'value': int(points.group(1)) if points else 100,
        'description': description,
        'flag': flag,
        'type': challenge_type,
        'state': state,
        'flag_type': flag_type,
        'tags': [difficulty.group(1) if difficulty else 'Medium']
    }

def generate_challenge_yml(challenge_dir):
    """Generate challenge.yml for a challenge"""
    readme_path = challenge_dir / 'README.md'
    if not readme_path.exists():
        print(f"Skipping {challenge_dir.name}: No README.md found")
        return
    
    data = parse_readme(readme_path)
    
    # Find files in the files/subdirectory if it exists
    files = []
    files_dir = challenge_dir / 'files'
    if files_dir.exists() and files_dir.is_dir():
        for f in files_dir.iterdir():
            if f.is_file():
                files.append(str(f.name))
    
    # ============= CTFd STANDARD STRUCTURE =============
    challenge_yml = {
        'name': data['name'],           # Challenge name
        'author': AUTHOR,               
        'category': data['category'],    # Challenge category
        'description': data['description'], # Challenge description
        'value': data['value'],          # Points value
        'type': data['type'],            # 'standard' or 'dynamic' (from README or default)
        'state': data['state'],          # 'visible' or 'hidden' (from README or default)
        'flags': [                       
            {
                'flag': data['flag'],    # The actual flag
                'type': data['flag_type'] # Flag type (from README or default)
            }
        ],
        'tags': data['tags'],            # Array of tags (we use difficulty)
        'files': files                   # The files to upload
    }
    # ==================================================
    
    yml_path = challenge_dir / 'challenge.yml'
    with open(yml_path, 'w', encoding='utf-8') as f:
        yaml.dump(challenge_yml, f, default_flow_style=False, sort_keys=False, allow_unicode=True, width=1000)
    
    print(f"Generated: {challenge_dir.name}/challenge.yml")

def process_challenges(challenges_dir):
    """Process all challenge directories"""
    challenges_path = Path(challenges_dir)
    if not challenges_path.exists():
        print(f"Error: Challenges directory '{challenges_dir}' not found")
        return
    
    challenge_count = 0
    for challenge_dir in sorted(challenges_path.iterdir()):
        if challenge_dir.is_dir() and not challenge_dir.name.startswith('.'):
            try:
                generate_challenge_yml(challenge_dir)
                challenge_count += 1
            except Exception as e:
                print(f"Error in {challenge_dir.name}: {e}")
    
    print(f"\nProcessed {challenge_count} challenges")

if __name__ == "__main__":
    process_challenges(CHALLENGES_DIR)