import os
import json

SUBJECTS = ['english', 'hindi', 'mathematics', 'sanskrit', 'science', 'social_science']

def check_counts():
    print(f"{'Subject':<15} | {'File':<20} | {'Short Count':<12}")
    print("-" * 55)
    
    counts = {}

    for subject in SUBJECTS:
        # Try finding the 2025 file
        base_dir = f"{subject}_data_annotated"
        if not os.path.exists(base_dir):
            base_dir = f"{subject}_data" # Fallback
            
        filename = f"{subject[:3]}_2025i.json" # heuristic for filename
        # Fix filenames manually as they might vary
        if subject == 'social_science': filename = "soc_2025i.json"
        
        filepath = os.path.join(base_dir, filename)
        
        if not os.path.exists(filepath):
             # Try listing to find match
             found = False
             if os.path.exists(base_dir):
                 for f in os.listdir(base_dir):
                     if "2025i" in f and f.endswith(".json"):
                         filepath = os.path.join(base_dir, f)
                         found = True
                         break
             if not found:
                 print(f"{subject:<15} | {'Not Found':<20} | {'N/A':<12}")
                 counts[subject] = 0
                 continue

        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
                short_count = sum(1 for item in data if item.get('type') == 'short')
                print(f"{subject:<15} | {os.path.basename(filepath):<20} | {short_count:<12}")
                counts[subject] = short_count
        except Exception as e:
            print(f"{subject:<15} | {'Error':<20} | {str(e):<12}")
            counts[subject] = 0
            
    return counts

if __name__ == "__main__":
    check_counts()
