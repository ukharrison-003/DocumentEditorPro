import customtkinter as ctk


class InfoCard(ctk.CTkFrame):

    def __init__(self, master, title, value="0"):
        super().__init__(master, corner_radius=10)

        self.title = ctk.CTkLabel(
            self,
            text=title,
            font=("Segoe UI", 14, "bold")
        )
        self.title.pack(anchor="w", padx=15, pady=(10, 5))

        self.value = ctk.CTkLabel(
            self,
            text=value,
            font=("Segoe UI", 28, "bold")
        )
        self.value.pack(anchor="w", padx=15, pady=(0, 10))

    def set_value(self, value):
        self.value.configure(text=str(value))


class Dashboard(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        title = ctk.CTkLabel(
            self,
            text="Dashboard",
            font=("Segoe UI", 28, "bold")
        )
        title.pack(anchor="w", padx=20, pady=(20, 10))

        self.current_file = ctk.CTkLabel(
            self,
            text="Current File: No document selected",
            font=("Segoe UI", 14)
        )
        self.current_file.pack(anchor="w", padx=20, pady=(0, 20))

        cards = ctk.CTkFrame(self, fg_color="transparent")
        cards.pack(fill="x", padx=20)

        cards.grid_columnconfigure((0, 1, 2), weight=1)

        self.paragraphs = InfoCard(cards, "Paragraphs")
        self.paragraphs.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.word_headings = InfoCard(cards, "Word Headings")
        self.word_headings.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        self.day_headings = InfoCard(cards, "Day Headings")
        self.day_headings.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")

        self.smart_topics = InfoCard(cards, "Smart Topics")
        self.smart_topics.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        self.duplicates = InfoCard(cards, "Duplicate Sections")
        self.duplicates.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

        self.blanks = InfoCard(cards, "Blank Paragraphs")
        self.blanks.grid(row=1, column=2, padx=10, pady=10, sticky="nsew")

        log_title = ctk.CTkLabel(
            self,
            text="Activity Log",
            font=("Segoe UI", 18, "bold")
        )
        log_title.pack(anchor="w", padx=20, pady=(20, 5))

        self.log = ctk.CTkTextbox(
            self,
            height=180
        )
        self.log.pack(fill="both", expand=True, padx=20, pady=(0, 20))

        self.log.insert("end", "Application started...\n")
        self.log.configure(state="disabled")

    def add_log(self, message):

        self.log.configure(state="normal")
        self.log.insert("end", f"• {message}\n")
        self.log.see("end")
        self.log.configure(state="disabled")

    def update_statistics(self, result):

        self.current_file.configure(
            text=f"Current File: {result.filename}"
        )

        self.paragraphs.set_value(result.paragraphs)

        self.word_headings.set_value(result.word_headings)

        self.day_headings.set_value(result.day_headings)

        self.smart_topics.set_value(result.smart_topics)

        self.duplicates.set_value(result.duplicate_sections)

        self.blanks.set_value(result.blank_paragraphs)