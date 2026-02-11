import shutil
import os
import pathlib
import datetime

def main():
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    
    folders = ["hindi_data", "hindi_data_annotated", "hindi_pro"]
    
    base_dir = pathlib.Path(".")
    backup_root = base_dir / "hindi_data_backup" / timestamp
    backup_root.mkdir(parents=True, exist_ok=True)
    
    print(f"🧹 Starting Hindi Data Cleanup (Backup: {backup_root})")
    
    for folder_name in folders:
        folder_path = base_dir / folder_name
        if not folder_path.exists():
            continue
            
        # Create backup dest
        backup_dest = backup_root / folder_name
        shutil.copytree(folder_path, backup_dest, dirs_exist_ok=True)
        print(f"📦 Backed up {folder_name}")
        
        # Delete JSON files
        files = list(folder_path.glob("*.json"))
        deleted_count = 0
        for f in files:
            if f.name == "manifest.json":
                continue
            f.unlink()
            deleted_count += 1
            
        print(f"🗑️  Deleted {deleted_count} files from {folder_name}")

if __name__ == "__main__":
    main()
