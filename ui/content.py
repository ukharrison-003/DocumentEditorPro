import customtkinter as ctk


class Content(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(master)

        title = ctk.CTkLabel(
            self,
            text="Document Information",
            font=("Segoe UI", 24, "bold")
        )

        title.pack(pady=20)

        self.info = ctk.CTkTextbox(
            self,
            width=650,
            height=450
        )

        self.info.pack(fill="both", expand=True, padx=20, pady=20)

        self.info.insert(
            "end",
            "Welcome to Document Editor Pro\n\n"
            "Open a document to begin."
        )