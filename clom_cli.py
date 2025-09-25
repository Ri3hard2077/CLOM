#!/usr/bin/env python3
"""
CLOM CLI – Cyberpunk Load Order Manager
Gebruikt functies uit clom.py
"""

import argparse
from pathlib import Path
from clom import load_mods, resolve_conflicts, save_profile, load_profile, sort_load_order

DEFAULT_MODS_PATH = Path("./mods")

def cmd_list(args):
    mods = load_mods(str(args.path or DEFAULT_MODS_PATH), extensions=args.ext)
    print(f"🔍 {len(mods)} mods gevonden:")
    for m in mods:
        print(f"- {m.get('name')} (v{m.get('version')})")
        files = m.get("files", [])
        if files:
            for f in files:
                print(f"   • {f}")
        else:
            print("   (geen bestanden gevonden)")

def cmd_resolve(args):
    mods = load_mods(str(args.path or DEFAULT_MODS_PATH), extensions=args.ext)
    conflicts = resolve_conflicts(mods)
    if conflicts:
        print(f"⚠️  {len(conflicts)} conflicterende bestanden gevonden:\n")
        for file, modlist in conflicts.items():
            print(f"  • {file}")
            for m in modlist:
                print(f"     ↳ {m}")
    else:
        print("✅ Geen conflicten!")

def cmd_profile_save(args):
    mods = load_mods(str(args.path or DEFAULT_MODS_PATH), extensions=args.ext)
    save_profile(args.name, mods)
    print(f"💾 Profiel '{args.name}' opgeslagen.")

def cmd_profile_load(args):
    mods = load_profile(args.name)
    if mods:
        print(f"📂 Profiel '{args.name}' geladen:")
        for m in mods:
            print(f"- {m.get('name')} (v{m.get('version')})")
            files = m.get("files", [])
            if files:
                for f in files:
                    print(f"   • {f}")
    else:
        print(f"⚠️  Profiel '{args.name}' niet gevonden.")

def cmd_order(args):
    mods = load_mods(str(args.path or DEFAULT_MODS_PATH), extensions=args.ext)
    order = sort_load_order(mods, use_priority=args.priority)
    if args.priority:
        print("📜 Load order (priority + ASCII sort):\n")
    else:
        print("📜 Load order (ASCII sort):\n")
    for mod, f, prio in order:
        if args.priority:
            print(f"{f}  ← {mod} (prio {prio})")
        else:
            print(f"{f}  ← {mod}")

def cmd_priority_init(args):
    mods = load_mods(str(args.path or DEFAULT_MODS_PATH), extensions=args.ext)
    priorities = {m["name"]: 0 for m in mods}

    file = Path(args.output or "priority.json")
    with open(file, "w", encoding="utf-8") as f:
        import json
        json.dump(priorities, f, indent=2)

    print(f"📝 Nieuw priority-bestand aangemaakt: {file}")
    print("Alle mods hebben nu prioriteit 0. Pas dit bestand handmatig aan om de volgorde te sturen.")

def main():
    parser = argparse.ArgumentParser(prog="clom", description="Cyberpunk Load Order Manager CLI")
    sub = parser.add_subparsers(dest="command", required=True)

    p_list = sub.add_parser("list", help="Toon mods en bestanden")
    p_list.add_argument("-p", "--path", help="Pad naar mods")
    p_list.add_argument("-e", "--ext", nargs="+", help="Filter op bestandsextensies (bijv. .archive .lua)")
    p_list.set_defaults(func=cmd_list)

    p_res = sub.add_parser("resolve", help="Detecteer conflicten")
    p_res.add_argument("-p", "--path", help="Pad naar mods")
    p_res.add_argument("-e", "--ext", nargs="+", help="Filter op bestandsextensies")
    p_res.set_defaults(func=cmd_resolve)

    p_save = sub.add_parser("profile-save", help="Sla profiel op")
    p_save.add_argument("name", help="Profielnaam")
    p_save.add_argument("-p", "--path", help="Pad naar mods")
    p_save.add_argument("-e", "--ext", nargs="+", help="Filter op bestandsextensies")
    p_save.set_defaults(func=cmd_profile_save)

    p_load = sub.add_parser("profile-load", help="Laad profiel")
    p_load.add_argument("name", help="Profielnaam")
    p_load.set_defaults(func=cmd_profile_load)

    p_prio = sub.add_parser("priority-init", help="Genereer priority.json met alle mods (prio 0)")
    p_prio.add_argument("-p", "--path", help="Pad naar mods")
    p_prio.add_argument("-e", "--ext", nargs="+", help="Filter op bestandsextensies")
    p_prio.add_argument("-o", "--output", help="Bestandsnaam voor priority.json")
    p_prio.set_defaults(func=cmd_priority_init)

    p_order = sub.add_parser("order", help="Toon load order (ASCII sort)")
    p_order.add_argument("-p", "--path", help="Pad naar mods")
    p_order.add_argument("-e", "--ext", nargs="+", help="Filter op bestandsextensies")
    p_order.add_argument("--priority", action="store_true", help="Gebruik priority.json voor sortering")
    p_order.set_defaults(func=cmd_order)

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
