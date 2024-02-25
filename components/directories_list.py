import customtkinter
from os import listdir
from os.path import isfile, join
from components.image import ImageComponent
import random


class DirectoriesListComponent(customtkinter.CTkScrollableFrame):
    def __init__(self, app: customtkinter.CTk, directories: list[str]) -> None:
        super().__init__(app)
        self.directories = directories
        self.create_widgets()
        self.widgets = []
        self.image_component = None

    def on_click(self, directory: str) -> None:
        print(directory)
        if self.image_component:
            self.image_component.destroy()

        dir_files = [f for f in listdir(directory) if isfile(join(directory, f)) and f.endswith(('.png', '.jpg', '.jpeg'))]
        random_img = random.choice(dir_files)
        self.image_component = ImageComponent(self.master, f"{directory}/{random_img}")
        self.image_component.grid(row=1, column=1)

    def create_widgets(self) -> None:
        for i, directory in enumerate(self.directories):
            widget = customtkinter.CTkButton(self, text=directory)
            widget.bind("<Button-1>", lambda event, directory=directory: self.on_click(directory))
            widget.grid(row=i, column=0, padx=5, pady=5)
