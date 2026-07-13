import customtkinter as ctk

from ui.sidebar import Sidebar
from ui.dashboard import Dashboard
from ui.statusbar import StatusBar


ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")


class DocumentEditorApp:

    def __init__(self):

        self.root = ctk.CTk()

        self.root.title("Document Editor Pro")

        self.root.geometry("1200x750")

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        self.sidebar = Sidebar(self.root)
        self.sidebar.grid(row=0, column=0, sticky="ns")

        self.dashboard = Dashboard(self.root)
        self.dashboard.grid(row=0, column=1, sticky="nsew")

        self.status = StatusBar(self.root)
        self.status.grid(
            row=1,
            column=0,
            columnspan=2,
            sticky="ew"
        )

    def run(self):

        self.root.mainloop()