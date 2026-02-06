import json
import utils

with open('social_science_data_raw/soc_2020i_raw.txt', 'r', encoding='utf-8') as f:
    text = f.read()

cleaned = utils.clean_json_response(text)
try:
    data = json.loads(cleaned)
    print("✅ Successfully parsed!")
except json.JSONDecodeError as e:
    print(f"❌ Failed to parse: {e}")
    print(f"Error at line {e.lineno}, column {e.colno}")
    
    # Print the context around the error
    lines = cleaned.splitlines()
    start_line = max(0, e.lineno - 3)
    end_line = min(len(lines), e.lineno + 2)
    for i in range(start_line, end_line):
        prefix = ">>>" if i == e.lineno - 1 else "   "
        if i < len(lines):
            print(f"{prefix} {i+1}: {lines[i]}")
