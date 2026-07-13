import customtkinter as ctk

from tkinter import filedialog
from engine.analyzer import DocumentAnalyzer
from ui.sidebar import Sidebar
from ui.dashboard import Dashboard
from ui.statusbar import StatusBar


ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")


class DocumentEditorApp:

    def __init__(self):
        self.selected_file = ""
        self.analyzer = DocumentAnalyzer()

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
    def open_document(self):

        filename = filedialog.askopenfilename(
        filetypes=[("Word Documents", "*.docx")]
    )

        if filename:

            self.selected_file = filename

        self.status.set("Document selected.")

        self.dashboard.current_file.configure(
            text=f"Current File: {filename.split('/')[-1]}"
        )


    def analyze_document(self):

        if self.selected_file == "":

            self.status.set("Please open a document first.")

            return

        self.status.set("Analyzing document...")

        result = self.analyzer.analyze(self.selected_file)

        self.dashboard.update_statistics(result)

        self.status.set("Analysis complete.")

    def run(self):

        self.root.mainloop()