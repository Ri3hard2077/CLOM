import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import json
from clom import load_mods, sort_load_order, resolve_conflicts

DEFAULT_MODS_PATH = "./mods"

# ---------------- Mods ----------------
def populate_mods(tree):
    """Laadt mods en toont ze in de Treeview."""
    mods = load_mods(DEFAULT_MODS_PATH)
    for mod in mods:
        files = len(mod.get("files", []))
        tree.insert("", "end", values=(mod["name"], mod.get("version", "1.0"), files))

# ---------------- Load Order ----------------
def populate_order(tree, use_priority=False):
    """Laadt load order en toont deze in de Treeview."""
    mods = load_mods(DEFAULT_MODS_PATH)
    order = sort_load_order(mods, use_priority=use_priority)
    for mod, f, prio in order:
        if use_priority:
            tree.insert("", "end", values=(f, mod, prio))
        else:
            tree.insert("", "end", values=(f, mod, ""))

def export_order(order, filename="loadorder.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(order, f, indent=2)
    messagebox.showinfo("Export", f"Load order geëxporteerd naar {filename}")

def import_order(filename="loadorder.json"):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            order = json.load(f)
        messagebox.showinfo("Import", f"Load order geïmporteerd uit {filename}")
        return order
    except FileNotFoundError:
        messagebox.showerror("Fout", f"Bestand {filename} niet gevonden")
        return []

# ---------------- Conflicten ----------------
def populate_conflicts(tree):
    """Laadt conflicten en toont ze in de Treeview."""
    mods = load_mods(DEFAULT_MODS_PATH)
    conflicts = resolve_conflicts(mods)
    for file, modlist in conflicts.items():
        tree.insert("", "end", values=(file, ", ".join(modlist)))

# ---------------- Profielen ----------------
def save_profile(name="default.json"):
    mods = load_mods(DEFAULT_MODS_PATH)
    data = [m["name"] for m in mods]
    with open(name, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    messagebox.showinfo("Profiel opgeslagen", f"Profiel opgeslagen als {name}")

def load_profile(name="default.json"):
    try:
        with open(name, "r", encoding="utf-8") as f:
            data = json.load(f)
        messagebox.showinfo("Profiel geladen", f"Profiel {name} geladen:\n{len(data)} mods")
        return data
    except FileNotFoundError:
        messagebox.showerror("Fout", f"Profiel {name} niet gevonden")
        return []

# ---------------- Main GUI ----------------
def main():
    root = tk.Tk()
    root.title("CLOM - Cyberpunk Load Order Manager")
    root.geometry("900x600")

    notebook = ttk.Notebook(root)
    notebook.pack(fill="both", expand=True)

    # Mods tab
    frame_mods = ttk.Frame(notebook)
    notebook.add(frame_mods, text="Mods")

    columns_mods = ("Naam", "Versie", "Aantal bestanden")
    tree_mods = ttk.Treeview(frame_mods, columns=columns_mods, show="headings")
    for col in columns_mods:
        tree_mods.heading(col, text=col)
        tree_mods.column(col, width=250)
    tree_mods.pack(fill="both", expand=True, padx=10, pady=10)

    populate_mods(tree_mods)

    # Conflicten tab
    frame_conflicts = ttk.Frame(notebook)
    notebook.add(frame_conflicts, text="Conflicten")

    columns_conflicts = ("Bestand", "Mods")
    tree_conflicts = ttk.Treeview(frame_conflicts, columns=columns_conflicts, show="headings")
    for col in columns_conflicts:
        tree_conflicts.heading(col, text=col)
        tree_conflicts.column(col, width=400)
    tree_conflicts.pack(fill="both", expand=True, padx=10, pady=10)

    populate_conflicts(tree_conflicts)

    # Load Order tab
    frame_order = ttk.Frame(notebook)
    notebook.add(frame_order, text="Load Order")

    columns_order = ("Bestand", "Mod", "Prioriteit")
    tree_order = ttk.Treeview(frame_order, columns=columns_order, show="headings")
    for col in columns_order:
        tree_order.heading(col, text=col)
        tree_order.column(col, width=250)
    tree_order.pack(fill="both", expand=True, padx=10, pady=10)

    btn_frame = ttk.Frame(frame_order)
    btn_frame.pack(pady=5)

    def refresh_ascii():
        tree_order.delete(*tree_order.get_children())
        populate_order(tree_order, use_priority=False)

    def refresh_priority():
        tree_order.delete(*tree_order.get_children())
        populate_order(tree_order, use_priority=True)

    def do_export():
        order = []
        for item in tree_order.get_children():
            order.append(tree_order.item(item)["values"])
        filename = filedialog.asksaveasfilename(defaultextension=".json")
        if filename:
            export_order(order, filename)

    def do_import():
        filename = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if filename:
            order = import_order(filename)
            tree_order.delete(*tree_order.get_children())
            for row in order:
                tree_order.insert("", "end", values=row)

    ttk.Button(btn_frame, text="Toon ASCII order", command=refresh_ascii).pack(side="left", padx=5)
    ttk.Button(btn_frame, text="Toon Priority order", command=refresh_priority).pack(side="left", padx=5)
    ttk.Button(btn_frame, text="Exporteren", command=do_export).pack(side="left", padx=5)
    ttk.Button(btn_frame, text="Importeren", command=do_import).pack(side="left", padx=5)

    # Profielen tab
    frame_profiles = ttk.Frame(notebook)
    notebook.add(frame_profiles, text="Profielen")

    ttk.Label(frame_profiles, text="Profielbeheer").pack(pady=10)

    btns = ttk.Frame(frame_profiles)
    btns.pack(pady=10)

    def do_save_profile():
        filename = filedialog.asksaveasfilename(defaultextension=".json")
        if filename:
            save_profile(filename)

    def do_load_profile():
        filename = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if filename:
            load_profile(filename)

    ttk.Button(btns, text="Profiel opslaan", command=do_save_profile).pack(side="left", padx=5)
    ttk.Button(btns, text="Profiel laden", command=do_load_profile).pack(side="left", padx=5)

    # Statusbalk
    status = tk.Label(root, text="Status: klaar", bd=1, relief="sunken", anchor="w")
    status.pack(side="bottom", fill="x")

    root.mainloop()

if __name__ == "__main__":
    main()
