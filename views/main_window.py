import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from models.jemaat_model import get_all_jemaat, add_jemaat, update_jemaat, delete_jemaat
from utils.backup import backup_manual, backup_otomatis
from utils.xlsx_exporter import export_to_excel
from utils.backup import backup_manual, backup_otomatis, import_database

def show_main_window(root):
    root.title("Every Nation Church Database")
    root.geometry("1000x550")

    # --- SEARCH BAR ---
    search_var = tk.StringVar()

    def refresh_table(filtered_data=None):
        for row in tree.get_children():
            tree.delete(row)
        jemaat_list = filtered_data if filtered_data else get_all_jemaat()
        for idx, row in enumerate(jemaat_list, start=1):
            tree.insert("", tk.END, values=(idx, *row[1:]))

    def on_search(*args):
        keyword = search_var.get().lower()
        jemaat_list = get_all_jemaat()
        filtered = [
            r for r in jemaat_list
            if keyword in " ".join(str(x).lower() for x in r[1:])
        ]
        refresh_table(filtered)

    search_var.trace_add("write", on_search)

    frame_search = tk.Frame(root)
    frame_search.pack(pady=(10, 0))
    tk.Label(frame_search, text="Cari: ").pack(side=tk.LEFT)
    tk.Entry(frame_search, textvariable=search_var, width=50).pack(side=tk.LEFT, padx=5)

    # --- TABEL JEMAAT ---
    columns = (
        "No", "Nama Lengkap", "Alamat", "No. HP", "Tanggal Lahir", "Jenis Kelamin",
        "Status", "Pemuridan", "Baptis", "Pelayanan"
    )
    tree = ttk.Treeview(root, columns=columns, show="headings")
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)

    tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

    refresh_table()

    def open_form(jemaat=None):
        form = tk.Toplevel(root)
        form.title("Form Jemaat")

        labels = [
            "Nama Lengkap", "Alamat", "No. HP", "Tanggal Lahir",
            "Jenis Kelamin", "Status", "Riwayat Pemuridan", "Baptis", "Pelayanan"
        ]
        entries = []
        jenis_kelamin_opsi = ["Pria", "Wanita"]

        for i, label in enumerate(labels):
            tk.Label(form, text=label).grid(row=i, column=0, padx=10, pady=5, sticky="w")
            if label == "Jenis Kelamin":
                cb = ttk.Combobox(form, values=jenis_kelamin_opsi, state="readonly", width=37)
                cb.grid(row=i, column=1, pady=5)
                entries.append(cb)
            elif label == "Tanggal Lahir":
                tanggal = DateEntry(form, width=34, date_pattern="yyyy-mm-dd",
                                    background='darkblue', foreground='white',
                                    borderwidth=2, year=2000, month=1, day=1)
                tanggal.grid(row=i, column=1, pady=5)
                entries.append(tanggal)
            else:
                entry = tk.Entry(form, width=40)
                entry.grid(row=i, column=1, pady=5)
                entries.append(entry)

        if jemaat:
            for i in range(9):
                if hasattr(entries[i], 'delete'):
                    entries[i].delete(0, tk.END)
                    entries[i].insert(0, jemaat[i+1])
                elif hasattr(entries[i], 'set_date'):
                    entries[i].set_date(jemaat[i+1])

        def save():
            data = [e.get() for e in entries]
            if jemaat:
                update_jemaat(jemaat[0], data)
            else:
                add_jemaat(data)
            form.destroy()
            refresh_table()

        btn_text = "Update" if jemaat else "Simpan"
        tk.Button(form, text=btn_text, command=save).grid(row=9, column=1, pady=10)

    def edit_selected():
        selected = tree.focus()
        if not selected:
            messagebox.showwarning("Pilih data", "Pilih data jemaat yang ingin diedit.")
            return
        data = tree.item(selected)['values']
        jemaat = get_all_jemaat()[data[0] - 1]
        open_form(jemaat=jemaat)

    def delete_selected():
        selected = tree.focus()
        if not selected:
            messagebox.showwarning("Pilih data", "Pilih data jemaat yang ingin dihapus.")
            return
        data = tree.item(selected)['values']
        jemaat = get_all_jemaat()[data[0] - 1]
        confirm = messagebox.askyesno("Konfirmasi", f"Yakin hapus {jemaat[1]}?")
        if confirm:
            delete_jemaat(jemaat[0])
            refresh_table()

    frame_btn = tk.Frame(root)
    frame_btn.pack(pady=10)

    tk.Button(frame_btn, text="Tambah Jemaat", command=lambda: open_form()).pack(side=tk.LEFT, padx=10)
    tk.Button(frame_btn, text="Edit", command=edit_selected).pack(side=tk.LEFT, padx=10)
    tk.Button(frame_btn, text="Hapus", command=delete_selected).pack(side=tk.LEFT, padx=10)
    tk.Button(frame_btn, text="Backup Manual", command=backup_manual).pack(side=tk.LEFT, padx=10)
    tk.Button(frame_btn, text="Export ke Excel", command=export_to_excel).pack(side=tk.LEFT, padx=10)
    tk.Button(frame_btn, text="Import Database", command=lambda: [import_database(), refresh_table()]).pack(side=tk.LEFT, padx=10)

    def on_exit():
        backup_otomatis()
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_exit)
