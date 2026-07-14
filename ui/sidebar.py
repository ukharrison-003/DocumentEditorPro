import customtkinter as ctk


class Sidebar(ctk.CTkFrame):

    def __init__(
        self,
        master,
        open_callback=None,
        analyze_callback=None,
        clean_callback=None,
        report_callback=None
    ):

        super().__init__(master, width=220)

        self.grid_propagate(False)

        title = ctk.CTkLabel(
            self,
            text="DOCUMENT EDITOR PRO",
            font=("Segoe UI", 18, "bold")
        )

        title.pack(pady=(20, 25))

        self.open_btn = ctk.CTkButton(
            self,
            text="📂 Open Document",
            command=open_callback,
            height=40
        )

        self.open_btn.pack(fill="x", padx=15, pady=5)

        self.analyze_btn = ctk.CTkButton(
            self,
            text="🔍 Analyze",
            command=analyze_callback,
            height=40
        )

        self.analyze_btn.pack(fill="x", padx=15, pady=5)

        self.clean_btn = ctk.CTkButton(
            self,
            text="🧹 Clean Document",
            command=clean_callback,
            height=40
        )

        self.clean_btn.pack(fill="x", padx=15, pady=5)

        self.report_btn = ctk.CTkButton(
            self,
            text="📄 Duplicate Report",
            command=report_callback,
            height=40
        )

        self.report_btn.pack(fill="x", padx=15, pady=5)

        self.export_btn = ctk.CTkButton(
            self,
            text="💾 Save Clean Copy",
            state="disabled",
            height=40
        )

        self.export_btn.pack(fill="x", padx=15, pady=5)

        self.settings_btn = ctk.CTkButton(
            self,
            text="⚙ Settings",
            state="disabled",
            height=40
        )

        self.settings_btn.pack(fill="x", padx=15, pady=5)