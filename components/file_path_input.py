import customtkinter
from os import listdir
from os.path import isdir, join
from components.directories_list import DirectoriesListComponent
import tkinter as tk


class FilePathInputComponent(customtkinter.CTkFrame):
    def __init__(self, app: customtkinter.CTk) -> None:
        super().__init__(app)

        self.entry = customtkinter.CTkEntry(self, placeholder_text="Enter the path to the directory", width=300)
        self.entry.grid(row=0, column=0, padx=10, pady=10)
        self.entry.bind("<Return>", self.on_enter)

        self.browse_btn = customtkinter.CTkButton(self, text="Browse", command=self.browse)
        self.browse_btn.grid(row=0, column=1, padx=10, pady=10)

        self.button = customtkinter.CTkButton(self, text="Search")
        self.button.grid(row=0, column=2, padx=10, pady=10)
        self.button.bind("<Button-1>", self.on_enter)

    def browse(self) -> None:
        file = tk.filedialog.askdirectory()
        if file:
            self.entry.insert(0, file)

    def on_enter(self, _event: tk.Event) -> None:
        root = self.get_entry_value()
        if not root or root == "":
            return

        directories = self.get_directories_from_root(root)
        DirectoriesListComponent(self.master, directories).grid(row=1, column=0, rowspan=12)

    def get_entry_value(self) -> str:
        return self.entry.get()

    def get_directories_from_root(self, root: str) -> list[str]:
        return [d for d in listdir(root) if isdir(join(root, d)) and not d.startswith(".")]
