import os
import sys
import json
import tkinter as tk
from tkinter import messagebox

def resource_path(filename):
    """
    Zorgt dat bestanden altijd naast de .exe of .py gevonden worden.
    Dit voorkomt dat PyInstaller naar een tijdelijke map schrijft.
    """
    if getattr(sys, 'frozen', False):
        # Als we in een PyInstaller build zitten
        base_path = os.path.dirname(sys.executable)
    else:
        # Tijdens development
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, filename)

def load_config():
    path = resource_path("config.json")
    if os.path.exists(path):
        with open(path, "r") as f:
            return json.load(f)
    else:
        # standaardconfig als er geen config.json is
        return {"mod_folder": "test_mods"}

def load_modlist():
    # Lees config.json
    config = load_config()
    mod_folder = config.get("mod_folder", "test_mods")

    # Relatief pad → naast de .exe
    if not os.path.isabs(mod_folder):
        mod_folder = resource_path(mod_folder)

    if os.path.exists(mod_folder):
        mods = [f for f in os.listdir(mod_folder) if f.endswith(".archive")]
        if mods:
            print(f"[CLOM] {len(mods)} mods gevonden in {mod_folder}")
            return mods
        else:
            msg = f"[CLOM] Geen .archive bestanden gevonden in {mod_folder}"
            print(msg)
            try:
                root = tk.Tk()
                root.withdraw()
                messagebox.showwarning("CLOM", msg)
            except:
                pass
            return []
    else:
        msg = f"[CLOM] Map niet gevonden: {mod_folder}"
        print(msg)
        try:
            root = tk.Tk()
            root.withdraw()
            messagebox.showwarning("CLOM", msg)
        except:
            pass
        return []

def load_order():
    path = resource_path("loadorder.json")
    if not os.path.exists(path):
        print("[CLOM] Geen loadorder.json gevonden, maak een lege aan.")
        with open(path, "w") as f:
            json.dump({}, f)
        return {}
    with open(path, "r") as f:
        return json.load(f)

def interactive_reorder(mods):
    """
    Eenvoudig console-menu om mods handmatig te herschikken.
    """
    mods = mods[:]  # kopie
    while True:
        print("\nHuidige volgorde:")
        for i, mod in enumerate(mods):
            print(f"{i+1}. {mod}")

        print("\nOpties:")
        print("  m <nr> <up/down>  - verplaats mod omhoog/omlaag")
        print("  s                 - sla op en stop")
        print("  q                 - stop zonder opslaan")

        cmd = input("Voer commando in: ").strip().lower()
        if cmd == "s":
            return mods
        elif cmd == "q":
            return None
        elif cmd.startswith("m "):
            try:
                _, idx, direction = cmd.split()
                idx = int(idx) - 1
                if 0 <= idx < len(mods):
                    if direction == "up" and idx > 0:
                        mods[idx-1], mods[idx] = mods[idx], mods[idx-1]
                    elif direction == "down" and idx < len(mods)-1:
                        mods[idx+1], mods[idx] = mods[idx], mods[idx+1]
                    else:
                        print("Kan niet verder verplaatsen.")
                else:
                    print("Ongeldig nummer.")
            except Exception as e:
                print("Fout in commando:", e)
        else:
            print("Onbekend commando.")
    # einde while

def apply_order(modlist, order):
    print("=== Cyberpunk Load Order Manager (CLOM) ===")
    print("Mods gevonden:", modlist)

    # Standaard sortering: ASCII
    sorted_mods = sorted(modlist)
    print("Standaard volgorde (ASCII):", sorted_mods)

    # Interactieve aanpassing
    new_order = interactive_reorder(sorted_mods)
    if new_order is None:
        print("[CLOM] Geen wijzigingen opgeslagen.")
        return sorted_mods

    # Schrijf nieuwe volgorde naar loadorder.json
    path = resource_path("loadorder.json")
    order_dict = {mod: i for i, mod in enumerate(new_order)}
    with open(path, "w") as f:
        json.dump(order_dict, f, indent=4)

    print(f"[CLOM] Nieuwe loadorder opgeslagen in {path}")
    return new_order

def main():
    modlist = load_modlist()
    order = load_order()
    apply_order(modlist, order)

if __name__ == "__main__":
    main()
