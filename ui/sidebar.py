import customtkinter as ctk


class Sidebar(ctk.CTkFrame):

    def __init__(self, master, open_callback=None, analyze_callback=None):

        super().__init__(master, width=220)

        self.grid_propagate(False)

        title = ctk.CTkLabel(
            self,
            text="TOOLS",
            font=("Segoe UI", 18, "bold")
        )

        title.pack(pady=(20, 15))

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

        buttons = [
            "🧹 Clean",
            "🔢 Renumber",
            "✨ Format",
            "📤 Export",
            "⚙ Settings"
        ]

        for text in buttons:

            btn = ctk.CTkButton(
                self,
                text=text,
                height=40,
                state="disabled"
            )

            btn.pack(fill="x", padx=15, pady=5)