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

import os
PRIORITY_FILE = "priority.json"

def set_priority(mod_name, value=10):
    """Zet de prioriteit van een mod in priority.json."""
    data = {}
    if os.path.exists(PRIORITY_FILE):
        with open(PRIORITY_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
    if mod_name not in data:
        data[mod_name] = 0
    data[mod_name] = value
    with open(PRIORITY_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    messagebox.showinfo("Prioriteit aangepast", f"Mod '{mod_name}' heeft nu prioriteit {value}")

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

def save_order_from_tree(tree, filename="priority.json"):
    """Sla de huidige volgorde uit de Treeview op in priority.json."""
    order = []
    for item in tree.get_children():
        values = tree.item(item)["values"]
        order.append(values)

    # Bouw een dict {mod: prioriteit}
    data = {}
    for idx, row in enumerate(order):
        bestand, mod, prio = row
        # gebruik index als prioriteit als er geen waarde is
        data[mod] = idx

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    messagebox.showinfo("Load Order opgeslagen", f"Nieuwe volgorde opgeslagen in {filename}")

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

    # Dropdown + slider + knop voor oplossen
    choice_frame = ttk.Frame(frame_conflicts)
    choice_frame.pack(pady=10)

    ttk.Label(choice_frame, text="Kies winnaar:").pack(side="left", padx=5)

    mod_choice = ttk.Combobox(choice_frame, state="readonly")
    mod_choice.pack(side="left", padx=5)

    # Slider voor prioriteit
    prio_var = tk.IntVar(value=10)
    prio_slider = ttk.Scale(choice_frame, from_=0, to=100, orient="horizontal", variable=prio_var)
    prio_slider.pack(side="left", padx=5)
    ttk.Label(choice_frame, textvariable=prio_var).pack(side="left", padx=5)

    def update_dropdown(event):
        """Vul de dropdown met mods van de geselecteerde conflictregel."""
        sel = tree_conflicts.selection()
        if not sel:
            return
        values = tree_conflicts.item(sel[0])["values"]
        mods = values[1].split(", ")
        mod_choice["values"] = mods
        if mods:
            mod_choice.current(0)

    tree_conflicts.bind("<<TreeviewSelect>>", update_dropdown)

    def resolve_with_dropdown():
        """Geef de gekozen mod prioriteit (via slider)."""
        chosen = mod_choice.get()
        if not chosen:
            messagebox.showwarning("Geen keuze", "Selecteer eerst een conflict en kies een mod.")
            return
        value = prio_var.get()
        set_priority(chosen, value=value)

    ttk.Button(choice_frame, text="Laat deze mod winnen", command=resolve_with_dropdown).pack(side="left", padx=5)

    # Knoppen voor oplossen
    btn_frame_conf = ttk.Frame(frame_conflicts)
    btn_frame_conf.pack(pady=5)

    def resolve_with_mod(index):
        """Kies een mod uit de geselecteerde conflictregel en geef die prioriteit."""
        sel = tree_conflicts.selection()
        if not sel:
            messagebox.showwarning("Geen selectie", "Selecteer eerst een conflictregel.")
            return
        values = tree_conflicts.item(sel[0])["values"]
        mods = values[1].split(", ")
        if index < len(mods):
            chosen = mods[index]
            set_priority(chosen, value=10)

    ttk.Button(btn_frame_conf, text="Laat Mod A winnen", command=lambda: resolve_with_mod(0)).pack(side="left", padx=5)
    ttk.Button(btn_frame_conf, text="Laat Mod B winnen", command=lambda: resolve_with_mod(1)).pack(side="left", padx=5)

    # Load Order tab
    frame_order = ttk.Frame(notebook)
    notebook.add(frame_order, text="Load Order")

    columns_order = ("Bestand", "Mod", "Prioriteit")
    tree_order = ttk.Treeview(frame_order, columns=columns_order, show="headings")
    for col in columns_order:
        tree_order.heading(col, text=col)
        tree_order.column(col, width=250)
    tree_order.pack(fill="both", expand=True, padx=10, pady=10)

    # --- Drag & Drop functionaliteit ---
    def on_drag_start(event):
        item = tree_order.identify_row(event.y)
        if item:
            tree_order._drag_item = item

    def on_drag_motion(event):
        item = tree_order.identify_row(event.y)
        if item and hasattr(tree_order, "_drag_item"):
            tree_order.move(tree_order._drag_item, tree_order.parent(item), tree_order.index(item))

    def on_drag_stop(event):
        if hasattr(tree_order, "_drag_item"):
            del tree_order._drag_item
        # hier GEEN automatisch opslaan meer

    tree_order.bind("<ButtonPress-1>", on_drag_start)
    tree_order.bind("<B1-Motion>", on_drag_motion)
    tree_order.bind("<ButtonRelease-1>", on_drag_stop)

    # --- Knoppen onder de tabel ---
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

    def do_save_order():
        save_order_from_tree(tree_order)

    ttk.Button(btn_frame, text="Toon ASCII order", command=refresh_ascii).pack(side="left", padx=5)
    ttk.Button(btn_frame, text="Toon Priority order", command=refresh_priority).pack(side="left", padx=5)
    ttk.Button(btn_frame, text="Exporteren", command=do_export).pack(side="left", padx=5)
    ttk.Button(btn_frame, text="Importeren", command=do_import).pack(side="left", padx=5)
    ttk.Button(btn_frame, text="Opslaan volgorde", command=do_save_order).pack(side="left", padx=5)


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
