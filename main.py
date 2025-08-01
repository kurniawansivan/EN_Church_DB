import tkinter as tk
from core.init import initialize_database
from core.auth import is_profile_exists
from views.registration_form import show_registration_form
from views.login_form import show_login_form
from views.main_window import show_main_window

def main():
    initialize_database()

    root = tk.Tk()
    root.withdraw()  # Sembunyikan jendela utama sampai login/registrasi selesai

    def go_to_main_menu():
        root.deiconify()
        show_main_window(root)

    if not is_profile_exists():
        show_registration_form(root, on_success=go_to_main_menu)
    else:
        show_login_form(root, on_success=go_to_main_menu)

    root.mainloop()

if __name__ == "__main__":
    main()
