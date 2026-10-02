import os
import json
import re
from typing import Dict, List, Any


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9\-\_\s]", "", value)
    value = re.sub(r"[\s\-]+", "-", value)
    return value or "unknown"


def split_by_chapters(source_file: str, output_dir: str, type_name: str) -> Dict[str, Any]:
    with open(source_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    if not isinstance(data, dict):
        raise ValueError(f"Expected top-level object keyed by year in {source_file}")

    sections: Dict[str, Dict[str, Dict[str, List[Dict[str, Any]]]]] = {}

    for year, items in data.items():
        if not isinstance(items, list):
            continue
        for item in items:
            if not isinstance(item, dict):
                continue
            section = item.get("section")
            if not section or section in ("UNCLASSIFIED", "unknown", "None"):
                section = "Unclassified"
            else:
                section = str(section).strip()

            chapter_id = item.get("chapter")
            if chapter_id is None or chapter_id == "":
                chapter_id = item.get("chapter_name")
            if chapter_id is None or chapter_id == "":
                chapter_id = "unclassified"

            chapter_key = str(chapter_id).strip()

            if section not in sections:
                sections[section] = {}
            if chapter_key not in sections[section]:
                sections[section][chapter_key] = {}
            sections[section][chapter_key].setdefault(year, []).append(item)

    manifest = []
    total_chapters = 0
    for section_name, chapters in sorted(sections.items()):
        sec_dir = os.path.join(output_dir, section_name)
        os.makedirs(sec_dir, exist_ok=True)
        sec_manifest = []

        for chapter_key, year_map in sorted(chapters.items(), key=lambda x: (int(x[0]) if x[0].isdigit() else 999, x[0])):
            try:
                ordered_years = sorted(year_map.keys(), key=lambda y: int(y))
            except ValueError:
                ordered_years = sorted(year_map.keys())
            ordered_obj = {y: year_map[y] for y in ordered_years}

            filename = f"chapter-{slugify(chapter_key)}.json"
            out_path = os.path.join(sec_dir, filename)
            with open(out_path, "w", encoding="utf-8") as f:
                json.dump(ordered_obj, f, ensure_ascii=False, indent=2)

            total = sum(len(v) for v in year_map.values())
            entry = {
                "section": section_name,
                "chapter": chapter_key,
                "file": f"{section_name}/{filename}",
                "total_items": total,
                "years": len(year_map)
            }
            sec_manifest.append(entry)
            manifest.append(entry)
            total_chapters += 1

        with open(os.path.join(sec_dir, "manifest.json"), "w", encoding="utf-8") as f:
            json.dump(sec_manifest, f, ensure_ascii=False, indent=2)

    manifest_path = os.path.join(output_dir, "manifest.json")
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)

    return {
        "type": type_name,
        "total_chapters": total_chapters,
        "total_items": sum(entry["total_items"] for entry in manifest),
        "chapters": manifest
    }


def main() -> None:
    types_dir = "english_pro_types"
    base_output_dir = "english_pro_type_chapters"

    types = ["objective", "short", "long", "comprehension", "letter_writing", "essay", "translation"]

    overall_manifest = []

    for type_name in types:
        source_file = os.path.join(types_dir, f"type-{type_name}.json")
        if not os.path.exists(source_file):
            print(f"Warning: {source_file} not found, skipping")
            continue

        output_dir = os.path.join(base_output_dir, f"{type_name}_chapters")
        os.makedirs(output_dir, exist_ok=True)

        print(f"Processing {type_name} type...")
        manifest_info = split_by_chapters(source_file, output_dir, type_name)
        overall_manifest.append(manifest_info)

        print(f"  Created {manifest_info['total_chapters']} chapter files across sections")
        print(f"  Total items: {manifest_info['total_items']}")

    overall_manifest_path = os.path.join(base_output_dir, "overall_manifest.json")
    with open(overall_manifest_path, "w", encoding="utf-8") as f:
        json.dump(overall_manifest, f, ensure_ascii=False, indent=2)

    print(f"\nCompleted processing all types")
    print(f"Output directories created under: {base_output_dir}")
    print(f"Overall manifest written to: {overall_manifest_path}")


if __name__ == "__main__":
    main()
