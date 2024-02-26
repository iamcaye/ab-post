import customtkinter
from .image import ImageComponent
from PIL import Image


class ImageListComponent(customtkinter.CTkFrame):
    def __init__(self, app: customtkinter.CTk, images: list[str]) -> None:
        super().__init__(app)
        self.app = app
        self.images = sorted(images)
        self.loaded_images = [Image.open(image) for image in self.images]
        self.img_component = None
        self.image_id = 0
        self.current_label = None
        self.create_paginator()
        self.create_slider()

        if images and len(images) > 0:
            self.show_image(self.image_id)

    def on_previous(self) -> None:
        if self.image_id > 0:
            self.image_id -= 1
            self.show_image(self.image_id)
            self.slider.set(self.image_id)

    def on_next(self) -> None:
        if self.image_id < len(self.images) - 1:
            self.image_id += 1
            self.show_image(self.image_id)
            self.slider.set(self.image_id)

    def create_slider(self) -> None:
        self.slider = customtkinter.CTkSlider(self.master, from_=0, to=len(self.images) - 1, command=lambda value: self.show_image(int(value)))
        self.slider.grid(row=5, column=2, columnspan=10, padx=10, pady=10)
        self.slider.set(0)

    def create_paginator(self) -> None:
        self.previous_btn = customtkinter.CTkButton(self.master, text="Previous")
        self.previous_btn .grid(row=6, column=2, padx=5, pady=5)
        self.previous_btn.bind("<Button-1>", lambda event: self.on_previous())

        self.current_label = customtkinter.CTkLabel(self.master, text=f"{self.image_id + 1}/{len(self.images)}")
        self.current_label.grid(row=6, column=3, padx=5, pady=5)

        self.next_btn = customtkinter.CTkButton(self.master, text="Next")
        self.next_btn.grid(row=6, column=4, padx=5, pady=5)
        self.next_btn.bind("<Button-1>", lambda event: self.on_next())

    def show_image(self, id: int) -> None:
        self.img_component = ImageComponent(self.master, raw_img=self.loaded_images[id]).grid(row=1, column=2, columnspan=10, rowspan=3, padx=10, pady=10)

        self.current_label.configure(text=f"{id + 1}/{len(self.images)}")
