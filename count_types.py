import json
import os
import sys
from collections import Counter

def count_types(file_path):
    if not os.path.exists(file_path):
        print(f"Error: File {file_path} not found.")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    if isinstance(data, list):
        items = data
    elif isinstance(data, dict):
        # Handle cases where data is keyed by year
        items = []
        for year_items in data.values():
            if isinstance(year_items, list):
                items.extend(year_items)
    else:
        print("Error: Unknown JSON structure.")
        return

    type_counts = Counter()
    for item in items:
        if isinstance(item, dict):
            t = item.get('type', 'missing')
            type_counts[t] += 1
    
    print(f"\nType counts for {file_path}:")
    print("-" * 40)
    for t, count in type_counts.most_common():
        print(f"{t}: {count}")
    print("-" * 40)
    print(f"Total items: {len(items)}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python count_types.py <path_to_json_file>")
    else:
        count_types(sys.argv[1])
