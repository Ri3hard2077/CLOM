import json
import os

def load_modlist():
    path = os.path.join("mods", "modlist.txt")
    if not os.path.exists(path):
        print("[CLOM] Geen modlist gevonden.")
        return []
    with open(path, "r") as f:
        return [line.strip() for line in f if line.strip()]

def load_order():
    with open("loadorder.json", "r") as f:
        return json.load(f)

def apply_order(modlist, order):
    print("=== Cyberpunk Load Order Manager (CLOM) ===")
    print("Mods gevonden:", modlist)
    print("Gewenste volgorde:", order)

    sorted_mods = sorted(modlist, key=lambda m: order.get(m, 999))
    print("Toegepaste volgorde:", sorted_mods)
    return sorted_mods

def main():
    modlist = load_modlist()
    order = load_order()
    apply_order(modlist, order)

if __name__ == "__main__":
    main()