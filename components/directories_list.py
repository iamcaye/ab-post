import customtkinter
from .image_list import ImageListComponent
from os import listdir


class DirectoriesListComponent(customtkinter.CTkScrollableFrame):
    def __init__(self, app: customtkinter.CTk, directories: list[str]) -> None:
        super().__init__(app)
        self.app = app
        self.directories = directories
        self.create_widgets()
        self.widgets = []
        self.image_component = None

    def on_click(self, directory: str) -> None:
        print(directory)
        if self.image_component:
            self.image_component.destroy()

        # get images from directory that ends with images file extension
        files = [f"{directory}/{file}" for file in listdir(directory) if file.endswith((".jpg", ".jpeg", ".png"))]

        self.image_component = ImageListComponent(self.app, files)
        self.image_component.grid(row=1, column=2, padx=10, pady=10)

    def create_widgets(self) -> None:
        for i, directory in enumerate(self.directories):
            widget = customtkinter.CTkButton(self, text=directory)
            widget.bind("<Button-1>", lambda event, directory=directory: self.on_click(directory))
            widget.grid(row=i, column=0, padx=5, pady=5, columnspan=2)
