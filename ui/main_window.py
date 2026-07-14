import customtkinter as ctk

from engine.document_cleaner import DocumentCleaner
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
        self.cleaner = DocumentCleaner()

        self.root = ctk.CTk()

        self.root.title("Document Editor Pro")

        self.root.geometry("1200x750")

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        self.sidebar = Sidebar(
            self.root,
            open_callback=self.open_document,
            analyze_callback=self.analyze_document,
            clean_callback=self.clean_document,
            report_callback=self.show_report
        )
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
        print("Button clicked")

        self.status.set("Document selected.")

        filename = filedialog.askopenfilename(
        filetypes=[("Word Documents", "*.docx")]
    )

        if filename:

            self.selected_file = filename

        self.status.set("Document selected.")

        self.dashboard.current_file.configure(
            text=f"Current File: {filename.split('/')[-1]}"
        )
        self.dashboard.add_log(
            f"Opened {filename.split('/')[-1]}"
        )

    def analyze_document(self):

        if self.selected_file == "":

            self.status.set("Please open a document first.")

            return

        self.status.set("Analyzing document...")
        self.dashboard.add_log(
            "Analysis started..."
)

        result = self.analyzer.analyze(self.selected_file)

        self.dashboard.update_statistics(result)
        self.dashboard.add_log(
            "Analysis completed."
)
    def show_report(self):

        self.dashboard.add_log(
        "Duplicate report is not available yet."
    )

        self.status.set(
        "Duplicate report coming soon."
    )


    def clean_document(self):

        if self.selected_file == "":

            self.status.set("Please open a document first.")
            return

        self.dashboard.add_log("Cleaning started...")
        self.status.set("Cleaning document...")

        output_file = self.selected_file.replace(
            ".docx",
            "_Cleaned.docx"
        )

        try:

            result = self.cleaner.clean(
                self.selected_file,
                output_file
            )

            self.dashboard.add_log(
                f"Original Blocks : {result['original']}"
            )

            self.dashboard.add_log(
                f"Duplicate Blocks Removed : {result['removed']}"
            )

            self.dashboard.add_log(
                f"Remaining Blocks : {result['cleaned']}"
            )

            self.dashboard.add_log(
                f"Saved as:\n{output_file}"
            )

            self.status.set("Cleaning completed successfully!")

        except Exception as e:

            self.dashboard.add_log(
                f"ERROR: {e}"
            )

            self.status.set("Cleaning failed.")

    def run(self):

        self.root.mainloop()