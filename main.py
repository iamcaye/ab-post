#!/usr/bin/python3.10
import customtkinter
from components.image import ImageComponent
from components.file_path_input import FilePathInputComponent


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("AB-post")
        # self.geometry("800x600")


app = App()
FilePathInputComponent(app).grid(row=0, column=0, padx=10, pady=10, columnspan=12)
app.mainloop()
