import os
import json
import re
from typing import Dict, List, Any


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9\-\_\s]", "", value)
    value = re.sub(r"[\s\-]+", "-", value)
    return value or "unknown"


def main() -> None:
    source_path = os.path.join("hindi_pro", "hindi_all_years.json")
    output_dir = "hindi_pro_chapters"
    os.makedirs(output_dir, exist_ok=True)

    with open(source_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if not isinstance(data, dict):
        raise ValueError("Expected top-level object keyed by year.")

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

        with open(os.path.join(sec_dir, "manifest.json"), "w", encoding="utf-8") as f:
            json.dump(sec_manifest, f, ensure_ascii=False, indent=2)

    with open(os.path.join(output_dir, "manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)

    print(f"Wrote {len(manifest)} chapter files across {len(sections)} sections to {output_dir}")


if __name__ == "__main__":
    main()
