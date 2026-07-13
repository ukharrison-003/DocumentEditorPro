import customtkinter as ctk


class Sidebar(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(master, width=220)

        self.grid_propagate(False)

        title = ctk.CTkLabel(
            self,
            text="TOOLS",
            font=("Segoe UI", 18, "bold")
        )

        title.pack(pady=(20, 15))

        buttons = [
            "📂 Open Document",
            "🔍 Analyze",
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
                height=40
            )

            btn.pack(fill="x", padx=15, pady=5)