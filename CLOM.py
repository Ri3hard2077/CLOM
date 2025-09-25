"""
clom.py – Core logic for CLOM (Cyberpunk Load Order Manager)
Uitgebreide versie met bestandstype-filter en load order sorting.
"""

import json
from pathlib import Path

DEFAULT_PROFILES_PATH = Path("./profiles")
DEFAULT_PROFILES_PATH.mkdir(parents=True, exist_ok=True)

# Standaard relevante extensies
DEFAULT_EXTENSIONS = [".archive", ".xl", ".yaml", ".json", ".lua", ".reds", ".ini"]

def load_mods(path="./mods", extensions=None):
    """
    Laadt mods en filtert bestanden op extensie.
    """
    if extensions is None:
        extensions = DEFAULT_EXTENSIONS

    mods = []
    path = Path(path)
    if not path.exists():
        return mods

    for entry in path.iterdir():
        if entry.is_dir():
            files = [
                str(f.relative_to(entry))
                for f in entry.rglob("*")
                if f.is_file() and f.suffix.lower() in extensions
            ]
            mods.append({
                "name": entry.name,
                "version": "1.0",
                "files": files
            })
    return mods

def resolve_conflicts(mods):
    """
    Detecteert dubbele bestandsnamen tussen mods.
    Retourneert een dict: { bestand: [mods die dit bestand bevatten] }
    """
    conflicts = {}
    seen_files = {}
    for mod in mods:
        for f in mod["files"]:
            if f in seen_files:
                if f not in conflicts:
                    conflicts[f] = [seen_files[f]]
                conflicts[f].append(mod["name"])
            else:
                seen_files[f] = mod["name"]
    return conflicts

def save_profile(name, mods):
    """
    Slaat een profiel op als JSON in ./profiles.
    """
    file = DEFAULT_PROFILES_PATH / f"{name}.json"
    with open(file, "w", encoding="utf-8") as f:
        json.dump(mods, f, indent=2)

def load_profile(name):
    """
    Laadt een profiel uit ./profiles.
    Retourneert een lijst van mods of lege lijst als niet gevonden.
    """
    file = DEFAULT_PROFILES_PATH / f"{name}.json"
    if not file.exists():
        return []
    with open(file, "r", encoding="utf-8") as f:
        return json.load(f)

def load_priorities(file="priority.json"):
    """
    Laadt prioriteiten uit priority.json.
    Formaat: { "ModNaam": prioriteit (int) }
    """
    path = Path(file)
    if not path.exists():
        return {}
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def sort_load_order(mods, priority_file="priority.json", use_priority=False):
    """
    Sorteert bestanden:
    - Standaard: ASCII sortering
    - Met use_priority=True: eerst op prioriteit, dan ASCII
    """
    priorities = load_priorities(priority_file) if use_priority else {}
    load_order = []
    for mod in mods:
        prio = priorities.get(mod["name"], 0)
        for f in mod["files"]:
            load_order.append((mod["name"], f, prio))
    # sorteer: eerst priority, dan ASCII
    load_order.sort(key=lambda x: (x[2], x[1]))
    return load_order

